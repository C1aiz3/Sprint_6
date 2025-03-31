import pytest
import allure
from src.data import QUESTIONS_ANSWERS
from src.pages.main_page import MainPage



class TestQuestionsText:


    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", QUESTIONS_ANSWERS)
    def test_questions_text(self, driver, question_locator, answer_locator, expected_answer):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url()
        scooter_main_page.accept_cookies()

        with allure.step(f'Check question answer text'):

            scooter_main_page.click_element(question_locator)
            assert scooter_main_page.find_element(answer_locator).text == expected_answer
