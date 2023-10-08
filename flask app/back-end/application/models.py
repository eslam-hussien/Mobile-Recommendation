from .app import db, ma


class Product(db.Model):
    ram = db.Column(db.Integer)
    mobile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    storage_size = db.Column(db.Integer)
    cpu_id = db.Column(db.Integer, db.ForeignKey('cpu.cpu_id'))
    ppi = db.Column(db.Integer)
    price_egp = db.Column(db.Integer)
    selfie = db.Column(db.Integer)
    main_camera = db.Column(db.Integer)
    battery_endurance_time = db.Column(db.Integer)
    display_protection = db.Column(db.Integer)
    mobile = db.Column(db.String(70))
    make = db.Column(db.Integer)
    thickness = db.Column(db.Float)
    edge = db.Column(db.Integer)

    def __init__(self, ram, cpu_id, storage_size,
                 ppi, price_egp, selfie,
                 main_camera, battery_endurance_time, display_protection, mobile, make, thickness, edge):
        self.ram = ram
        self.storage_size = storage_size
        self.cpu_id = cpu_id
        self.ppi = ppi
        self.price_egp = price_egp
        self.selfie = selfie
        self.main_camera = main_camera
        self.battery_endurance_time = battery_endurance_time
        self.display_protection = display_protection
        self.mobile = mobile
        self.make = make
        self.thickness = thickness
        self.edge = edge

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def _normalize(self, value, att):
        max = db.session.query(db.func.max(getattr(Product, att))).scalar()
        min = db.session.query(db.func.min(getattr(Product, att))).scalar()
        if isinstance(max, int) and isinstance(min, int):
            return (value-min)/(max-min)
        else:
            print(
                f"invalid values in database : min: {min} and max: {max} for the attribute : {att}")
            return 0

    @property
    def nram(self):
        return self._normalize(self.ram, 'ram')

    @property
    def nstorage_size(self):
        return self._normalize(self.storage_size, 'storage_size')

    @property
    def nppi(self):
        return self._normalize(self.ppi, 'ppi')

    @property
    def nselfie(self):
        return self._normalize(self.selfie, 'selfie')

    @property
    def nmain_camera(self):
        return self._normalize(self.main_camera, 'main_camera')

    @property
    def nbattery_endurance_time(self):
        return self._normalize(self.battery_endurance_time, 'battery_endurance_time')

    @property
    def nmake(self):
        return self._normalize(self.make, 'make')


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('mobile_id ', 'ram', 'cpu_id', 'storage_size', 'ppi', 'price_egp', 'selfie', 'main_camera',
                  'battery_endurance_time', 'display_protection', 'mobile', 'make', 'thickness', 'edge')


class cpu(db.Model):
    cpu_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpu_score = db.Column(db.Integer)
    cpu_model = db.Column(db.String(150))


def __init__(self, cpu_id, cpu_score, cpu_model):
    self.cpu_id = cpu_id
    self.cpu_score = cpu_score
    self.cpu_model = cpu_model


class cpuSchema(ma.Schema):
    class Meta:
        fields = ('cpu_id', 'cpu_score', 'cpu_model')


class AffiliationBusiness(db.Model):
    aff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aff_name = db.Column(db.String(70))
    website_link = db.Column(db.String(500))

    def __init__(self, aff_id, aff_name, website_link):
        self.aff_id = aff_id
        self.aff_name = aff_name
        self.website_like = website_link


class AffiliationBusinessSchema(ma.Schema):
    class Meta:
        fields = ('aff_id', 'aff_name', 'website_link')


class AffiliationSelectedMobile(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    mobile_id = db.Column(db.Integer, db.ForeignKey(Product.mobile_id))
    aff_id = db.Column(db.Integer, db.ForeignKey(AffiliationBusiness.aff_id))
    date_of_choice = db.Column(db.DateTime)

    def __init__(self, mobile_id, aff_id, date_of_choice):
        self.mobile_id = mobile_id
        self.aff_id = aff_id
        self.date_of_choice = date_of_choice


class AffiliationSelectedMobileSchema(ma.Schema):
    class Meta:
        fields = ('mobile_id', 'aff_id', 'date_of_choice')


cpu_schema = cpuSchema()
cpu_schema = cpuSchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# AffiliationBusiness_schema = AffiliationBusinessSchema()
# AffiliationBusiness_schema = AffiliationBusinessSchema(many=True)

# AffiliationSelectedMobile_schema = AffiliationSelectedMobileSchema()
# AffiliationSelectedMobile_schema = AffiliationSelectedMobileSchema(many=True)
