#! /usr/bin/env bash

init() {
    echo $PWD
    echo ">> alembic init alembic";
    alembic init alembic
    echo ">> writing alembic/env.py";
    cat << EOF > "alembic/env.py"
from logging.config import fileConfig
import os
import sys

sys.path.append("./ ")

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from models import Base

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


section = config.config_ini_section

config.set_section_option(
    section, "sqlalchemy.url", os.environ.get("SQLALCHEMY_DATABASE_URL")
)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    # almost identical to Flask-Migrate (Thanks miguel!)    
    # this callback is used to prevent an auto-migration from being generated
    # when there are no changes to the schema

    def process_revision_directives(context, revision, directives):
        if config.cmd_opts.autogenerate:
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                print('No changes in schema detected.')

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives
        )

        with context.begin_transaction():
            context.run_migrations() 

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
EOF
}

migrate() {
    echo '>> status=$(alembic revision --autogenerate -m "$1")';
    status=$(alembic revision --autogenerate -m "$1")
    echo $status
    echo ">> alembic upgrade head";
    alembic upgrade head
}

cd ../

if [ -d venv ]; then
    echo ">> source venv/bin/activate;";
    source venv/bin/activate;
fi
if [ -f .env ]; then
    echo ">> source .env;";
    source .env;
fi

if [ ! -d alembic ]; then
    init
fi

sleep 0.5

echo '>> migrate "$(git rev-parse HEAD)"'
migrate "$(git rev-parse HEAD)"
