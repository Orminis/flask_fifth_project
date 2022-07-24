from enum import Enum


class UserRole(Enum):
    complainer = "Complainer"
    approver = "Approver"
    admin = "Admin"


class ComplaintState(Enum):
    pending = "Pending"
    approved = "Approved"
    declined = "Declined"
