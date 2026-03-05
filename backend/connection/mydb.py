import os
import mysql.connector
from dotenv import load_dotenv
from typing import Any


def conn() -> Any:
    load_dotenv()

    mydb = mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE"),
        charset="utf8mb4",
    )
    return mydb  # noqa: RET504
