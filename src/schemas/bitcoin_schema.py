import marshmallow as ma


class BitcoinBlockRequestSchema(ma.Schema):
    # timestamp = ma.fields.String(required=False)
    timestamp = ma.fields.DateTime(meta={"description": ""}, required=False)


class BitcoinBlockResponseSchema(ma.Schema):
    block_id = ma.fields.String(meta={"description": "The block ID"})
    block_height = ma.fields.Integer(meta={"description": ""})
    block_timestamp = ma.fields.Integer(meta={"description": ""})
    block_nonce = ma.fields.Integer(meta={"description": ""})
    block_difficulty = ma.fields.Float(meta={"description": ""})
    block_tx_count = ma.fields.Integer(meta={"description": ""})
    block_mediantime = ma.fields.Integer(meta={"description": ""})
