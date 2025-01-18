# page_object_proj
Page Object style project with pytests using selenium python

# Start
## Установить виртуальное окружение командой (пример для python3.10)
python3.10 -m venv venv

## Активировать окружение
source venv/bin/activate

## Установить пакеты
pip install -r requirements.txt

## Запустить тесты
pytest -v --tb=line --language=en -m need_review

## Ожидаемый результат

test_product_page.py::TestUserAddToBasketFromProductPage::test_user_can_add_product_to_basket PASSED                                             [ 25%]
test_product_page.py::TestProductPageGuest::test_guest_can_add_product_to_basket PASSED                                                          [ 50%]
test_product_page.py::TestProductPageGuest::test_guest_cant_see_product_in_basket_opened_from_product_page PASSED                                [ 75%]
test_product_page.py::TestProductPageGuest::test_guest_can_go_to_login_page_from_product_page PASSED                                             [100%]