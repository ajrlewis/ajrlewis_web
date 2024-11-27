# ajrlewis_web

A.J.R.Lewis Web served by FastAPI (optimized for Gandi.net deployment).

See the API docs: https://ajrlewis.com/api/docs

## Environment Variables

## MySQL Commands

```sql
show databases;
use ajrlewis_web;
show tables;
```

## Gandi Things

### Resetting logs

```bash
cd /srv/data/var/log/www/
echo "" > uwsgi.log
```

## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file or or see https://opensource.org/licenses/MIT for more details.

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

