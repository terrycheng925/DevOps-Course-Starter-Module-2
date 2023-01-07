#!/bin/bash -e
poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
