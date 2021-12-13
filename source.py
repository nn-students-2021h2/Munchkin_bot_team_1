import json
import os
import sys

import requests
from dotenv import load_dotenv

# Loading bot's token from environment variable
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

if BOT_TOKEN is None:
    sys.exit(
        "There is no BOT_TOKEN in .env file or .env file does not exist.\n"
        "Exiting..."
    )

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"
PLACEHOLDER_MSG = "The bot is currently under development, please be patient."
LONG_POLLING_TIMEOUT = 10


def gameloop():
    ...


def main() -> None:
    last_update_id = None

    while True:
        r = requests.get(
            BASE_URL + "getUpdates",
            params={"offset": last_update_id, "timeout": LONG_POLLING_TIMEOUT},
        )
        response_dict = json.loads(r.text)

        print(r.status_code)
        print(r.text)

        for upd in response_dict["result"]:
            last_update_id = upd["update_id"] + 1
            msg = upd["message"]
            chat_id = msg["chat"]["id"]

            if "text" in msg:
                r = requests.post(
                    BASE_URL + "sendMessage",
                    params={"chat_id": chat_id, "text": PLACEHOLDER_MSG},
                )


if __name__ == "__main__":
    SystemExit(main())
