#!/usr/bin/env bash

prod_path=/srv/revelation/
cd ${prod_path}

# Setting up virtualenv
source venv/bin/activate

./revelation/manage.py clearsessions

# Shutting down virtualenv
deactivate