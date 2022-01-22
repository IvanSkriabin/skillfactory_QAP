from basic import WebPage
from elements import WebElement, ManyWebElements
import os

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru/'

        super().__init__(web_driver, url)
    # Находим локаторы элементов:
    h1 = WebElement(xpath='//h1')

    h2 = WebElement(xpath='//h2')

    first_element_in_location = WebElement(xpath="//ul[@class='a6']/li[1]")

    location = WebElement(xpath="//button[@class='_1-6r']")
    # Проверка возможности изменить регион:
    location_input = WebElement(xpath="//input[@class='_16XE _2HHF']")
    # Проверка ссылки на страницу TOP Fashion:
    top_fashion = WebElement(xpath="//ul[@class='c6c9']/li[1]")
    # Проверка ссылки на страницу Premium:
    premium = WebElement(xpath="//ul[@class='c6c9']/li[2]")
    # Проверка ссылки на страницу Ozon Счёт:
    ozon_card = WebElement(xpath="//ul[@class='c6c9']/li[3]")
    # Проверка ссылки на страницу Live:
    live = WebElement(xpath='//a[@href="/live/"]')
    # Проверка ссылки на страницу Sale:
    sale = WebElement(xpath='//a[@href="/info/actions/"]')
    # Проверка ссылки на страницу Бренды:
    brands = WebElement(xpath='//a[@href="/brand/"]')
    # Проверка ссылки на страницу Магазины:
    seller = WebElement(xpath="//a[@href='/seller/']")

    certificates_menu = WebElement(xpath='//a[@href="/context/detail/id/135382627/?perehod=menu"]')
    # Проверка ссылки на страницу Электроника:
    electronics = WebElement(xpath="//ul[@class='c6c9']/li[9]")
    # Проверка ссылки на страницу Одежда и обувь:
    main_apparel = WebElement(xpath='//a[@href="/info/main-apparel/"]')
    # Проверка ссылки на страницу Детские товары:
    for_kids = WebElement(xpath="//ul[@class='c6c9']/li[11]")
    # Проверка ссылки на страницу Дом и сад:
    garden = WebElement(xpath="//ul[@class='c6c9']/li[12]")
    # Проверка ссылки на страницу Ozon-бизнес:
    business = WebElement(xpath='//a[@href="/business/?perehod=header"]')
    # Проверка ссылки на страницу Мобильное приложение:
    appspromo = WebElement(xpath='//a[@href="/info/appspromo/"]')
    # Проверка ссылки на страницу Реферальная программа:
    referral = WebElement(xpath='//a[@href="/referral/?perehod=header"]')
    # Проверка ссылки на страницу Зарабатывай с Ozon:
    make_money_with_us = WebElement(xpath='//a[@href="//business.ozon.ru/?perehod=header"]')
    # Проверка ссылки на страницу Подарочные сертификаты:
    certificates_header = WebElement(xpath='//a[@href="/context/detail/id/135382627/?perehod=header"]')
    # Проверка ссылки на страницу Пункты выдачи:
    desks_map = WebElement(xpath='//a[@href="/info/map/"]')
    # Проверка ссылки на страницу Постаматы:
    postamat = WebElement(xpath='//a[@href="/postamat/"]')
    # Проверка ссылки на страницу Помощь:
    help = WebElement(xpath='//a[@href="//docs.ozon.ru/common/"]')
    # Проверка ссылки на Стоимость доставки:
    free_delivery = WebElement(xpath='//a[@href="/my/deliveryPriceInfo"]')
    # Проверка элемента Ozon travel:
    ozon_travel = WebElement(xpath="//ul[@class='c6c9']/li[13]")

    discount = WebElement(xpath="//ul[@class='c6c9']/li[14]")
    # Проверка ссылки на страницу Заказы:
    order_list = WebElement(xpath='//div[@url="/my/orderlist"]')
    # Проверка ссылки на страницу Избранное:
    favorites = WebElement(xpath='//a[@href="/my/favorites"]')
    # Проверка ссылки на страницу Корзина:
    cart = WebElement(xpath='//a[@href="/cart/"]')
    # Проверка кнопки Каталог:
    catalog_btn = WebElement(xpath='//div[@data-widget="catalogMenu"]')

    catalog_smartphones = WebElement(xpath='//a[@href="/category/smartfony-15502/"]')
    # Проверка поля поиска:
    search_input = WebElement(xpath='//form[@action="/search"]/div[2]/input')
    # Проверка кнопки поиска:
    search_btn = WebElement(xpath='//form[@action="/search"]/button')

    sort = WebElement(xpath='/html/body/div[1]/div/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]/div/div/div/div[1]/div[1]')
    # Проверка поиска и сортировки по цене по возрастанию:
    sort_by_price_low_to_high = WebElement(xpath='//div[@role="option"][3]')
    # Проверка поиска и сортировки по цене по убыванию:
    sort_by_price_high_to_low = WebElement(xpath='//div[@role="option"][4]')
    # Поиск и сортировка по новизне:
    sort_by_new = WebElement(xpath='//div[@role="option"][2]')
    # Проверка поиска и сортировки по рейтингу:
    sort_by_popular = WebElement(xpath='//div[@role="option"][1]')
    # Проверка поиска и сортировки по размеру скидки:
    sort_by_discount = WebElement(xpath='//div[@role="option"][5]')
    # Проверка поиска и сортировки по рейтингу:
    sort_by_rating = WebElement(xpath='//div[@role="option"][6]')

    products_prices = ManyWebElements(xpath='//div[@class="b5v4 a5d2 item a1d1"]//span')

    products = ManyWebElements(xpath='//div[@class="a0c4"]')

    products_discounts = ManyWebElements(xpath='//div[@class="b0e6 b0e7 a5d2 item a1d1"]//span')

    products_titles = ManyWebElements(xpath='//a[@class="tile-hover-target b3u9"]/span/span')

    search_not_found = WebElement(xpath='//div[@class="b6q3"]')

    first_line_footer = ManyWebElements(xpath='//footer/div/div/div/a[1]')

    second_line_footer = ManyWebElements(xpath='//footer/div/div/div/a[2]')

    third_line_footer = ManyWebElements(xpath='//footer/div/div/div/a[3]')

    forth_line_footer = ManyWebElements(xpath='//footer/div/div/div/a[4]')
    # Проверка ссылки на страницу Откройте пункт выдачи Ozon:
    ozon_business_partner_footer = WebElement(xpath='//footer/div/div/div/a[@href="https://business.ozon.ru/partners?perehod=footer"]')
    # Проверка ссылки на страницу Стать Поставщиком Ozon:
    ozon_business_footer = WebElement(xpath='//footer/div/div/div/a[@href="https://business.ozon.ru/?perehod=footer"]')
    # Проверка ссылки на страницу Что продавать на Ozon:
    what_to_sell_footer = WebElement(xpath='//footer/div/div/div/a[@href="https://seller.ozon.ru/what_to_sell/?perehod=footer"]')
    # Проверка ссылки на страницу Ecommerce Online School:
    ecomschool_footer = WebElement(xpath='//footer/div/div/div/a[@href="https://www.ozon.ru/info/ecomschool"]')
    # Проверка ссылки на страницу Ozon в ВКонтакте:
    vk_footer = WebElement(xpath='//footer/div[1]/div/div[5]/div[2]/a[@href="https://vk.com/ozon"]')
    # Проверка ссылки на страницу Ozon в Facebook:
    facebook_footer = WebElement(xpath='//footer/div[1]/div/div[5]/div[2]/a[@href="https://www.facebook.com/ozon.ru"]')
    # Социальные сети:
    social_networks_footer = ManyWebElements(xpath='//footer/div[1]/div/div[5]/div[2]/a')