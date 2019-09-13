import json
import time
from json import JSONDecodeError

import requests

from common.utils import Db

base_url = "https://api.cryptonator.com/api/ticker/"
db = Db()


def update_rate():
    pairs = db.get_all_pairs()
    for pair in pairs:
        response = requests.get(base_url + pair)
        try:
            parsed = json.loads(response.text)
        except (JSONDecodeError,):
            continue
        try:
            rate = float(parsed["ticker"]["price"])
        except (KeyError,):
            continue
        db.set_or_update_currency_rate(pair, rate)


# bad code(
while True:
    time.sleep(10)
    update_rate()
