# ajrlewis_web

A.J.R.Lewis Web served by FastAPI (optimized for Gandi.net deployment).

See the API docs: https://ajrlewis.com/api/docs

## Environment Variables

```sql
show databases;
use ajrlewis_web;
show tables;
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## TODO

### Using llmkit + imagekit

- image/card

- image/card/reader
    - Returns a V-card object of the supplied PNG image.

### Using imagekit + nostrkit

- nostr/events
    - get
        - query npub, kind, tags
    - post
        - nsec, kind, tags, content

- nostr/card
    - Given an npub, create back and front business card PNG

- web/
    Extracts text from website

