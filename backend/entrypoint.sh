#!/bin/bash
set -e

echo "Waiting for database..."
until python -c "
import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE'),
    charset='utf8mb4'
).close()
" 2>/dev/null; do
    sleep 2
done
echo "Database ready."

TABLE_COUNT=$(python -c "
import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
db = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE'),
    charset='utf8mb4'
)
cur = db.cursor()
cur.execute('SHOW TABLES')
print(len(cur.fetchall()))
")

if [ "$TABLE_COUNT" -eq "0" ]; then
    echo "Loading dictionary data..."
    mkdir -p backend/load_data/dictionaries
    python -m backend.load_data
    rm -rf backend/load_data/dictionaries
    echo "Dictionary loaded."
fi

exec uvicorn backend.main:app --host 0.0.0.0 --port 8000
