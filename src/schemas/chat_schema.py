import marshmallow as ma


class ChatAskRequestSchema(ma.Schema):
    question = ma.fields.String(required=True)


class ChatAskResponseSchema(ma.Schema):
    answer = ma.fields.String(required=True)


class ChatExtractRequestSchema(ma.Schema):
    text = ma.fields.String(required=True)
    data_points = ma.fields.Dict(required=True)


class ChatExtractResponseSchema(ma.Schema):
    data_points = ma.fields.Dict(required=True)


class ChatRequestSchema(ma.Schema):
    text = ma.fields.String(required=True)


class ChatResponseSchema(ma.Schema):
    content = ma.fields.String(required=True)


class ChatCodeRequestSchema(ma.Schema):
    language = ma.fields.String(required=True)
    description = ma.fields.String(required=True)


class ChatCodeResponseSchema(ma.Schema):
    code = ma.fields.String(required=True)
