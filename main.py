
from settings import LOGIN, PASSWORD, TOKEN
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)

#функция для ответа на сообщения в ЛС группы
def write_msg(id, text):
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
             if event.to_me:
                if event.text == "Привет":
                  write_msg(event.user_id, "и тебе привет")
                elif event.text == "как дела?":
                    write_msg(event.user_id, "норм")