from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = By.XPATH, '//button[@id="rcc-confirm-button"]'                          #Кнопка принятия куки
    FIRST_QUESTION = By.XPATH, '//div[@class="accordion"]/div[1]'                           #Первый вопрос на главной странице
    SECOND_QUESTION = By.XPATH, '//div[@class="accordion"]/div[2]'                          #Второй вопрос на главной странице
    THIRD_QUESTION = By.XPATH, '//div[@class="accordion"]/div[3]'                           #Третий вопрос на главной странице
    FOURTH_QUESTION = By.XPATH, '//div[@id="accordion__heading-3"]'                         #Четвертый вопрос на главной странице
    FIVETH_QUESTION = By.XPATH, '//div[@id="accordion__heading-4"]'                         #Пятый вопрос на главной странице
    SIXTH_QUESTION = By.XPATH, '//div[@id="accordion__heading-5"]'                          #Шестой вопрос на главной странице
    SEVENTH_QUESTION = By.XPATH, '//div[@id="accordion__heading-6"]'                        #Седьмой вопрос на главной странице
    EIGHTH_QUESTION = By.XPATH, '//div[@id="accordion__heading-7"]'                         #Восьмой вопрос на главной странице
    FIRST_ANSWER = By.XPATH, '//div[@class="accordion"]/div[1]//p'                          #Ответ на первый вопрос
    SECOND_ANSWER = By.XPATH, '//div[@class="accordion"]/div[2]//p'                         #Ответ на второй вопрос
    THIRD_ANSWER = By.XPATH, '//div[@class="accordion"]/div[3]//p'                          #Ответ на третий вопрос
    FOURTH_ANSWER = By.XPATH, '//div[@class="accordion"]/div[4]//p'                         #Ответ на четвертый вопрос
    FIVETH_ANSWER = By.XPATH, '//div[@class="accordion"]/div[5]//p'                         #Ответ на пятый вопрос
    SIXTH_ANSWER = By.XPATH, '//div[@class="accordion"]/div[6]//p'                          #Ответ на шестой вопрос
    SEVENTH_ANSWER = By.XPATH, '//div[@class="accordion"]/div[7]//p'                        #Ответ на седьмой вопрос
    EIGHTH_ANSWER = By.XPATH, '//div[@class="accordion"]/div[8]//p'                         #Ответ на восьмой вопрос
    TOP_ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g"]'                  #Кнопка "Заказать" сверху
    BOTTOM_ORDER_BUTTON = By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button'       #Кнопка "Заказать" снизу
    DZEN_BUTTON = By.XPATH, '//a[@target="_blank"]'                                         #Кнопка "Дзен"
    SCOOTER_MAIN_PAGE_BUTTON = By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]'          #Кнопка "Самокат"



