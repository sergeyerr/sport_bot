"""
    Графический компонент, который представляет пользователю
    мероприятия с возможностью записаться на них.
"""

from frontend.setup import frontend

# Запись на мероприятие должна добавлять соответствующую запись
# в таблицу activities.

activity = {
    "name": "Поездка на 68 автобусе",
    # Остальные поля из прототипа интерфеса в Figma
    # надо взять.
}


def create_message():
    """
        Возвращает разметку компонента и
        текст сообщения, в котором разметка будет расположена.

        Возвращаемые значения
        ---------------------
        пара: (message_text, message_markup)
    """

    # Замените pass на Ваш код.
    pass


@frontend.callback_query_handler(
    lambda call: call.data.startswith("activity_viewer_viewer_cancel"))
def activities_near_button_pressed(call):
    # Этот обработчик реализовывать не нужно
    # Данный вызов должен быть в конце каждого обработчика.
    frontend.answer_callback_query(call.id)
