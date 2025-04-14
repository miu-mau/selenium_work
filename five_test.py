import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("page_to_open", ["admin"], indirect=True)
def test_add_Devices_in_Catalog(pages):
    _, _, _, _, admin_page = pages
    admin_page.login("user", "bitnami")
    time.sleep(2)
    admin_page.click_navigate("Catalog")
    time.sleep(1)
    admin_page.click_submenu_item("Categories")
    time.sleep(2)
    admin_page.add_new()
    time.sleep(1)
    admin_page.add_new_category("Devices")
    time.sleep(2)

@pytest.mark.parametrize("page_to_open", ["admin"], indirect=True)
def test_add_new_product(pages):
    _, _, _, _, admin_page = pages
    admin_page.login("user", "bitnami")
    time.sleep(2)
    admin_page.click_navigate("Catalog")
    time.sleep(1)
    admin_page.click_submenu_item("Products")
    time.sleep(2)
    admin_page.add_new()
    time.sleep(1)
    admin_page.add_new_product("mouse1", "Devices", "300")
    time.sleep(1)
    admin_page.add_new()
    time.sleep(1)
    admin_page.add_new_product("mouse2", "Devices", "450")
    time.sleep(1)
    admin_page.add_new()
    time.sleep(1)
    admin_page.add_new_product("keyboard1", "Devices", "650")
    time.sleep(1)
    admin_page.add_new()
    time.sleep(1)
    admin_page.add_new_product("keyboard2", "Devices", "1200")
    time.sleep(1)


@pytest.mark.parametrize("page_to_open", ["home"], indirect=True)
def test_watch_new_product(pages):
    home_page, _, _, _, _ = pages
    time.sleep(1)
    home_page.search("mouse1")
    home_page.search("mouse2")
    home_page.search("keyboard1")
    home_page.search("keyboard2")



@pytest.mark.parametrize("page_to_open", ["admin"], indirect=True)
def test_delete_product(pages):
    _, _, _, _, admin_page = pages
    admin_page.login("user", "bitnami")
    time.sleep(2)
    admin_page.click_navigate("Catalog")
    time.sleep(1)
    admin_page.click_submenu_item("Products")
    time.sleep(2)
    admin_page.page_select(2)
    time.sleep(1)
    admin_page.select_product("mouse1")
    time.sleep(1)
    admin_page.scroll_up(200)
    time.sleep(1)
    admin_page.select_product("keyboard1")
    time.sleep(1)
    admin_page.delete_product()
    time.sleep(1)

@pytest.mark.parametrize("page_to_open", ["home"], indirect=True)
def test_watch_product_again(pages):
    home_page, _, _, _, _ = pages
    time.sleep(1)
    home_page.search("mouse1")
    home_page.search("mouse2")
    home_page.search("keyboard1")
    home_page.search("keyboard2")