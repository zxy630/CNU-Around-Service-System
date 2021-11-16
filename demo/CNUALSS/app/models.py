from app import db


class Cate(db.Model):
    plate = db.Column(db.Integer, nullable=False)  # 板块
    ID = db.Column(db.String(100), primary_key=True, nullable=True)  # 编号
    name = db.Column(db.String(125), nullable=False)  # 名称
    label = db.Column(db.String(100))  # 标签
    opening_hours = db.Column(db.String(125))  # 营业时间
    person_price = db.Column(db.Float(2))  # 人均价格
    telephone = db.Column(db.String(100))  # 电话
    address = db.Column(db.String(100))  # 地址
    special = db.Column(db.Text)  # 特色
    img_url = db.Column(db.String(125))  # 图片
    # 评价


class Beauty(db.Model):
    plate = db.Column(db.Integer, nullable=False)  # 板块
    ID = db.Column(db.String(100), primary_key=True, nullable=True)  # 编号
    name = db.Column(db.String(125), nullable=False)  # 名称
    label = db.Column(db.String(100))  # 标签
    opening_hours = db.Column(db.String(125))  # 营业时间
    person_price = db.Column(db.Float(2))  # 人均价格
    telephone = db.Column(db.String(100))  # 电话
    address = db.Column(db.String(100))  # 地址
    special = db.Column(db.Text)  # 特色
    img_url = db.Column(db.String(125))  # 图片
    # 评价


class Recreation(db.Model):
    plate = db.Column(db.Integer, nullable=False)  # 板块
    ID = db.Column(db.String(100), primary_key=True, nullable=True)  # 编号
    name = db.Column(db.String(125), nullable=False)  # 名称
    label = db.Column(db.String(100))  # 标签
    opening_hours = db.Column(db.String(125))  # 营业时间
    person_price = db.Column(db.Float(2))  # 人均价格
    telephone = db.Column(db.String(100))  # 电话
    address = db.Column(db.String(100))  # 地址
    special = db.Column(db.Text)  # 特色
    img_url = db.Column(db.String(655))  # 图片
    # 评价


class Hotel(db.Model):
    plate = db.Column(db.Integer, nullable=False)  # 板块
    ID = db.Column(db.String(100), primary_key=True, nullable=True)  # 编号
    name = db.Column(db.String(125), nullable=False)  # 名称
    label = db.Column(db.String(100))  # 标签
    opening_hours = db.Column(db.String(125))  # 营业时间
    person_price = db.Column(db.Float(2))  # 人均价格
    telephone = db.Column(db.String(100))  # 电话
    address = db.Column(db.String(100))  # 地址
    special = db.Column(db.Text)  # 特色
    img_url = db.Column(db.String(655))  # 图片
    # 评价