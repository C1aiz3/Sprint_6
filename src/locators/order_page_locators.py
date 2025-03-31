from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME = By.XPATH, '//div[@class="Order_Form__17u6u"]/div[1]/input'         #Поле "Имя"
    SECOND_NAME = By.XPATH, '//div[@class="Order_Form__17u6u"]/div[2]/input'        #Поле "Фамилия"
    ADDRESS_LOCATOR = By.XPATH, '//div[@class="Order_Form__17u6u"]/div[3]/input'    #Поле "Адрес"
    METRO_STATION_FIELD = By.XPATH, '//div[@class="select-search__value"]/input'    #Выпадающий список "Станция метро"
    METRO_STATION_VARIANT = By.XPATH, '//li[1]'                                     #Один из вариантов в выпадающем списке "станция метро"
    PHONE_NUMBER = By.XPATH, '//div[@class="Order_Form__17u6u"]/div[5]/input'       #Поле "Телефон"
    NEXT_BUTTON = By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button'        #Кнопка "Далее"
    DATE = By.XPATH, '//div[@class="react-datepicker-wrapper"]//input'              #Поле "Когда привезти"
    RENTAL_PERIOD = By.XPATH, '//div[@class="Dropdown-control"]'                    #Поле "Срок аренды"
    RENT_VARIANT1 = By.XPATH, '//div[@class="Dropdown-option"][1]'                  #"Срок аренды" : сутки
    RENT_VARIANT2 = By.XPATH, '//div[@class="Dropdown-option"][2]'                  #"Срок аренды" : двое суток
    BLACK_COLOR = By.XPATH, '//label[@for="black"]'                                 #"Цвет самоката" : черный жемчуг
    GREY_COLOR = By.XPATH, '//label[@for="grey"]'                                   #"Цвет самоката" : серая безысходность
    COMMENT = By.XPATH, '//div[@class="Order_Form__17u6u"]/div/input'               #Поле "Комментарий"
    ORDER_BUTTON = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[2]'       #Кнопка "Заказать"
    YES_BUTTON = By.XPATH, '//div[@class="Order_Modal__YZ-d3"]/div/button[2]'       #Кнопка "Да" на этапе согласия с заказом
    ORDER_PLACED_WINDOW = By.XPATH, '//div[@class="Order_Modal__YZ-d3"]'            #Окно с информацией об оформленном заказе