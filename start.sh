#!/bin/sh
gunicorn --config gunicorn_config.py wsgi:app