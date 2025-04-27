import pytest
import allure
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", action="store", default="localhost:4444")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture(scope="module")
def driver(request):
    executor = request.config.getoption("--executor")
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    executor_url = f"http://{executor}/wd/hub"

    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False,
            # "enableVideo": True,
            # "videoName": f"{request.node.name}.mp4"
        })

        browser = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.set_capability("browserName", "firefox")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })

        browser = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    else:
        raise NotImplementedError(f"Browser {browser_name} is not supported.")

    # Allure: добавляем capabilities
    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities),
        attachment_type=allure.attachment_type.JSON,
    )

    yield browser
    browser.quit()


@pytest.fixture(scope="module")
def pages(driver):
    from page.Home_page import HomePage
    from page.Product_page import ProductPage
    from page.Review_page import ReviewPage
    from page.Login_page import LoginPage
    from page.Admin_page import AdminPage

    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    review_page = ReviewPage(driver)
    login_page = LoginPage(driver)
    admin_page = AdminPage(driver)
    return home_page, product_page, review_page, login_page, admin_page


@pytest.fixture(scope="function")
def page_to_open(request):
    return request.param


@pytest.fixture(scope="function", autouse=True)
def setup(driver, pages, page_to_open):
    home_page, _, _, _, admin_page = pages

    if page_to_open == "home":
        home_page.navigate_to_product("https://demo-opencart.ru/index.php")
    elif page_to_open == "admin":
        admin_page.navigate_to_admin("https://demo-opencart.ru/admin/index.php")
# @pytest.fixture(scope="module", autouse=True)
# def setup(driver, pages):
#     home_page, _, _, _, _ = pages
#     home_page.navigate_to_product("https://demo-opencart.ru/index.php")
