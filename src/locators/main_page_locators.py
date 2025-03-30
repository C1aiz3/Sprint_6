from selenium.webdriver.common.by import By

class MainPageLocators:
    cookie_button = By.XPATH, '//button[@id="rcc-confirm-button"]'                          #Кнопка принятия куки
    first_question = By.XPATH, '//div[@class="accordion"]/div[1]'                           #Первый вопрос на главной странице
    second_question = By.XPATH, '//div[@class="accordion"]/div[2]'                          #Второй вопрос на главной странице
    third_question = By.XPATH, '//div[@class="accordion"]/div[3]'                           #Третий вопрос на главной странице
    fourth_question = By.XPATH, '//div[@id="accordion__heading-3"]'                         #Четвертый вопрос на главной странице
    fiveth_question = By.XPATH, '//div[@id="accordion__heading-4"]'                         #Пятый вопрос на главной странице
    sixth_question = By.XPATH, '//div[@id="accordion__heading-5"]'                          #Шестой вопрос на главной странице
    seventh_question = By.XPATH, '//div[@id="accordion__heading-6"]'                        #Седьмой вопрос на главной странице
    eighth_question = By.XPATH, '//div[@id="accordion__heading-7"]'                         #Восьмой вопрос на главной странице
    first_answer = By.XPATH, '//div[@class="accordion"]/div[1]//p'                          #Ответ на первый вопрос
    second_answer = By.XPATH, '//div[@class="accordion"]/div[2]//p'                         #Ответ на второй вопрос
    third_answer = By.XPATH, '//div[@class="accordion"]/div[3]//p'                          #Ответ на третий вопрос
    fourth_answer = By.XPATH, '//div[@class="accordion"]/div[4]//p'                         #Ответ на четвертый вопрос
    fiveth_answer = By.XPATH, '//div[@class="accordion"]/div[5]//p'                         #Ответ на пятый вопрос
    sixth_answer = By.XPATH, '//div[@class="accordion"]/div[6]//p'                          #Ответ на шестой вопрос
    seventh_answer = By.XPATH, '//div[@class="accordion"]/div[7]//p'                        #Ответ на седьмой вопрос
    eighth_answer = By.XPATH, '//div[@class="accordion"]/div[8]//p'                         #Ответ на восьмой вопрос
    top_order_button = By.XPATH, '//button[@class="Button_Button__ra12g"]'                  #Кнопка "Заказать" сверху
    bottom_order_button = By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button'       #Кнопка "Заказать" снизу
    dzen_button = By.XPATH, '//a[@target="_blank"]'                                         #Кнопка "Дзен"
    alert = By.XPATH, '//div[@class="kc00720f4"]'                                           #Поисковая строка на Дзене
    scooter_main_page_button = By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]'          #Кнопка "Самокат"



