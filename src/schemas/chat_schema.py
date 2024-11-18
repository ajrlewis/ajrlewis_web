import marshmallow as ma


class ChatContextMessageSchema(ma.Schema):
    role = ma.fields.String(
        metadata={"description": "The role of the context message."}
    )
    content = ma.fields.String(
        metadata={"description": "The content of the context message."}
    )


class ChatRequestSchema(ma.Schema):
    context_messages = ma.fields.List(
        ma.fields.Nested(ChatContextMessageSchema),
        metadata={"description": "The context messages to pass to the LLM."},
    )


class ChatResponseSchema(ma.Schema):
    context_message = ChatContextMessageSchema


class ChatHumanizeRequestSchema(ma.Schema):
    text = ma.fields.String(meta={"description": "The text to humanize."})


class ChatHumanizeResponseSchema(ma.Schema):
    humanized_text = ma.fields.String(meta={"description": "The humanized text."})


class ChatAskRequestSchema(ma.Schema):
    question = ma.fields.String(meta={"description": "The question to ask the LLM."})


class ChatAskResponseSchema(ma.Schema):
    answer = ma.fields.String(
        meta={"description": "The answer to the question for the LLM."}
    )


class ChatKeywordsRequestSchema(ma.Schema):
    text = ma.fields.String(meta={"description": "The text to extract keywords from."})


class ChatKeywordsResponseSchema(ma.Schema):
    keywords = ma.fields.String(
        meta={"description": "The extracted keywords from the text."}
    )


class ChatExtractRequestSchema(ma.Schema):
    text = ma.fields.String(
        meta={"description": "The text to extract data points from."}
    )
    data_points = ma.fields.Dict(
        meta={
            "description": "The data points to extract, i.e. the name of the point and a description of what it is."
        }
    )


class ChatExtractResponseSchema(ma.Schema):
    data_points = ma.fields.Dict(
        meta={"description": "The extracted data points from the text."}
    )


class ChatSentimentResponseSchema(ma.Schema):
    sentiment = ma.fields.String(
        meta={"description": "The sentiment of the supplied text."}
    )


class ChatCodeRequestSchema(ma.Schema):
    language = ma.fields.String(
        meta={"description": "The computer language to develop the code in."}
    )
    description = ma.fields.String(
        meta={"description": "A description of what the code should do."}
    )


class ChatCodeResponseSchema(ma.Schema):
    code = ma.fields.String(
        meta={"description": "The code to do the description in the required language."}
    )
