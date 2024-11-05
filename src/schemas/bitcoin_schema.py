import marshmallow as ma


class BitcoinBlockRequestSchema(ma.Schema):
    # timestamp = ma.fields.String(required=False)
    timestamp = ma.fields.DateTime(required=False)


# class BitcoinResponseSchema(ma.Schema):
#     answer = ma.fields.String(required=True)
