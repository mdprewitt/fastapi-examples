from fastapi import FastAPI
import asyncio
import time
import logging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()

app = FastAPI()


@app.get("/hc")
async def root():
    return {"message": "Hello World"}

@app.get("/slow")
async def slow():
    LOG.info("Start slow")
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    LOG.info("End slow")
    return {"message": "Sleepy World"}


@app.get("/bad-slow")
async def bad_slow():
    LOG.info("Start bad slow")
    time.sleep(10)
    LOG.info("End bad slow")
    return {"message": "Bad Sleepy World"}


