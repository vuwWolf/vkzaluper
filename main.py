import vk_api
from threading import Timer
from importlib import reload
import randomizerForFuncMesaga as zalupa
import time

personId = None #Вместо None айди в ВК жертвы

Token = 'ХУЙ'
#Вписывай токен того аккаунта ВК, с которого будет производиться заебатинг

vk_seks = vk_api.VkApi(
    token=Token
vk = vk_seks.get_api()

def checkOnline():
    information = vk.users.get(user_id=personId, fields='online')
    online = information[0]['online']
    return online

huita = checkOnline()

def mesaga():
    message = zalupa.pizdecToString
    vk.messages.send(user_id=personId, message= message, random_id=0)
    time.sleep(5)
def ebalka():
    while True:
        try:
            if huita == 1:
                print('Цель в сети. Начинаем доёб')
                checkOnline()
                while huita == 1:
                    mesaga()
                    reload(zalupa)

            else:
                print('Цель не в сети. Ожидаем актива')
        except ValueError:
            print('zalupaFM')

ebalka()




