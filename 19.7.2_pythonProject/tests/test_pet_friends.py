from api import PetFriends
from settings import valid_email, valid_password, not_valid_email, not_valid_password
import os

pf = PetFriends()


def test_get_api_key_for_user(email=valid_email, password=valid_password):
    """ Указываем валидные авторизационные данные,
    проверяем, что запрос api-ключа возвращает код ответа 200 и в результате имеется слово key"""

    # Отправляем запрос, сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем, что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api-ключ и сохраняем в переменную auth_key, затем, используя этот ключ,
    запрашиваем список всех питомцев и проверяем, что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Франклин', animal_type='кот',
                                     age='8', pet_photo='images/IMG_2116.jpg'):
    """Проверяем что можно добавить питомца с валидными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем api-ключ и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем, если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Franky", "cat", "9.5", "images/IMG_2132.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на его удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Снова запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем, что код ответа - 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Фрэнки', animal_type='Кот', age=9):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список питомцев не пустой, обновляем его имя, тип и возраст  первого питомца
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем, что код ответа - 200 и имя питомца соответствует введенному значению
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то удаляем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_get_all_pets_with_valid_key_wrong_filter(filter='my'):
    """ Проверяем, что при запросе всех питомцев в случае, если передать в значение фильтра
     недопустимый параметр, будет возращен статус код ошибки.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этот ключ,
    запрашиваем список всех питомцев  """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 500

def test_get_api_key_for_not_valid_user(email=not_valid_email, password=not_valid_password):
    """ Проверяем что запрос api-ключа для не зарегестрированного пользователя возвращает
    статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_add_new_pet_without_photo(name='Тузик', animal_type='кот',
                                     age='5'):
    """Проверяем, что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
def test_add_new_pet_without_photo_noncorrect(name='Тузик', animal_type='кот',
                                     age='Пять'):
    """Проверяем можно ли добавить питомца с некорректными данными"""

       # Запрашиваем api-ключ и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    result['age'] = age.isdigit()
    assert age.isdigit() == False
def test_add_new_pet_without_parrametrs(name='', animal_type='',
                                     age=''):
    """Проверяем, можно ли добавить питомца с пустыми параметрами"""

       # Запрашиваем api-ключ и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
def test_add_new_pet_with_large_parametr_name(name='вфаывыпрволываолрджоправожлдэлорпавыпролждэлокуешщгждюолбьтимьтбжгдшншеукуцкегшжлдюобпавпыаффывапролждэжшгенекуецкушщгжолдрпавыавфвапролднгнеекушгдплрптавыафвпролднекуецкеншгдлропавыафвфапролдрпавапвралдпоавыфывапрдлорпоавпыафываролдрлпоавпыапрооапрпопавпа'
                                     , animal_type='',age=''):
    """Проверяем можно ли добавить питомца c большим значением в параметре name"""

       # Запрашиваем api-ключ и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
def test_add_new_pet_with_large_parametr_type(name=''
                                     , animal_type='вфаывыпрволываолрджоправожлдэлорпавыпролждэлокуешщгждюолбьтимьтбжгдшншеукуцкегшжлдюобпавпыаффывапролждэжшгенекуецкушщгжолдрпавыавфвапролднгнеекушгдплрптавыафвпролднекуецкеншгдлропавыафвфапролдрпавапвралдпоавыфывапрдлорпоавпыафываролдрлпоавпыапрооапрпопавпа'
                                     ,age=''):
    """Проверяем можно ли добавить питомца c большим значением в параметре animal_type"""

       # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
def test_add_new_pet_with_large_parametr_age(name=''
                                     , animal_type=''
                                     ,age='вфаывыпрволываолрджоправожлдэлорпавыпролждэлокуешщгждюолбьтимьтбжгдшншеукуцкегшжлдюобпавпыаффывапролждэжшгенекуецкушщгжолдрпавыавфвапролднгнеекушгдплрптавыафвпролднекуецкеншгдлропавыафвфапролдрпавапвралдпоавыфывапрдлорпоавпыафываролдрлпоавпыапрооапрпопавпа'):
    """Проверяем можно ли добавить питомца c большим значением в параметре age"""

       # Запрашиваем api-ключ и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    result['age'] = age.isdigit()
    assert age.isdigit() == True