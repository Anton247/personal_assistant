
from settings import LOGIN, PASSWORD, TOKEN
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)

def send_sticker(id_user, id_sticker):
  vk_session.method("messages.sendSticker", {'peer_id':id_user, 'sticker_id':id_sticker, 'random_id':0})
#функция для ответа на сообщения в ЛС  
def write_msg(id, text):
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      if event.from_user:
        if event.to_me:
          if event.text == 'Картинка':
            vk_session.method('messages.send', {'peer_id': event.user_id,'attachment': "photo56419740_457251425", 'random_id': 0})
            vk_session.method('messages.send', {'peer_id': event.user_id,'attachment': "video4448869_161923713", 'random_id': 0})
          message = "Привет!\nЯ очень занят. Напиши мне позже"
          write_msg(event.user_id, message)
          send_sticker(event.user_id, 19584)