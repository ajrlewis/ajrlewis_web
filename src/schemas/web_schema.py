import marshmallow as ma


class WebScrapeQueryArgsSchema(ma.Schema):
    url = ma.fields.String(metadata={"description": "The URL to extract data from."})


class WebScrapeImageTagSchema(ma.Schema):
    alt = ma.fields.String(
        metadata={"description": "The alternative text for the tag."}
    )
    src = ma.fields.String(metadata={"description": "The image source for the tag."})


class WebScrapeAnchorTagSchema(ma.Schema):
    href = ma.fields.String(metadata={"description": "The hyperlink for the tag."})


class WebScrapeResponseSchema(ma.Schema):
    url = ma.fields.String(metadata={"description": "The supplied URL."})
    sanitized_url = ma.fields.String(metadata={"description": "The sanitized URL."})
    redirected_url = ma.fields.String(
        metadata={"description": "The final redirected URL."}
    )
    text = ma.fields.String(
        metadata={"description": "The visible text of the website."}
    )
    error = ma.fields.String(
        metadata={"description": "The error response if anything goes well."}
    )
    is_reachable = ma.fields.Bool(
        metadata={"description": "The the website reachable?"}
    )
    scraped_on = ma.fields.DateTime(
        metadata={"description": "When the website was scraped."}
    )
    image_tags = ma.fields.List(
        ma.fields.Nested(WebScrapeImageTagSchema),
        metadata={"description": "The image tags with alternative text descriptions."},
    )
    anchor_tags = ma.fields.List(
        ma.fields.Nested(WebScrapeAnchorTagSchema),
        metadata={"description": "The anchor tags on the website."},
    )


class WebSearchQueryArgsSchema(ma.Schema):
    keywords = ma.fields.String(metadata={"description": "The keywords to search for."})
    max_results = ma.fields.Integer(
        metadata={"description": "Number of results to return."}
    )


class WebSearchResultSchema(ma.Schema):
    title = ma.fields.String(
        metadata={"description": "The title of the search result."}
    )
    body = ma.fields.String(metadata={"description": "The body of the search result."})
    href = ma.fields.String(metadata={"description": "The link of the search result."})


class WebSearchResponseSchema(ma.Schema):
    results = ma.fields.List(
        ma.fields.Nested(WebSearchResultSchema),
        metadata={"description": "The list of search results."},
    )
