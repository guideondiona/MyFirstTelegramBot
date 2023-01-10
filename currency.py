import requests
import json
import os

SITE = 'https://api.apilayer.com/currency_data/live?source=USD'
headers = {
    'apikey': os.getenv('apikey')
}


def getCur():
    try:
        responce = requests.get(SITE, headers=headers)
        with open('cur.json', 'w') as f:
            json.dump(json.loads(responce.text), f, indent=4)
        return 0
    except:
        return 1


def loadCur(val='USDKZT'):
    with open('cur.json') as f:
        raw = json.load(f)
    if 'USD' in val:
        return raw['quotes'].get(val, 0)
    fr, to = raw['quotes'].get('USD' + val[:3], 1), raw['quotes'].get('USD' + val[3:], 1)
    return to / fr


if __name__ == "__main__":
    loadCur(val='USDKZT')
