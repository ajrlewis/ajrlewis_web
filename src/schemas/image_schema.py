import marshmallow as ma


class ImageRequestSchema(ma.Schema):
    file = ma.fields.Field(
        description="The image to upload.",
        metadata={"type": "string", "format": "binary"},
        required=True,
    )


class ImageCreateRequestSchema(ma.Schema):
    prompt = ma.fields.String(
        description="The prompt to create an image from.", required=True
    )


class ImageResponseSchema(ma.Schema):
    image = ma.fields.Field(
        description="The downloadable image.",
        metadata={"type": "string", "format": "binary"},
        required=True,
    )


class ImageTextExtractResponseSchema(ma.Schema):
    text = ma.fields.String(
        description="The text extracted from the image.", required=True
    )
