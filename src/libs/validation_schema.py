from marshmallow import fields, Schema, validate


class RegistrationSchema(Schema):
    nick = fields.Str(validate=validate.Length(min=3, max=150), required=True)
    email = fields.Email(required=True)
    password = fields.Str(validate=validate.Length(min=5), required=True)

class LoginSchema(Schema):
    remember = fields.Str()
    email = fields.Email(required=True)
    password=fields.Str(required=True)

