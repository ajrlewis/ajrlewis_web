import marshmallow as ma


class WebScrapeSchema(ma.Schema):
    web_id = ma.fields.Int(dump_only=True)
    url = ma.fields.String()
    sanitized_url = ma.fields.String()
    redirected_url = ma.fields.String()
    text = ma.fields.String()
    error = ma.fields.String()
    is_reachable = ma.fields.Bool()
    scraped_on = ma.fields.DateTime()


class WebScrapeQueryArgsSchema(ma.Schema):
    url = ma.fields.String(metadata={"description": "The URL to extract text from."})


class WebSearchSchema(ma.Schema):
    results = ma.fields.List(ma.fields.Dict())


class WebSearchQueryArgsSchema(ma.Schema):
    keywords = ma.fields.String(metadata={"description": "The keywords to search for."})
    max_results = ma.fields.Integer(
        metadata={"description": "Number of results to return."}
    )
