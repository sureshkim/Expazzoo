#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .
from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

APP_ID = 27048557
API_HASH = "dbf9db84b9e32cbf6fd0f8e79ac27230"
SESSION = "1BVtsOHgBu1tUjoiG5p9av5paFHhY0YNS8YtVvybHUNmo7bmtSXyDWE8FJB14s5uaV16L4H1ee_Y8MDLeZW2UPYLiEsvlbL6DSTtfS8gbh_HyMBh4SjhDFuHkRjcPhIAPvmvwvb87CJ1zpGeF7HshtAIj-adK3sU_vhPa7-3enV_f6TKZlDi02oVMDEJsxVyjQKG-zhuyTff386J-YMJWnZLnqhk9l1SXxyIRUbOU2iCLd7s8LZ4gdtVL0aWQerVLfJS0HMNlmrok-RQUp2KkZWb6JVW96LVw2ziiD21yq71G4sWixCbWAnPnQoReL176F6jsKXNiJ4NfiNyTh0lVkaVip8KVaF8="
FROM_ = "-1001710117697"
TO_ = "-1001903674225"


FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    if event.message.video:  # Only forward if the message contains a video
        for i in TO:
            try:
                await BotzHubUser.send_message(
                    i,
                    event.message
                )
                print(f"Video forwarded from {event.chat_id} to {i}")
            except Exception as e:
                print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
    
