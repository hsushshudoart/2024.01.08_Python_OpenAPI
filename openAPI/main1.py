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
