import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("page_to_open", ["loc_admin"], indirect=True)
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
    time.sleep(1)
    admin_page.back()
    time.sleep(1)
    admin_page.page_select(2)
    time.sleep(1)

    # ищем элемент по тексту
    rows = admin_page.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    assert any("Devices" in row.text for row in rows), "Категория 'Devices' не найдена в таблице"   

    time.sleep(1) 



@pytest.mark.parametrize("page_to_open", ["loc_admin"], indirect=True)
def test_add_new_product(pages):
    _, _, _, _, admin_page = pages
    admin_page.login("user", "bitnami")
    time.sleep(2)
    admin_page.click_navigate("Catalog")
    time.sleep(1)
    admin_page.click_submenu_item("Products")
    time.sleep(2)
    for name, price in [("mouse1", "300"), ("mouse2", "450"), ("keyboard1", "650"), ("keyboard2", "1200")]:
        admin_page.add_new()
        time.sleep(1)
        admin_page.add_new_product(name, "Devices", price)
        time.sleep(1)

    admin_page.page_select(2)
    time.sleep(1)
    #Проверка, что продукт появился в таблице
    rows = admin_page.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    assert any(name in row.text for row in rows), f"Товар '{name}' не найден в таблице"

    time.sleep(1)




@pytest.mark.parametrize("page_to_open", ["loc"], indirect=True)
def test_watch_new_product(pages):
    home_page, _, _, _, _ = pages
    time.sleep(5)

    for name in ["mouse1", "mouse2", "keyboard1", "keyboard2"]:
        home_page.search(name)
        time.sleep(1)
        items = home_page.driver.find_elements(By.CSS_SELECTOR, ".product-thumb h4 a")
        assert any(name in item.text for item in items), f"'{name}' не найден на главной"



@pytest.mark.parametrize("page_to_open", ["loc_admin"], indirect=True)
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

    rows = admin_page.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    texts = [row.text for row in rows]
    assert not any("mouse1" in t for t in texts), "'mouse1' всё ещё в таблице"
    assert not any("keyboard1" in t for t in texts), "'keyboard1' всё ещё в таблице"

    time.sleep(1)

@pytest.mark.parametrize("page_to_open", ["loc"], indirect=True)
def test_watch_product_again(pages):
    home_page, _, _, _, _ = pages
    time.sleep(1)
    for name in ["mouse1", "keyboard1"]:
        home_page.search(name)
        time.sleep(1)
        items = home_page.driver.find_elements(By.CSS_SELECTOR, ".product-thumb h4 a")
        assert not any(name in item.text for item in items), f"'{name}' отображается, но должен быть удалён"