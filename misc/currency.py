import requests
import json
import os
from config import config
import pathlib
from time import time


BASE_DIR = pathlib.Path(__file__).parent.parent


def getCur():
    if os.path.exists(BASE_DIR / "cur.json"):
        with open(BASE_DIR / "cur.json") as f:
            date = int(json.loads(f.read()).get("timestamp", 0))
        if time() - date < 28800:
            print("Alredy updated")
            return 2

    try:
        responce = requests.get(
            url="https://api.apilayer.com/currency_data/live?source=USD",
            headers={"apikey": config.api_key.get_secret_value()},
        )
        with open("cur.json", "w") as f:
            json.dump(json.loads(responce.text), f, indent=4)
        return 0
    except Exception as ex:
        print(ex)


def loadCur(val="USDKZT"):
    getCur()
    with open("cur.json") as f:
        raw = json.load(f)
    if "USD" in val:
        return raw["quotes"].get(val, 0)
    fr, to = raw["quotes"].get("USD" + val[:3], 1), raw["quotes"].get(
        "USD" + val[3:], 1
    )
    return to / fr


if __name__ == "__main__":
    loadCur(val="USDKZT")
