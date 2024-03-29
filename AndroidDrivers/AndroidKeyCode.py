from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3aXL'
desired_caps['app'] = 'C:\\Users\\Alex\\Downloads\\Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps["automationName"] = "UiAutomator2"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)

button_enter_some_value = driver.find_element(By.ID, 'com.code2lead.kwad:id/EnterValue')
button_enter_some_value.click()

text_field = driver.find_element(By.CLASS_NAME, 'android.widget.EditText')
text_field.send_keys('Code2Lead')
text_field.click()

driver.press_keycode(67)
driver.press_keycode(67)

driver.press_keycode(4)
driver.press_keycode(4)