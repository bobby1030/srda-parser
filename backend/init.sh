#!/bin/sh

# Build the database and start the server
python3 -m backend &&
    gunicorn -w 4 -b 0.0.0.0:5000 backend.api.api:api
