from typing import Optional

from fastapi import FastAPI

from models import customers, create_tables, User, Address
from db_operations import fetch_users_with_pagination,insert_records, fetch_records, fetch_users_with_addresses,execute_raw_sql

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/records")
def get_records():
    return fetch_records()
