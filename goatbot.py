from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import helpers
import logging
import os
import requests

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# Global shit
chosen_word = ''
taboo_word = ''
scramble_word = ''

def start(bot, update):
    update.message.reply_text('Fuck you!')


def help(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,
    text='''
    Commands that are available (so far):
        1 - word
        2 - taboo
        3 - scramble
        4 - trumptrump
    ''')


def word(bot, update):
    global chosen_word
    chosen_word = helpers.random_word(helpers.words)
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text=f'Type: {chosen_word}')


def is_right(bot, update):
    global chosen_word
    global taboo_word
    global scramble_word
    if update.message.text.lower() == chosen_word.lower():
        chat_id = update.message.chat_id
        user = update.message.from_user
        bot.sendMessage(chat_id, text=f'{user.first_name} got it first bitches!')
        chosen_word = ''
    
    if update.message.text.lower() == taboo_word.lower():
        chat_id = update.message.chat_id
        user = update.message.from_user
        bot.sendMessage(chat_id, text=f'{user.first_name} got that bitch right!')
        taboo_word = ''
    
    if update.message.text.lower() == scramble_word.lower():
        chat_id = update.message.chat_id
        user = update.message.from_user
        bot.sendMessage(chat_id, text=f'{user.first_name} is pretty smart. You should learn from that individual.')
        scramble_word = ''

def taboo(bot, update):
    global taboo_word
    taboo_word = helpers.random_word(helpers.words)
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    bot.sendMessage(chat_id, text='Word has been sent')
    bot.sendMessage(user_id, text=f'Your word is {taboo_word}')


def scramble(bot, update):
    global scramble_word
    scramble_word = helpers.random_word(helpers.words)
    assorted_word = helpers.scramble_words(scramble_word)
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text=f'Unscramble: {assorted_word}')


def trump_trump(bot, update):
    chat_id = update.message.chat_id

    r = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
    json_data = r.json()
    bot.sendMessage(chat_id, text=f"Our president once said: {json_data['message']}")



def error(bot, update, error):
    logger.warn(f'Update {update} caused error {error}')


def main():
    # updater = Updater(os.environ['TOKEN'])
    updater = Updater('321867389:AAHAAqfgadfrhSeTfzB2z6BDGPUP437jYp8')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('word', word))
    dp.add_handler(CommandHandler('taboo', taboo))
    dp.add_handler(CommandHandler('scramble', scramble))
    dp.add_handler(CommandHandler('trumptrump', trump_trump))
    dp.add_handler(MessageHandler(Filters.text, is_right))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
