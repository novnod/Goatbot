from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(lebelnames)s - %(message)s')

logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')


def echo(bot, update):
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    logger.warn(f'Update {update} caused error {error}')


def main():
    # Create the EventHandler and pass it your token
    updater = Updater('232179235:AAG-ySLhZaTLdBsw8T7h7yXdm1RFKhQlu_A')

    # Get the dispatcher to register Handlers
    dp = updater.dispatcher

    # On different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    # On noncommand i.e messahe - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Starts the bot
    updater.start_polling()

    # Run the bot until you press Ctrl + c 
    # start_polling() is non blocking
    updater.idle()

if __name__ == '__main__':
    main()