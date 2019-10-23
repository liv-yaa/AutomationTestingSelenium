from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options) # Same as browser

start_url = "https://duckgo.com"
driver.get(start_url)
# print(driver.page_source.encode("utf-8"))

search_form = driver.find_element_by_id('search_form_input_homepage')

print(search_form)

search_form.send_keys('real python')
search_form.submit()

results = driver.find_elements_by_class_name('result')
print(results[0].text)

driver.quit()