import pytest,urllib
from app import create_app
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def driver():
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    opts = Options()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts,service=service)
    return driver

def test_application_status(driver):
   driver.get("https://bmi-web-test-qa.herokuapp.com/")
   driver.quit()

#def test_form_submission(driver):
#   driver.get("https://bmi-web-test-qa.herokuapp.com/")
    #wait= WebDriverWait(driver,20)
    #driver.find_element(By.ID,"height").send_keys("511" + Keys.ENTER)
    #driver.find_elememt(By.ID,"weight").send_keys("200" + Keys.ENTER)
    #driver.find_elememt(By.ID,"submit").click()
    
    #assert driver.title == "Results"
#    driver.quit()



@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

#def test_home_page(client):

#    #flask_app = create_app()

#    #with flask_app.test_client() as test_client:
#    response = client.get('/')
#   assert response.status_code == 200


