# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random
import requests
import traceback
from photo import photokek, invert, make_3d, glitch_this_run, based
import os
from work_with_database import insert_information_to_database
import sqlite3
import datetime
import lyricsgenius
import datetime

vk_session = vk_api.VkApi(token='credentials')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 'credentials')

sphere = ["возможно", 'лол, нет', 'ахах, даже не надейся, лошара', 'конечно, бро', '100 проц', 'хз']
owner_id = 318741811

genius = lyricsgenius.Genius("cPUR_aPri8bOEi4gw_9W54BA_x5lh10b7_CbbSA_n1pLYSyJ8T91WQv0YEQuIkgK", skip_non_songs=True,
                             remove_section_headers=True)

ban = ['жижа', 'жижка', ]

con = sqlite3.connect('nicknames.db')
cur = con.cursor()

def send_message(chat_id, message):
    vk.messages.send(random_id=get_random_id(),
                     peer_id=chat_id,
                     message=message)


def check_ban(chat_id, message: str, username):
    dictionary_ban = {'кира', 'ппп', 'рерол', "реролл", "рол", "ролл",
                      'рероллить', "реролить", "фигурк", "инвалид", "тикет", "гарант", "хаято", "гаш", 'погги', 'жижа',
                      'жижк', "жож", 'галочкин', "выпал", "качка"}
    prepared = message.lower()
    for word in dictionary_ban:
        if word in prepared:
            send_message(chat_id, f'{username}, WOW! ЖИЖКА МОМЕНТ! WOW!')
            send_message(chat_id, f'{username}, сори я ненавижу джоджо и ппп')
            break
def tyanki(chat_id, username):
    num = str(random.randint(1, 192))
    random_url = num + '.jpg'
    random_url = '/usr/local/bin/evabot/tyanki/' + random_url
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(random_url)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f"photo{owner_id}_{photo_id}_{access_key}"

    vk.messages.send(peer_id=chat_id, random_id=get_random_id(),
                     message=f'{username}, руки на стол!',
                     attachment=attachment)


def kick(chat_id, username, kick_command, sex_id):
    try:
        urls = ['kick1', 'kick2', 'kick3', 'kick4', 'kick5', 'kick6', 'kick7']
        random_url = random.choice(urls) + '.jpg'
        random_url = '/usr/local/bin/evabot/kicks/' + random_url
        upload = vk_api.VkUpload(vk)
        photo = upload.photo_messages(random_url)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f"photo{owner_id}_{photo_id}_{access_key}"
        kick_command = kick_command.split(' ')
        kick_command.pop(0)
        if 'тест' in kick_command:
            kick_command.remove('тест')
        kick_command = ' '.join(kick_command)
        if sex_id == 1:
            postfix = 'а'
        else:
            postfix = ''
        if ':' in kick_command:
            kick_command = kick_command.split(':')
            name = kick_command[0]
            with_words = kick_command[1]
            vk.messages.send(peer_id=chat_id, random_id=get_random_id(),
                             message=f'{username} ударил{postfix} {name} со словами: "{with_words}" &#128074;',
                             attachment=attachment)
        else:
            name = kick_command
            vk.messages.send(peer_id=chat_id, random_id=get_random_id(),
                             message=f'{username} ударил{postfix} {name} &#128074;',
                             attachment=attachment)
    except Exception:
        send_message(chat_id, 'Ошибка. Запишите команду, как на примере: "Ева ударить Обама" или '
                              '"Ева ударить Обама: получай!"')


def send_kek(chat_id, username):
    url1 = 'photo1.jpg'
    url2 = 'photo2.jpg'

    upload = vk_api.VkUpload(vk)
    photo1 = upload.photo_messages(url1)
    photo2 = upload.photo_messages(url2)

    owner_id = photo1[0]['owner_id']
    photo_id = photo1[0]['id']
    access_key = photo1[0]['access_key']

    attachment1 = f'photo{owner_id}_{photo_id}_{access_key}'

    owner_id = photo2[0]['owner_id']
    photo_id = photo2[0]['id']
    access_key = photo2[0]['access_key']

    attachment2 = f'photo{owner_id}_{photo_id}_{access_key}'

    vk.messages.send(peer_id=chat_id, random_id=get_random_id(),
                     message=f'{username}, держи',
                     attachment=[attachment1, attachment2])
    os.remove('photo1.jpg')
    os.remove('photo2.jpg')


