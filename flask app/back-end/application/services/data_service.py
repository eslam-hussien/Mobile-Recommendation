from application.models import Product, cpu
from application.app import db
from .algorithm import alg


class DataService:
    def __init__(self,  product_schema):
        self.product_schema = product_schema

    def add_product(self, prod):
        new_product = Product(prod["ram"], prod["storage_size"], prod["cpu_id"], prod["ppi"], prod["price_egp"], prod["selfie"],
                              prod["main_camera"], prod["battery_endurance_time"], prod["display_protection"], prod["mobile"], prod["make"], prod["thickness"], prod["edge"])

        db.session.add(new_product)
        db.session.commit()
        return new_product

    def get(self, id):
        return Product.query.get(id)

    def update_product(self, id, prod):
        old = self.get(id)
        if(old != None):
            old.update(prod)
            db.session.commit()
        return old

    def top10_battery(self):
        return Product.query.order_by(
            Product.battery_endurance_time.desc()).limit(10).all()

    def top10_camera(self):
        return Product.query.order_by(Product.main_camera.desc()).limit(10).all()

    def top10_ppi(self):
        return Product.query.order_by(Product.ppi.desc()).limit(10).all()

    def top10_cpu(self):
        return Product.query.join(cpu, cpu.cpu_id == Product.cpu_id).order_by(
            cpu.cpu_score.desc()).limit(10).all()

    def delete(self, id):
        product = self.get(id)
        db.session.delete(product)
        db.session.commit()
        return product

    def merge(self, dict1, dict2):
        res = {**dict1, **dict2}
        return res

    def serialize_product_cpu(self, raw_product):
        p = raw_product[0]
        c = raw_product[1]
        p1 = self.product_schema.dump(p)
        p2 = {"nram": p.nram, "nstorage_size": p.nstorage_size,
              "nppi": p.nppi, "nselfie": p.nselfie,
              "nmain_camera": p.nmain_camera, "nbattery_endurance_time": p.nbattery_endurance_time,
              "nmake": p.nmake, 'cpu_score': c.cpu_score}
        product = self.merge(p1, p2)

        return product

    def query_products_budget(self, budget=None):
        products = db.session.query(Product, cpu).join(cpu).filter(
            Product.price_egp <= budget if budget else True).all()
        return [self.serialize_product_cpu(p) for p in products]

    def get_recommended(self, data, level_weights, mapping):
        products = self.query_products_budget(data["budget"])
        return alg(data["interests"], products, level_weights, mapping)
