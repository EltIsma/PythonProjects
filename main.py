
import os
from time import sleep

import telegram



def post_endlessly(bot, chat_id, posting_period):
    while True:
        for root, dirs, files in os.walk("images1"):
            for filename in files:
                image_path = f"{root}/{filename}"
                with open(image_path, "rb") as file:
                    photo = file.read()
                bot.send_photo(chat_id=chat_id, photo=photo)
                sleep(float(posting_period))


if __name__ == '__main__':
    tg_token = "5652546468:AAHseaoIdJgHoPgI5uIHOtG28RlfXGvUaS0"
    chat_id ="@nasaElt"
    posting_period =60
    bot = telegram.Bot(token=tg_token)
    post_endlessly(bot, chat_id, posting_period)
bot.polling()