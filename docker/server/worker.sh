#!/bin/sh

exec celery -A src.celery.celery_app worker --loglevel=info
