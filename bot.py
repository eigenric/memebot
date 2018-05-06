#!/usr/bin/env python

"""
Botcillo que envía memes personalizados
"""

import logging

from telegram.ext import Updater, CommandHandler
from config import TOKEN
from memegen import generar_meme


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def memerizar(bot, update, args):

    if update.message.text:

        generar_meme(" ".join(args), "meme.jpg")
        bot.send_photo(chat_id=update.message.chat_id, photo=open("memes/meme.jpg", "rb"))


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler("meme", memerizar, pass_args=True))

updater.start_polling()
updater.idle()
