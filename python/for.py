from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_search():
    """Негативный тест: проверка поведения при неверном поисковом запросе."""
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://ru.wikipedia.org")

        # Находим поле поиска и вводим несуществующую статью
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        search_box.send_keys("Zemlya123")
        search_button = driver.find_element(By.XPATH, '//*[@id="searchButton"]')
        search_button.click()

        # Ждём появления текста страницы
        error_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mw-content-text"))
        ).text

        # Проверяем наличие сообщения об ошибке
        assert "совпадений не найдено" in error_text.lower() \
               or "не существует" in error_text.lower(), \
               "❌ Википедия не показала сообщение о том, что страница не найдена!"

        print("✅ Негативный тест пройден — страница не найдена, как ожидалось.")

    except Exception as e:
        print(f"❌ Ошибка при выполнении негативного теста: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_invalid_search()
