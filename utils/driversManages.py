from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOpt
from selenium.webdriver.firefox.options import Options as firefoxOpt


def get_driver(browser):
    if browser == 'Firefox':
        driver = firefox_driver_init()
    elif browser == "Edge":
        driver = edge_driver_init()
    elif browser == "Opera":
        driver = opera_driver_init()
    else:
        driver = chrome_driver_init()
    return driver


def chrome_driver_init():
    opt = chromeOpt()
    driver = webdriver.Chrome("./driver/ChromeDriver/chromedriver", options=opt)

    driver.implicitly_wait(30)
    driver.maximize_window()

    print('Open Chrome browser')
    return driver


def firefox_driver_init():
    options = firefoxOpt()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path="./driver/FirefoxDriver/geckodriver.exe", options=options)

    driver.implicitly_wait(30)
    driver.maximize_window()

    print('Open Firefox browser')
    return driver


def edge_driver_init():
    driver = webdriver.Edge(executable_path="./driver/EdgeDriver/msedgedriver.exe")

    driver.implicitly_wait(30)
    driver.maximize_window()

    print('Open Edge browser')
    return driver


def opera_driver_init():
    driver = webdriver.Opera(executable_path="./driver/OperaDriver/operadriver.exe")

    driver.implicitly_wait(30)
    driver.maximize_window()

    print('Open Edge browser')
    return driver
