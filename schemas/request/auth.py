from marshmallow import fields, validate
from schemas.request.base import AuthBase


# сега са основни и мога да ги допълним
class RegisterSchemaRequest(AuthBase):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=100))


class LoginSchemaRequest(AuthBase):
    pass
