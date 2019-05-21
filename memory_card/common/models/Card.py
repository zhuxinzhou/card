# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from config.DB import db


class Card(db.Model):
    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)

    # 会员id
    member_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

    # 卡片名字
    card_name = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue())

    # 卡片内容
    card_content = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())

    # 复习状态 已复习一次：1，以此类推
    study_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

    # 状态 0 未归档 1 已归档
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

    # 下次复习时间
    last_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    # 创建时间 插入数据库时间
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    fromid = db.Column(db.String(50))
