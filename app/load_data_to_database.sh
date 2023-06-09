#!/bin/bash
mkdir app/load_data/dictionaries &&
python -m app.load_data.create &&
python -m app.load_data.loading &&
rm -r app/load_data/dictionaries