from common.tester import Tester
import common.configs as cfg
from fastapi import FastAPI

app = FastAPI()

tester = Tester(cfg.ACCESS_TOKEN, cfg.FILE, f'common/resources/{cfg.FILE}')


@app.post("/image")
def upload_file():
    return tester.upload()


@app.get("/image/metadata")
def file_get_metadata():
    return tester.get_metadata()


@app.delete("/del")
def delete_file():
    return tester.delete()
