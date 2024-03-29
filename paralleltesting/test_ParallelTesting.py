from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
import time


def device_driver(device_uiid, systemPort):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'Pixel_3a_XL'
    desired_caps['app'] = 'C:\\Users\\Alex\\Downloads\\Android_Appium_Demo.apk'
    desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
    desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'
    desired_caps["automationName"] = "UiAutomator2"
    # new desired_caps for parallel working
    desired_caps['udid'] = device_uiid
    desired_caps['systemPort'] = systemPort # Default is 8200 an in range 8200 - 8299

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    return driver


def enter_text(driver):
    button_enter_some_value = driver.find_element(By.ID, 'com.skill2lead.appiumdemo:id/EnterValue')
    button_enter_some_value.click()

    time.sleep(2)
    text_field = driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys('Code2Lead')

    time.sleep(2)
    driver.quit()


def test_multiple_devices():
    driver_one = device_driver('emulator-5554', 8200)
    driver_two = device_driver('emulator-5556', 8201)

    enter_text(driver_one)
    enter_text(driver_two)
