#! /usr/bin/env bash

init() {
    echo ">>> flask db init";
    flask db init
    echo 'flask db migrate -m "init"';
    flask db migrate -m "init"
    echo ">>> flask db upgrade";
    flask db upgrade
}

migrate() {
    flask db migrate -m "{$1}"
    flask db upgrade
}

if [ -d venv ]; then
    echo ">>> source venv/bin/activate;";
    source venv/bin/activate;
fi

if [ -f .env ]; then
    echo ">>> source .env;";
    source .env;
fi

if [ ! -d migrations ]; then
    echo ">>> init";
    init
else
    echo '>>> migrate "$(git rev-parse HEAD)'
    migrate "$(git rev-parse HEAD)"
fi

