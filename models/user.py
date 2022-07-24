from db import db
from models.enums import UserRole


# основен клас за всички потребители
class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)


# клас за потребителите които имат оплакване
class ComplainerModel(BaseUserModel):
    __tablename__ = "complainers"

    role = db.Column(db.Enum(UserRole), default=UserRole.complainer, nullable=False)
    complains = db.relationship("ComplaintModel", backref="complaint", lazy="dynamic")


class ApproverModel(BaseUserModel):
    __tablename__ = "approvers"

    role = db.Column(db.Enum(UserRole), default=UserRole.approver, nullable=False)


class AdminModel(BaseUserModel):
    __tablename__ = "admins"

    role = db.Column(db.Enum(UserRole), default=UserRole.admin, nullable=False)
