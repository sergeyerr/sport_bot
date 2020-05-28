from frontend.setup import frontend


# Функция должна возвращать ID (!) изображения,
# желательно аватар пользователя.
# Для этого понадобиться прочитать документацию,
# подумать, как раскопать file_id аватара пользователя.
# UPD. Раскопали, возвращает ID аватара нынешнего юзера, если он есть, иначе - знак вопроса из картинок в ресурсах

def get_user_picture(bot, message):

    chat_id = message.chat.id #берется айдишник нынешнего чата

    try: #смотрим случай, когда есть аватарка
        pictureMas = bot.get_user_profile_photos(chat_id, limit=1).photos[0] #запрашиваются первое фото из тех, какие есть у юзера
        file_id = pictureMas[-1].file_id #берем айдишник получившегося фото
    except IndexError: #случай, когда нет аватарки (мб выдавать месс, мол, поставьте аву, пж?)
        file_id = open("../resources/images/noavatar.png", 'rb') # #пока будем выдавать знак вопроса с локалки
    return file_id
