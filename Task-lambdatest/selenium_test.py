from selenium import webdriver
from time import sleep

url = "http://localhost:4444/wd/hub"
print(url)

browser = "chrome"

driver = webdriver.Remote(command_executor = url, desired_capabilities = {'browserName':'chrome'})
driver.get('https://farnodes.com/')
sleep(1)
driver.get_screenshot_as_file("screenshot2.png")
driver.quit()
print("end...")