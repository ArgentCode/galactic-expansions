#!/bin/sh
pip install -r requirements.txt
exec flask --app flaskoffun.py run --host=0.0.0.0