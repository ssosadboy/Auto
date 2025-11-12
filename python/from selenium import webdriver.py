from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера
driver = webdriver.Chrome()

try:
    driver.get("https://ru.wikipedia.org")

    # Находим поле поиска и вводим запрос "Земля"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_box.send_keys("Земля")

    # Нажимаем кнопку поиска
    search_button = driver.find_element(By.XPATH, '//*[@id="searchButton"]')
    search_button.click()

    # Ждём, пока откроется страница статьи с заголовком "Земля"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "firstHeading"), "Земля")
    )

    # Извлекаем текст статьи
    body_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bodyContent"))
    ).text

    # Проверяем наличие информации о 20,95% кислорода
    assert "20,95" in body_text or "20.95" in body_text, "❌ Кислород исчез из атмосферы!"

    print("✅ Земля всё ещё пригодна для дыхания — 20,95% кислорода найдено!")

except Exception as e:
    print(f"❌ Ошибка при выполнении теста: {e}")

finally:
    driver.quit()
