import logging
import os
import sys

from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater,
)

# Loading bot's token from environment variable
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

if BOT_TOKEN is None:
    sys.exit(
        "There is no BOT_TOKEN in .env file or .env file does not exist.\n" "Exiting..."
    )

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"
PLACEHOLDER_MSG = "The bot is currently under development, please be patient."
LONG_POLLING_TIMEOUT = 10

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(f"Привет, {update.effective_user.first_name}!")


def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Введи команду /start для начала. ")


def print_placeholder_text(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(PLACEHOLDER_MSG)


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f"Update {update} caused error {context.error}")


def gameloop():
    ...


def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    updater = Updater(bot=bot, use_context=True)

    updater = Updater(BOT_TOKEN, use_context=True)

    # on different commands - answer in Telegram
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", chat_help))

    # on noncommand i.e message - echo the message on Telegram
    updater.dispatcher.add_handler(MessageHandler(Filters.text, print_placeholder_text))

    # log all errors
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    logger.info("Start Bot")
    SystemExit(main())
