from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    username = fields.Str()
    password = fields.Str()