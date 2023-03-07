import requests
import os
import telebot
from telebot import types
import tweepy

consumer_key="IFFIRl234asdasdjs2dym7A2q"
consumer_secret="op3l0KEolTycasdasdasdadsp94jMq4QCh6Jz9C"
access_token="140336566533436586-6wSIxYVZa4ngQFvTZZXOPLwS5dnWgl"
access_token_secret="p7KK1f6ka2asdasdasdasdasdGNolOcx326rq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

bot = telebot.TeleBot("5965086266:AAE-Vjff9jpwMI-kBmYNaJLJasdasd0TX1Vw")

@bot.message_handler(commands=['Start'])
def start(message):
    global firstname, username
    username = message.from_user.username
    firstname = message.from_user.first_name
    #Make it unique, so that no one else can use this bot other than you
    if username == "YOUR-USER-NAME":
        bot.send_message(chat_id=message.chat.id, text="Welcome, Master! Please enter the tweet or send the text messages")

@bot.message_handler(func=lambda message: True)
@bot.message_handler(content_types=["photo"])
def tweet(message):
    global firstname, username
    username = message.from_user.username
    firstname = message.from_user.first_name
    print(message)
    if username == "YOUR-USER-NAME":
        tweet_text = None
        if message.caption is not None:
            tweet_text = message.caption
        elif message.text is not None:
            tweet_text = message.text
        else:
            tweet_text = None
#        print(tweet_text)
#        print(message)
        if not os.path.exists('images'):
                os.makedirs('images')
        if message.photo:
            photo_id = message.photo[-1].file_id
            photo_file = bot.get_file(photo_id)
            photo_path = photo_file.file_path
            photo_url = (f'https://api.telegram.org/file/bot{bot.token}/{photo_path}')
            photo_response = requests.get(photo_url)
            photo_path = os.path.join('images', 'file_0.jpg')
            with open(photo_path, 'wb') as f:  # save the image file in the 'images' directory with the file name 'file_0.jpg'
                f.write(photo_response.content)

            media = api.media_upload(photo_path)  # use the actual file path to upload the media
            api.update_status(status=tweet_text, media_ids=[media.media_id])
        else:
        	api.update_status(status=tweet_text)

        bot.send_message(chat_id=message.chat.id, text="Tweet sent!\n\n/Start to send more.")
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(15)

