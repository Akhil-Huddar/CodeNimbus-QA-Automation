from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Browser:", driver.capabilities.get("browserName"))
print("Title:", driver.title)

input("Press Enter to close...")

driver.quit()