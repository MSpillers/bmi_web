import pytest,urllib
from flask_testing import LiveServerTestCase
from app import create_app
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_firefox_session():
   service = FirefoxService(executable_path=GeckoDriverManager().install())
   driver = webdriver.Firefox(service=service)
   driver.get("https://www.google.com")
   print(driver.title)
   driver.quit()


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

def test_home_page(client):

    #flask_app = create_app()

    #with flask_app.test_client() as test_client:
    response = client.get('/')
    assert response.status_code == 200


