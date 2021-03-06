from frontend.setup import frontend
import urllib
import os

def user_picture(user_id):
    # Смотрим случай, когда есть аватарка
    try:
        # Запрашиваются первое фото из тех, какие есть у юзера
        pictureMas = frontend.get_user_profile_photos(
            user_id, limit=1).photos[0]
        # Берем айдишник получившегося фото
        file_id = pictureMas[-1].file_id
    # Случай, когда нет аватарки (мб выдавать месс, мол, поставьте аву, пж?)
    except Exception:
        if not os.path.isfile('out.jpg'):
            url = 'https://i.ibb.co/m5NDJqv/noavatar.jpg'
            f = open('out.jpg', 'wb')
            f.write(urllib.request.urlopen(url).read())
        file_id = open('out.jpg', 'rb')
    return file_id
