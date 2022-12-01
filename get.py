import requests
import time
import sys

import os
from dotenv import load_dotenv

load_dotenv()
cookie = os.getenv('AOC_COOKIE')

WARNING_MESSAGE = "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is " \
                  "synchronized with the server time; the link will be enabled on the calendar the instant this " \
                  "puzzle becomes available.\n"


def progress_bar(year, day):
    filled_length = int(50 * (year - 2015) + 2 * day - 1) // (time.localtime().tm_year - 2015)
    bar = "█" * filled_length + "-" * (50 - filled_length)
    sys.stdout.write(f"\r|{bar}| {year}/{day} ")
    sys.stdout.flush()


def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = requests.get(url, cookies={"session": cookie})
    return r.text


def get_all():
    years = time.localtime().tm_year
    for year in range(2015, years + 1):
        for day in range(1, time.localtime().tm_mday + 1 if year == years else 26):
            if not os.path.exists(f"{year}/{day}.in"):
                inp = get_input(year, day)
                if inp == WARNING_MESSAGE:
                    print("\nChallenge not unlocked yet.")
                    return
                with open(f"{year}/{day}.in", "w") as input_file:
                    input_file.write(inp)
            progress_bar(year, day)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        y, d = sys.argv[1:]
        with open(f"{y}/{d}.in", "w") as f:
            f.write(get_input(y, d))
    else:
        for y in range(2015, time.localtime().tm_year + 1):
            if not os.path.exists(f"{y}"):
                os.mkdir(f"{y}")
        get_all()
