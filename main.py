import vk_api
from threading import Timer
from importlib import reload
import randomizerForFuncMesaga as zalupa
import time

personId = 290783919
    #419389340  #290783919

vk_seks = vk_api.VkApi(
    token='vk1.a.jJoBHYNKeYi0YmG8hMa8UciC4P0VFrQO260Orv62lOVRg_YvEoV4HJs-dETrXzvsN7Bj5YFgYE8mCAx_eVRvHubaN6B723f1BpWoWnvUDOezLYOMRgwZrPu4ctukn_p1DVxVUoVgmZxzgkOvXMGsb-JDGSBZkyz6nrgcB9RMmNLrNLB_HUV2H2ZNWD1xS9GY7VXUyr7xYwSVRbg_rt9aHw')
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




