from app import db
from sqlalchemy.dialects.postgresql import JSON


class CPU(db.Model):
    __tablename__ = 'cpu'

    cpu_id = db.Column(db.Integer, primary_key=True)
    cpu_rank = db.Column(db.Integer)
    cpu_model = db.Column(db.String(150))

    def __init__(self, cpu_id, cpu_rank, cpu_model):
        self.cpu_id = cpu_id
        self.cpu_rank = cpu_rank
        self.cpu_model = cpu_model

    def __repr__(self):
        return '<id {}>'.format(self.cpu_id)


class AllPhone(db.Model):
    __tablename__ = 'all_phone'
    mobile_id = db.Column(db.Integer, primary_key=True)
    ram = db.Column(db.Integer)
    storage_size = db.Column(db.Integer)
    cpu_id = db.Column(db.Integer, db.ForeignKey('cpu.cpu_id'))
    ppi = db.Column(db.Integer)
    price_egp = db.Column(db.Integer)
    rank_selfie = db.Column(db.Integer)
    rank_weights_selfie = db.Column(db.Integer)
    rank_maincamera = db.Column(db.Integer)
    rank_weights_mani_camera = db.Column(db.Integer)
    battery_endurance_time = db.Column(db.Integer)
    display_protection = db.Column(db.Boolean)
    mobile = db.Column(db.String(70))

    def __init__(self, mobile_id, ram, storage_size,
                 cpu_id, ppi, price_egp,
                 rank_selfie, rank_weights_selfie, rank_maincamera,
                 rank_weights_mani_camera, battery_endurance_time, display_protection, mobile):
        self.mobile_id = mobile_id
        self.ram = ram
        self.storage_size = storage_size
        self.cpu_id = cpu_id
        self.ppi = ppi
        self.price_egp = price_egp
        self.rank_selfie = rank_selfie
        self.rank_weights_selfie = rank_weights_selfie
        self.rank_maincamera = rank_maincamera
        self.rank_weights_mani_camera = rank_weights_mani_camera
        self.battery_endurance_time = battery_endurance_time
        self.display_protection = display_protection
        self.mobile = mobile

    def __repr__(self):
        return '<id {}>'.format(self.mobile_id)


class AffiliationBusiness(db.Model):
    __tablename__ = 'affiliation_business'
    aff_id = db.Column(db.Integer, primary_key=True)
    aff_name = db.Column(db.String(70))
    website_like = db.Column(db.String(500))

    def __init__(self, aff_id, aff_name, website_like):
        self.aff_id = aff_id
        self.aff_name = aff_name
        self.website_like = website_like

    def __repr__(self):
        return '<id {}>'.format(self.aff_id)


class AffiliationSelectedMobile(db.Model):
    __tablename__ = 'affiliation_selected_mobile'
    id = db.Column(db.Integer, primary_key=True)
    mobile_id = db.Column(db.Integer, db.ForeignKey(AllPhone.mobile_id))
    aff_id = db.Column(db.Integer, db.ForeignKey(AffiliationBusiness.aff_id))
    date_of_choice = db.Column(db.DateTime)

    def __init__(self, mobile_id, aff_id, date_of_choice):
        self.mobile_id = mobile_id
        self.aff_id = aff_id
        self.date_of_choice = date_of_choice

    def __repr__(self):
        return '<mobile_id {}, aff_id {}>'.format(self.mobile_id, self.aff_id)


