from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import Unauthorized
from telegram.ext.dispatcher import run_async
import helpers
import logging
import os
import requests

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# Global shit
word_dict = {}
taboo_dict = {}
scramble_dict = {}
groups = [-1001064437849, -242949424]


def start(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text='No')


def help(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,
                    text='''
    Commands that are available (so far):
    1 - word
    2 - taboo
    3 - scramble
    4 - trumptrump
    5 - urban
    ''')

def word(bot, update):
    global word_dict
    word_dict[update.message.chat_id] = helpers.random_word(helpers.words)
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text=f'Type: {word_dict[update.message.chat_id]}')


def is_right(bot, update):
    global word_dict
    global taboo_dict
    global scramble_dict
    if update.message.chat_id in word_dict:
        if update.message.text.lower() == word_dict[update.message.chat_id].lower():
            chat_id = update.message.chat_id
            user = update.message.from_user
            bot.sendMessage(
                chat_id, text=f'{user.first_name} got it first!')
            del word_dict[update.message.chat_id]

    if update.message.chat_id in taboo_dict:
        if update.message.text.lower() == taboo_dict[update.message.chat_id].lower():
            chat_id = update.message.chat_id
            user = update.message.from_user
            bot.sendMessage(
                chat_id, text=f'{user.first_name} got it right!')
            del taboo_dict[update.message.chat_id]

    if update.message.chat_id in scramble_dict:
        if update.message.text.lower() == scramble_dict[update.message.chat_id].lower():
            chat_id = update.message.chat_id
            user = update.message.from_user
            bot.sendMessage(
                chat_id, text=f'{user.first_name} is pretty smart. You should learn from that individual.')
            del scramble_dict[update.message.chat_id]

        if "saul" in update.message.text.lower() and "gay" in update.message.text.lower():
            chat_id = update.message.chat_id
            bot.sendMessage(chat_id, text="Damn right. That guy is gay af")


def taboo(bot, update):
    global taboo_dict
    taboo_dict[update.message.chat_id] = helpers.random_word(helpers.words)
    chat_id = update.message.chat_id
    user = update.message.from_user
    try:
        bot.sendMessage(
            user.id, text=f'Your word is {taboo_dict[update.message.chat_id]}')
        bot.sendMessage(chat_id, text='Word has been sent')
    except Unauthorized:
        bot.sendMessage(
            chat_id, text=f'Hey {user.first_name}. I can not pm you unless you pm first.')


def scramble(bot, update):
    global scramble_dict
    scramble_dict[update.message.chat_id] = helpers.random_word(helpers.words)
    assorted_word = helpers.scramble_words(
        scramble_dict[update.message.chat_id])
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text=f'Unscramble: {assorted_word}')


@run_async
def trump_trump(bot, update):
    chat_id = update.message.chat_id

    r = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
    json_data = r.json()
    bot.sendMessage(
        chat_id, text=f"Our president once said: {json_data['message']}")


@run_async
def urban(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text[6:]

    try:
        r = requests.get(f'http://api.urbandictionary.com/v0/define?term={text}')
        json_data = r.json()
        define = json_data['list'][0]['definition']
        example = json_data['list'][0]['example']

        bot.sendMessage(chat_id, text=f'{text}\n{define}\n\n{example}')

    except IndexError:
        bot.sendMessage(chat_id, text='Stop playing around!')


@run_async
def echo(bot, update):
    global groups
    chat_id = update.message.chat_id

    if update.message.from_user.id == 224662703:
        text = update.message.text[6:]

        [bot.sendMessage(chat, text=f'{text}') for chat in groups]
    else:
        bot.sendMessage(
            chat_id, text='You"re not my creator')


def get_id(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text=f"The Chat id is: {chat_id}")

def random_god(bot, update):
    chat_id = update.message.chat_id
    user = update.message.from_user
    random_god = helpers.random_word(helpers.gods_list)
    bot.sendMessage(chat_id, text=f"{user.first_name}, your god to play is {random_god}")


def error(bot, update, error):
    logger.warn(f'Update {update} caused error {error}')


def main():
    updater = Updater(os.environ['TOKEN'])
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('word', word))
    dp.add_handler(CommandHandler('taboo', taboo))
    dp.add_handler(CommandHandler('scramble', scramble))
    dp.add_handler(CommandHandler('trumptrump', trump_trump))
    dp.add_handler(CommandHandler('echo', echo))
    dp.add_handler(CommandHandler('getid', get_id))
    dp.add_handler(CommandHandler('urban', urban))
    dp.add_handler(CommandHandler('randomgod', random_god))
    dp.add_handler(MessageHandler(Filters.text, is_right))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
