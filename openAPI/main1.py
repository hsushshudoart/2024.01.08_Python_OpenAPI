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

@app.get("/items/{item_id}")
async def get_item(item_id):
    print(f"使用者輸入了:{item_id}")        #f'字串' ->> 字串差補
    return {"item_id":item_id}
