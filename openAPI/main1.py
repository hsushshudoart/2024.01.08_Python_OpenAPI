from typing import Union
from fastapi import FastAPI

import redis
import os
from dotenv import load_dotenv
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
"""
@app.get("/items/{item_id}")
async def get_item(item_id):
    print(f"使用者輸入了:{item_id}")        #f'字串' ->> 字串差補
    return {"item_id":item_id}
"""
@app.get("/items/{item_id}")
async def get_item(item_id:int):            #路徑參數:type ->> type hint
    print(f"使用者輸入了:{item_id}")
    return {"item_id":item_id}

@app.get("/items/{date}/{celsius}")         #2個路徑參數 Path Parameter
async def get_item(date:str,celsius:float):
    print(f"日期:{date}")
    print(f"溫度:{celsius}")
    return {"日期":date,"攝氏溫度":celsius}

#Query Parameter
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]