def send_invert(chat_id, username):
    url_inverted = 'imginverted.jpg'
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(url_inverted)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    vk.messages.send(peer_id=chat_id, random_id=get_random_id(),
                     message=f'{username}, держи',
                     attachment=attachment)
    os.remove('imginverted.jpg')


def send_3d(chat_id, username):
    url_3d = 'imgres3d.jpg'
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(url_3d)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    vk.messages.send(peer_id=chat_id, random_id=get_random_id(),
                     message=f'{username}, держи',
                     attachment=attachment)
    os.remove('imgres3d.jpg')


def check_nickname(user_id):
    db = sqlite3.connect('nicknames.db')
    sql = db.cursor()
    sql.execute("SELECT user_id FROM nicknames")
    nicknames = sql.fetchall()
    if (user_id,) not in nicknames:
        return vk.users.get(user_ids=event.object["from_id"])[0]['first_name']
    else:
        sql.execute(f"SELECT nickname FROM nicknames WHERE user_id = {user_id}")
        nickname_db = sql.fetchall()[0][0]
        db.commit()
        return nickname_db


# def check_allowed_commands(chat_id):
#     db = sqlite3.connect('commands_database.db')
#     sql = db.cursor()
#     sql.execute("SELECT chat_id FROM commands_database")
#     allowed = sql.fetchall()
#     if (chat_id,) in allowed:
#         sql.execute(f"SELECT autokick FROM commands_database WHERE chat_id = {chat_id}")
#         boolean = sql.fetchall()[0][0]
#         if boolean == 1:
#             return True
#     return False


def send_list(chat_id, list_message, k=5):
    def lambda_list(x):
        return x['first_name'] + " " + x['last_name']

    users_send = []
    dictionary_with_user_data_send = vk.messages.getConversationMembers(peer_id=id_chat)
    for user_send in dictionary_with_user_data_send['items']:
        if str(user_send['member_id'])[0] != '-':
            users_send.append(int(user_send['member_id']))
    n = len(users_send)
    if n < k:
        k = n
    if k > 20:
        k = 20
    chose = random.sample(users_send, k)
    final_string = ''
    user_got = vk.users.get(user_ids=chose)
    names = list(map(lambda_list, user_got))
    i = 0
    for x in names:
        i += 1
        final_string += str(i) + ") " + x + '\n'
    send_message(chat_id, f'Список {list_message}:\n{final_string}')


def send_glitch(id_chat, username):
    url_glitch = 'glitched_glitch.jpg'
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(url_glitch)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    vk.messages.send(peer_id=id_chat, random_id=get_random_id(),
                     message=f'{username}, держи',
                     attachment=attachment)
    os.remove('glitched_glitch.jpg')


