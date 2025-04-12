import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.admin
@pytest.mark.parametrize("email, password", [("user", "bitnami")])
def login_as_admin(pages, email, password):
    _, _, _, _, admin_page = pages
    admin_page.login(email, password)
    time.sleep(2)
    
def add_Devices(pages):
    _, _, _, _, admin_page = pages
    admin_page.click_menu("Catalog")
    time.sleep(2)
    admin_page.click_submenu("Categories")
    time.sleep(2)