import vk_api
import database

token = "vk1.a.07rHbbJwwXNuw6G57_fYTPztuM_YDYZAtkJGAUsJClesxa2CagyoMsU8ZSonIefjlQFFpT9nIGxxJQ9rm_TuPDiI3UbdVIY6Zq1TlYiwYCohnVURXXJ2Ul-DdlZSBqQFljPWyKjlZJTVm7C-su6fMPDmY_Ejo1SwUqHPrncH-iB9moew54Hz0WZxv_JtiPQO1pXEugC7qr2VeSdH60-iNQ"  # В ковычки вставляем аккуратно наш ранее взятый из группы токен.
token1 = "vk1.a.DORfAY-ITv15OOeopjNGLpGXe8b93O3NvCqWTKEIFez4emjJ_al1_H6w-HrvQAzVJCSzmpZ3M4_F0RdfR9P5jx6zZfqgIPilx2Fux9ovGOcoAx4osHv2oaxNXIWMmUHvBXkyE5srEhAWPQfCsSKTa2j8t5fS9uqy92fw8N3yjibjF9IIVmJiy5k9gafFI_pRY_0osB8e2wpRfRlOORxx6g"
# Подключаем токен и longpoll
vk = vk_api.VkApi(token=token)
vk1 = vk_api.VkApi(token=token1)
#give = vk.get_api()
#longpoll = VkLongPoll(vk)




# Создадим функцию для ответа на сообщения в лс группы
def bot_write(id, text):
    vk.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})

def bot_write_foto(id, text,url):
        vk.method('messages.send', {'user_id': id, 'message': text, "attachment": url, 'random_id': 0})


    #######################################

def photos_partner(id,nomer):
        partner_users = vk1.method("photos.get", {"owner_id": id,"rev": 0 ,"count": 3,"offset" : 0, "extended": 1, "album_id": "wall"})
        phot = partner_users["items"]
       #print(partner_users['count']) # количество фото
        return partner_users['count'], phot # кол-во фото и ссылка на фото

def user_data(id1):
    user = vk.method("users.get", {"user_ids": id1, 'fields': 'city,relation, sex,photo_50'})
    first_name_user = user[0]['first_name']  # имя пользователя


    last_name_user = user[0]['last_name']  # фамилия пользовател


    #date_of_birth = user[0]['bdate'] #    Дата рождения пользователя( часто не указана --- использовать не будем)
    # print(date_of_birth)
    #bot_write(id, "Введите год рождения")
    #wert = main.message
    #date_of_birth = int(wert)
    # print(date_of_birth)
    date_of_birth = 48 # КОСТЫЛЬ

    if (user[0]['sex'] == 2) :  # пол пользователя
        sex_user = 1
    elif (user[0]['sex'] == 1) :
        sex_user = 2
    else:
        bot_write(id, "Вы мужчина или женщина (2/1)?")

    city_user = user[0]['city']['title']  # город пользователя
    city_user_id = user[0]['city']['id']


    relation_user = user[0]['relation']  # семейное положение пользователя( избыточные данные)
    #rint(relation_user)

    photo_50_user = user[0]['photo_50']


    return first_name_user, last_name_user, date_of_birth, sex_user, city_user, relation_user, photo_50_user,city_user_id



def partner_search(id,city_user_id,date_of_birth,sex_user,nomer):           # поиск подходящих людей
    age_from = date_of_birth-5  # возростной диапазон
    age_to = date_of_birth+5
    user_partner = vk1.method("users.search", {'age_from': age_from, 'age_to':age_to , 'count': 1, 'city': city_user_id, 'offset': nomer})
    print(nomer)
    database.insert_users_partner(int(user_partner['items'][0]['id']), int(0))


def main_function(id,event, nomer, nomer1,status):
    try:
        qwert = user_data(id)
        partner_search(id, qwert[7], qwert[2], qwert[3], nomer)
        new_partners = database.select_users_partner(0)  ##########################################
        zzzz = photos_partner(new_partners[0][0], nomer)

        if int(zzzz[0]) >= 3:
            number_of_photo = 3
        else:
            number_of_photo = (int(zzzz[0]) - 1)

        qqqq = (user_data(new_partners[0][0]))

        bot_write(id, f"ЗНАКОМЬТЕСЬ:  {qqqq[0] + '    ' + qqqq[1]}")
        bot_write(event.user_id, f"ЛЕТ :   {qqqq[2]}")
        bot_write(event.user_id, f"Город :   {qqqq[4]}")
        bot_write(event.user_id, f" Семейное положение :   {qqqq[5]}")
        bot_write(id, f"Адрес страницы:  https://vk.com/id{new_partners[0][0]}")
        #bot_write(event.user_id, f" Пол:   {qqqq[3]}")

        for j in range(0, number_of_photo):
            zzzz = photos_partner(new_partners[0][0], j)
            bot_write_foto(id, f"ФОТО № {j + 1}", zzzz[1][j]['sizes'][3]['url'])  # цифра 3 это размер фото
        bot_write(event.user_id, "Продолжить : q    В черный список : w     В избранное : e ")
        nomer = nomer + 1
        zzzz = photos_partner(new_partners[0][0], 2)
        new_partners = database.select_users_partner(0)
        database.update_users_partner(new_partners[0][0], status)

        partner_search(id, qwert[7], qwert[2], qwert[3], nomer)
    except:
        database.update_users_partner(new_partners[0][0], 2)
        main_function(id, event, nomer + 1, nomer1,status)







