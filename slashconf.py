import slash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from sqlalchemy import True_


# @slash.parametrize("browser_name", ["chrome"])
@slash.fixture(autouse=True,scope="session")
def Driver():

    print("Inside webdriver fixture")
    # if browser_name == "chrome":
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(5)
    # elif browser_name == "edge":
    #     driver = webdriver.Edge()
    #     driver.implicitly_wait(5)
    #
    # else:
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(5)
    # driver = webdriver.Chrome()
    opt = Options()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opt)
    yield driver
    print("after yield")
    driver.quit()
