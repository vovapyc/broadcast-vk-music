# coding: utf-8

import config
import vk
import time

session = vk.AuthSession(scope='status',
                         access_token=config.ACCESS_TOKEN)
vkapi = vk.API(session)

print("Run")

def set_broadcast(audio, minutes):
    vkapi.audio.setBroadcast(audio=audio)
    time.sleep(minutes * 60)

while True:
    set_broadcast(config.AUDIO, 2)
