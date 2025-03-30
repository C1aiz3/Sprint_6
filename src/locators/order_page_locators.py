from selenium.webdriver.common.by import By

class OrderPageLocators:
    first_name = By.XPATH, '//div[@class="Order_Form__17u6u"]/div[1]/input'         #Поле "Имя"
    second_name = By.XPATH, '//div[@class="Order_Form__17u6u"]/div[2]/input'        #Поле "Фамилия"
    address_locator = By.XPATH, '//div[@class="Order_Form__17u6u"]/div[3]/input'    #Поле "Адрес"
    metro_station_field = By.XPATH, '//div[@class="select-search__value"]/input'    #Выпадающий список "Станция метро"
    metro_station_variant = By.XPATH, '//li[1]'                                     #Один из вариантов в выпадающем списке "станция метро"
    phone_number = By.XPATH, '//div[@class="Order_Form__17u6u"]/div[5]/input'       #Поле "Телефон"
    next_button = By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button'        #Кнопка "Далее"
    date = By.XPATH, '//div[@class="react-datepicker-wrapper"]//input'              #Поле "Когда привезти"
    rental_period = By.XPATH, '//div[@class="Dropdown-control"]'                    #Поле "Срок аренды"
    rent_variant1 = By.XPATH, '//div[@class="Dropdown-option"][1]'                  #"Срок аренды" : сутки
    rent_variant2 = By.XPATH, '//div[@class="Dropdown-option"][2]'                  #"Срок аренды" : двое суток
    black_color = By.XPATH, '//label[@for="black"]'                                 #"Цвет самоката" : черный жемчуг
    grey_color = By.XPATH, '//label[@for="grey"]'                                   #"Цвет самоката" : серая безысходность
    comment = By.XPATH, '//div[@class="Order_Form__17u6u"]/div/input'               #Поле "Комментарий"
    order_button = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[2]'       #Кнопка "Заказать"
    yes_button = By.XPATH, '//div[@class="Order_Modal__YZ-d3"]/div/button[2]'       #Кнопка "Да" на этапе согласия с заказом
    order_placed_window = By.XPATH, '//div[@class="Order_Modal__YZ-d3"]'            #Окно с информацией об оформленном заказе