#!/bin/bash
mkdir app/load_data/dictionaries &&
python -m app.load_data &&
rm -r app/load_data/dictionaries