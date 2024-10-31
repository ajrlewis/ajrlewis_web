import marshmallow as ma


class ChatExtractSchema(ma.Schema):
    text = ma.fields.String()
    data_points = ma.fields.Dict()