def send_based(id_chat, username):
    url_based = 'imgbaseded.jpg'
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(url_based)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    vk.messages.send(peer_id=id_chat, random_id=get_random_id(),
                     message=f'{username}, ответ базы:',
                     attachment=attachment)
    os.remove('imgbaseded.jpg')


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW or event.type == VkEventType.MESSAGE_NEW:
                message = event.object["text"]
                conversation_flag = False
                if event.type == VkBotEventType.MESSAGE_NEW:
                    conversation_flag = True
                sender_id = event.object['from_id']
                username = check_nickname(sender_id)
                check_ban(event.chat_id + 2000000000, message, username)
                if message.split(' ')[0].lower() == "ева" or message.split(' ')[0].lower() == "евочка" or \
                        message.split(' ')[0].lower() == "ева,":
                    time_start = datetime.datetime.now()
                    sender_id = event.object['from_id']
                    username = check_nickname(sender_id)
                    id_chat = event.chat_id
                    if id_chat is None:
                        id_chat = event.object.peer_id
                    else:
                        id_chat += 2000000000
                    command = message.split(' ')
                    command.pop(0)
                    if command:
                        first_command = command[0].lower()
                    else:
                        break
                    command = ' '.join(command)
                    command_lower = command.lower()
                    if 'привет' in first_command:
                        send_message(id_chat,
                                     f'{username}, приветики!!!')
                    elif 'сап' in first_command:
                        send_message(id_chat,
                                     f'{username}, сап, омежка :3')
                    elif 'салам' in first_command or 'салам алейкум' in first_command:
                        send_message(id_chat,
                                     f'{username}, алейкум асалам,'
                                     f' брат')
                    elif "шар" in first_command:
                        send_message(id_chat,
                                     f'{username}, {random.choice(sphere)}')
                    elif 'тянка' in command_lower or 'тяночка' in first_command or 'тян' in first_command:
                        tyanki(id_chat, username)
                    elif 'ударить' in first_command and conversation_flag:
                        sex = vk.users.get(user_ids=sender_id, fields='sex')[0]['sex']
                        kick(id_chat, username, command, sex)
                    elif 'выбери' in first_command:
                        if ' или ' in command_lower:
                            command_choose = command_lower.split(' ')
                            index = command_choose.index('выбери')
                            command_choose = ' '.join(command_choose[index + 1:]).split(' или ')
                            result = random.choice(command_choose)
                            send_message(id_chat, f'{username}, я думаю, что "{result}"')
                        else:
                            send_message(id_chat, f'{username}, а где "или" ёпта?')
                    elif 'ник' in first_command:
                        nickname = command.split(' ')
                        nickname.pop(0)
                        if 'тест' in nickname:
                            nickname.remove('тест')
                        nickname = ' '.join(nickname)
                        if 2 <= len(nickname) < 50:
                            insert_information_to_database(sender_id, nickname)
                            send_message(id_chat, 'Ник установлен!')
                        else:
                            send_message(id_chat, 'Слишком много символов! (максимум 20, минимум 2)')
                    elif 'кто' in first_command and conversation_flag:
                        users = []
                        dictionary_with_user_data = vk.messages.getConversationMembers(peer_id=id_chat)
                        for user in dictionary_with_user_data['items']:
                            if str(user['member_id'])[0] != '-':
                                users.append(int(user['member_id']))
                        random_user = random.choice(users)
                        user_get = vk.users.get(user_ids=(random_user))
                        user_get = user_get[0]
                        first_name = user_get['first_name']
                        last_name = user_get['last_name']
                        full_name = first_name + " " + last_name
                        send_message(id_chat, f'Уверена, что это {full_name}')
                    elif 'список' in first_command and conversation_flag:
                        command_list = command.split(' ')
                        command_list.pop(0)
                        if 'тест' in command_list:
                            command_list.remove('тест')
                        try:
                            count = int(command_list[0])
                            command_list.pop(0)
                            message_list = ' '.join(command_list)
                            send_list(id_chat, message_list, count)
                        except Exception:
                            message_list = ' '.join(command_list)
                            send_list(id_chat, message_list)
                    elif 'фото кек' in command_lower:
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            photokek(url)
                            send_kek(id_chat, username)
                        except BaseException:
                            send_message(id_chat, f'{username}, а где картинка ёпта?')
                    elif 'фото негатив' in command_lower:
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            invert(url)
                            send_invert(id_chat, username)
                        except Exception:
                            send_message(id_chat, f'{username}, а где картинка?')
                    elif 'фото 3д' in command_lower:
                        command_3d = command.split(' ')
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            make_3d(url)
                            send_3d(id_chat, username)
                        except Exception:
                            send_message(id_chat, f'{username}, а где картинка?')
                    elif 'ты меня любишь' in command or 'ты меня не любишь' in command:
                        if sender_id == owner_id:
                            send_message(id_chat, f'Конечно, любимый &#128150; &#128150; &#128150;')
                        else:
                            send_message(id_chat, f'НЕТ, я люблю только моего *id318741811 (создателя)!')
                    elif 'фото глитч' in command_lower:
                        command_glitch = command_lower.split(' ')
                        if 'тест' in command_glitch:
                            command_glitch.remove('тест')
                        try:
                            num = float(command_glitch[-1])
                        except Exception:
                            send_message(id_chat, 'Укажите параметр для фото глитч от 1 до 8')
                            break
                        if num > 10 or num < 0.1:
                            break
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            glitch_this_run(url, num, color='-c')
                            send_glitch(id_chat, username)
                        except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())
                            send_message(id_chat, f'{username}, а где картинка?')
                    elif 'фото разлом' in command_lower:
                        command_glitch = command_lower.split(' ')
                        if 'тест' in command_glitch:
                            command_glitch.remove('тест')
                        try:
                            num = float(command_glitch[-1])
                        except Exception:
                            send_message(id_chat, 'Укажите параметр для фото разлом от 1 до 8')
                            break
                        if num > 10 or num < 0.1:
                            break
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            glitch_this_run(url, num)
                            send_glitch(id_chat, username)
                        except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())
                            send_message(id_chat, f'{username}, а где картинка?')
                    elif 'фото полосочки' in command_lower:
                        command_glitch = command_lower.split(' ')
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            num = 1
                            glitch_this_run(url, num, lines='-s')
                            send_glitch(id_chat, username)
                        except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())
                            send_message(id_chat, f'{username}, а где картинка?')
                    elif 'база' in first_command:
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            based(url)
                            send_based(id_chat, username)
                        except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())
                            send_message(id_chat, f'{username}, а где картинка?')
                    elif 'шабат' in command_lower or 'шаббат' in command_lower:
                        time = datetime.datetime.now().weekday()
                        delta = 5 - time
                        if delta < 0:
                            delta += 7
                        if delta != 0:
                            send_message(id_chat, f'{username}, до шаббата {delta} дней!')
                        else:
                            url = '/usr/local/bin/evabot/tyanki/shabat.jpg'
                            upload = vk_api.VkUpload(vk)
                            photo = upload.photo_messages(url)
                            owner_id = photo[0]['owner_id']
                            photo_id = photo[0]['id']
                            access_key = photo[0]['access_key']
                            attachment = f"photo{owner_id}_{photo_id}_{access_key}"
                            vk.messages.send(peer_id=id_chat, random_id=get_random_id(),
                                             message=f'{username}, шаббат шалом!',
                                             attachment=attachment)
                    elif 'текст' in first_command:
                        command_lyrics = command_lower.split(' ')
                        command_lyrics.pop(0)
                        if '-' in command_lyrics:
                            command_lyrics = ' '.join(command_lyrics)
                            command_lyrics = command_lyrics.split(' - ')
                            song_genius = genius.search_song(command_lyrics[1], command_lyrics[0])
                            command = command.split(' ')
                            command.pop(0)
                            name = ' '.join(command)
                            try:
                                info = (song_genius.lyrics[:1990] + '..') if len(
                                    song_genius.lyrics) > 1970 else song_genius.lyrics
                                if song_genius.album:
                                    send_message(id_chat, f"{name}\n"
                                                          f"Альбом: {song_genius.album}\n"
                                                          f"Текст:\n{info}\n"
                                                          f"Link: {song_genius.url}")
                                else:
                                    send_message(id_chat, f"{name}\n"
                                                          f"Текст:\n{info}")
                            except AttributeError:
                                send_message(id_chat, 'не могу найти, извини')
                        else:
                            send_message(id_chat, 'формат: артист - песня')

                    # elif 'автокик' == first_command:
                    #     if 'автокик вкл' in command_lower:
                    #         check_power_on_commands_in_chat(event.chat_id, True)
                    #         send_message(id_chat, 'автокик включен')
                    #     elif 'автокик выкл' in command_lower:
                    #         check_power_on_commands_in_chat(event.chat_id, False)
                    #         send_message(id_chat, 'автокик выключен')

                    time_finish = datetime.datetime.now()
                    time_delta = str(time_finish - time_start).split(':')[2]
                    if ' тест' in command_lower:
                        send_message(id_chat, "время ответа сервера вк: " + str(os.system('ping -c 1 -t 4 vk.com')))
                        send_message(id_chat, f'Задача выполнялась: {time_delta} секунд')
            # elif event.object['action']['type'] == 'chat_kick_user'\
            #         and event.object['action']['member_id'] == event.object["from_id"]:
            #     print(1)
            #     user_leaved = event.object["from_id"]
            #     id_chat = event.chat_id
            #     if check_allowed_commands(id_chat):
            #         try:
            #             vk.messages.removeChatUser(chat_id=id_chat, user_id=event.object["from_id"])
            #         except Exception as e:
            #             print('Ошибка:\n', traceback.format_exc())



    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
