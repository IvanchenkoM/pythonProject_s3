import time
from testpage import OperationsHelper
import logging
import yaml

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


"""def test_step_1(brows):
    logging.info("Test1 starting")
    test_page = OperationsHelper(brows)
    test_page.go_to_site()
    test_page.enter_login('test')
    test_page.enter_pass('test')
    test_page.click_login_button()
    assert test_page.get_error_text() == '401'


def test_step_2(brows):
    logging.info("Test2 starting")
    test_page = OperationsHelper(brows)
    test_page.go_to_site()
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    assert test_page.get_success_text() == f'Hello, {testdata["login"]}'"""


def test_step_3(brows):
    logging.info("Test3 starting")
    test_page = OperationsHelper(brows)
    test_page.go_to_site()
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    test_page.click_contact_field()
    test_page.enter_contact_name_field(testdata['name'])
    test_page.enter_contact_email_field(testdata['email'])
    test_page.enter_contact_content_field(testdata['content'])
    test_page.click_btn_contact_us()
    time.sleep(5)
    assert test_page.alert() == 'Form successfully submitted'
    logging.info("PASSED")