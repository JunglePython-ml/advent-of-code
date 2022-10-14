import requests
import time

import os
from dotenv import load_dotenv

day = time.strftime("%d")
year = time.strftime("%Y")
load_dotenv()
cookie = os.getenv('AOC_COOKIE')

url = f"https://adventofcode.com/{year}/day/{day}/input"
cookie = {'session': cookie}
r = requests.get(url, cookies=cookie)

with open(f'{year}/{day}.in', 'w') as f:
    f.write(r.text)