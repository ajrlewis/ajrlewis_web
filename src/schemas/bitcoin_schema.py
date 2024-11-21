import marshmallow as ma


class BitcoinBlockRequestSchema(ma.Schema):
    timestamp = ma.fields.DateTime(meta={"description": ""}, required=False)


class BitcoinBlockResponseSchema(ma.Schema):
    block_id = ma.fields.String(meta={"description": "The block ID"})
    block_height = ma.fields.Integer(meta={"description": ""})
    block_timestamp = ma.fields.Integer(meta={"description": ""})
    block_nonce = ma.fields.Integer(meta={"description": ""})
    block_difficulty = ma.fields.Float(meta={"description": ""})
    block_tx_count = ma.fields.Integer(meta={"description": ""})
    block_mediantime = ma.fields.Integer(meta={"description": ""})


class BitcoinPriceRequestSchema(ma.Schema):
    currency = ma.fields.String(
        required=False,
        default="USD",
        meta={"description": "The name of the currency price of a bitcoin"},
    )


class BitcoinPriceResponseSchema(ma.Schema):
    currency_per_bitcoin = ma.fields.Float(
        meta={"description": "The price of a bitcoin in the supplied currency"},
    )
    sats_per_currency = ma.fields.Integer(
        meta={"description": "The price of a bitcoin in the supplied currency"},
    )
    currency = ma.fields.String(
        meta={"description": "The currency of the price of a bitcoin."},
    )
