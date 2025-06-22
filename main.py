# Emanuel Biruk Seifegebreal --> 2024 - A project for learning purposes
# Note: Websites change frequently so please expect this program not to work and focus on the program's logic
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(2)
web_cookies_accept = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]")
web_cookies_accept.click()
driver.implicitly_wait(10)
choose_english = driver.find_element(By.ID, "langSelect-EN")
choose_english.click()

# Cookie clicks
time.sleep(5)
cookie = driver.find_element(By.ID, 'bigCookie')

timeout = time.time() + 5
five_min = time.time() + 5 * 60
print(timeout)

while True:
    cookie.click()

    if time.time() > timeout:
        print('5 sec')
        upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        if len(upgrades) != 0:
            upgrades[-1].click()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, 'cookiesPerSecond').text
        print(cookie_per_s)
        break
