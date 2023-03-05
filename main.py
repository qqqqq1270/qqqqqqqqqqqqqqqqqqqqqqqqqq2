from typing import Any
import bot
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randrange
import requests
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import threading
import re
import configparser
from vk_api import VkTools
import database



# Импортируем библиотеку vk_api
import vk_api
# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType
import pandas as pd

# Создаём переменную для удобства в которой хранится наш токен от группы

token = "vk1.a.07rHbbJwwXNuw6G57_fYTPztuM_YDYZAtkJGAUsJClesxa2CagyoMsU8ZSonIefjlQFFpT9nIGxxJQ9rm_TuPDiI3UbdVIY6Zq1TlYiwYCohnVURXXJ2Ul-DdlZSBqQFljPWyKjlZJTVm7C-su6fMPDmY_Ejo1SwUqHPrncH-iB9moew54Hz0WZxv_JtiPQO1pXEugC7qr2VeSdH60-iNQ"  # В ковычки вставляем аккуратно наш ранее взятый из группы токен.
token1 = "vk1.a.DORfAY-ITv15OOeopjNGLpGXe8b93O3NvCqWTKEIFez4emjJ_al1_H6w-HrvQAzVJCSzmpZ3M4_F0RdfR9P5jx6zZfqgIPilx2Fux9ovGOcoAx4osHv2oaxNXIWMmUHvBXkyE5srEhAWPQfCsSKTa2j8t5fS9uqy92fw8N3yjibjF9IIVmJiy5k9gafFI_pRY_0osB8e2wpRfRlOORxx6g"

vk = vk_api.VkApi(token=token)
vk1 = vk_api.VkApi(token=token1)

nomer = 0
longpoll = VkLongPoll(vk)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        message = event.text.lower()
        nomer1 = 0

        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            qqqq = (bot.user_data(id))
            bot.bot_write(id, f"Здравствуйте, {qqqq[0]}")

            pfoto1 = bot.photos_partner(id,nomer1)


            if event.to_me:

               print(qqqq)
               if message == "привет":
                    bot.bot_write(event.user_id, f"Хай, {event.user_id}")
               elif message == "пока":
                    bot.bot_write(event.user_id, "Пока((")
               elif message == 'Данные':
                   bot.bot_write(id, f"Здравствуйте, {qqqq[0]}")
                   bot.bot_write(id, f"Здравствуйте, {qqqq[0]}")
               elif message == 'w':
                   bot.main_function(id, event, nomer, nomer1,2)
                   nomer = nomer + 1
               elif message == 'e':
                   bot.main_function(id, event, nomer, nomer1, 3)
                   nomer = nomer + 1


               elif message == "q":
                   ###########################################
                    bot.main_function(id, event, nomer, nomer1,1)
                    nomer = nomer +1
####################################################################################################



               else:
                     bot.bot_write(event.user_id, "Не поняла вашего ответа... Нажмите 'q' для поиска пары")