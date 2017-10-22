import copy
import mainfunc
import YandexAPI_func

YaURL = 'https://api.rasp.yandex.net/v3.0/search/?'
big_dict = open('big_dict.txt', 'r')


hi = ['Здаров', 'Привет', 'Здорова', 'Здарова', 'Hi', 'Hello', 'Хай']
yes = ['да', 'Да', 'Yes', 'yes']



print ('start')
while True:
    infMessage = mainfunc.get_message()
    if infMessage is not None:
        id = infMessage['chat_id']
        text = infMessage['text']
        if text in hi:
            send_message(id, send_hi)

