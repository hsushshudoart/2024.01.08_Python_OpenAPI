from typing import Union

from fastapi import FastAPI

import redis
import os
from dotenv import load_dotenv
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()

#@app.get("/") ->> 接收值的網上通道
@app.get("/")
def read_root():
    counter = redis_conn.incr('test:increment', 1)
    return {'Counter': counter}

@app.get("/counter/{c}")       #c ->> 路徑參數
def counter(c:int):
    counter = redis_conn.incr('test:increment', c)
    return {'Counter': counter}

""""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
"""
'''
#給pico_w用的
@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float=0.0):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    return {"狀態":"儲存成功"}
'''
'''
#給pico_w用的
@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):       #celsius:float ->>沒有給預設值,在執行的時候一定要有這個值才可以跑
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    print(f"亮度:{light}")
    return {"狀態":"儲存成功"}
'''


#連接到Redis資料庫
@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):       #celsius:float ->>沒有給預設值,在執行的時候一定要有這個值才可以跑
    #print(f"日期:{date}")
    redis_conn.rpush('pico_w:date', date)
    #print(f"位置:{address}")
    redis_conn.hset('pico_w:address',mapping={date:address})
    #print(f"攝氏:{celsius}")
    redis_conn.hset('pico_w:temperature',mapping={date:celsius})
    #print(f"亮度:{light}")
    redis_conn.hset('pico_w:light',mapping={date:light})

    date_get = redis_conn.lrange('pico_w:date', -1,-1)[0].decode()      #('pico_w:date', -1,-1) ->>從 第-1個 到 第-1個
    address_get = redis_conn.hget('pico_w:address',date_get).decode()
    temperature_get = redis_conn.hget('pico_w:temperature',date_get).decode()
    light_get = redis_conn.hget('pico_w:light',date_get).decode()
    print(date_get)
    print(address_get)
    print(temperature_get)
    print(light_get)

    return {"狀態":"儲存成功"}