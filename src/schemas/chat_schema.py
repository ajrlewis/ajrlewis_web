import marshmallow as ma


class ChatExtractRequestSchema(ma.Schema):
    text = ma.fields.String(required=True)
    data_points = ma.fields.Dict(required=True)


class ChatExtractResponseSchema(ma.Schema):
    data_points = ma.fields.Dict(required=True)
