import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def verify_Create_Career_Page(URL):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    actions = ActionChains(driver)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(URL)
    driver.find_element("xpath","//button[@class=\"ui button GetStartedHeader__StyleButton-sc-fm1kyw-21 iYMvVn\"]").click()
    driver.find_element("xpath",
                        "//button[text()='Create your Career Page!']").click()
    driver.find_element("id",
                        "Company-name").send_keys("Rajat-demo")
    driver.find_element("name",
                        "headquarters").send_keys("Bangalore")
    driver.find_element("name",
                        "industryType").send_keys("Information Services")
    driver.find_element("css selector","p.text-sm").click()
    driver.find_element("css selector","div.css-egrrsv-control").click()
    time.sleep(2)
    actions.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER).perform()
    driver.find_element("name",
                        "companyWebsite").send_keys("www.rajat-demo.com")
    driver.find_element("name",
                        "companyDescription").send_keys("THis is demo")
    driver.find_element("name","Confirm & Continue").click()
    driver.find_element("name","firstName").send_keys("Rajat")
    driver.find_element("name", "lastName").send_keys("Joshi")
    driver.find_element("name", "phoneNumber").send_keys("9999988888")
    driver.find_element("name", "workEmail").send_keys("company@test.com")
    driver.find_element("name", "password").send_keys("testdemo")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 700)")
    time.sleep(2)
    driver.find_element("xpath", "//button[text()='Sign Up For Free']").click();
    text = driver.find_element("xpath","//a[text()='Sign Up']").text
    assert text == "Sign Up"




def verify_Posting_Job(URL):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    actions = ActionChains(driver)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(URL)
    driver.find_element("xpath","//button[@class=\"ui button GetStartedHeader__StyleButton-sc-fm1kyw-21 iYMvVn\"]").click()
    driver.find_element("xpath",
                        "//button[text()='Post a Job!']").click()
    driver.find_element("id",
                        "Company-name").send_keys("Rajat-demo")
    driver.find_element("name",
                        "headquarters").send_keys("Bangalore")
    driver.find_element("name",
                        "industryType").send_keys("Information Services")
    driver.find_element("css selector","p.text-sm").click()
    driver.find_element("css selector","div.css-egrrsv-control").click()
    time.sleep(2)
    actions.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER).perform()
    driver.find_element("name",
                        "companyWebsite").send_keys("www.rajat-demo.com")
    driver.find_element("name",
                        "companyDescription").send_keys("This is demo")
    driver.find_element("name",
                        "Confirm & Continue").click()

    #fill Job requirement
    driver.find_element("name","jobTitle").send_keys("Senior Quality Engineer")
    time.sleep(2)
    driver.find_element("css selector","p.text-sm").click()
    driver.find_element("css selector","div.css-1jqq78o-placeholder").click()
    time.sleep(2)
    actions.send_keys(Keys.ARROW_DOWN,Keys.ENTER).perform()
    driver.find_element("name","jobLocation").send_keys("Bangalore")
    time.sleep(2)
    driver.find_element("css selector", "p.text-sm").click()
    driver.find_element("xpath","//div[@class='ql-editor ql-blank']").send_keys("bcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebfabcdefgadcdefgadcdebf")
    driver.find_element("xpath","//p[text()='Full-Time']").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 700)")
    driver.find_element("xpath","//button[@type='submit']").click()

    #fill Job Details

    driver.find_element("name","minimumSalary").send_keys("90000")
    driver.find_element("name", "maximumSalary").send_keys("100000")
    driver.execute_script("window.scrollTo(400, 0)")
    driver.find_element("css selector","div.css-egrrsv-control").click()
    time.sleep(2)
    actions.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER).perform()
    driver.find_element("xpath","//input[@placeholder='Eg; IT consulting']").send_keys("Information Services")
    driver.find_element("css selector", "p.text-sm").click()
    driver.find_element("xpath", "//input[@placeholder='Eg; Python, Java']").click()
    driver.find_element("xpath", "//input[@placeholder='Eg; Python, Java']").send_keys("Selenium")
    driver.find_element("css selector", "p.text-sm").click()
    time.sleep(5)
    driver.find_element("xpath","//p[@class='text-sm']").click()
    driver.find_element("xpath", "//input[@placeholder='Eg; Python, Java']").send_keys("Java")
    time.sleep(2)
    driver.find_element("xpath", "//p[@class='text-sm']").click()
    time.sleep(5)
    driver.find_element("xpath", "//input[@placeholder='Eg; Python, Java']").click()
    driver.find_element("xpath", "//input[@placeholder='Eg; Python, Java']").send_keys("Robot Framework")
    time.sleep(2)
    driver.find_element("xpath", "//p[@class='text-sm']").click()
    time.sleep(5)
    driver.find_element("xpath", "//input[@placeholder='Eg; Python, Java']").click()
    driver.find_element("xpath", "//input[@placeholder='Eg; Python, Java']").send_keys("api")
    time.sleep(2)
    driver.find_element("xpath", "//p[@class='text-sm']").click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 400)")
    time.sleep(2)
    driver.find_element("css selector","div.css-ce7t0n-control").click()
    actions.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER).perform()
    driver.find_element("xpath","//button[text()='Create a job']").click()

    #Sign Up Page

    driver.find_element("name","firstName").send_keys("Rajat")
    driver.find_element("name", "lastName").send_keys("Joshi")
    driver.find_element("name", "phoneNumber").send_keys("9999988888")
    driver.find_element("name", "workEmail").send_keys("company@test.com")
    driver.find_element("name", "password").send_keys("testdemo")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 700)")
    time.sleep(2)
    driver.find_element("xpath", "//button[text()='Sign Up For Free']").click();
    text = driver.find_element("xpath","//a[text()='Sign Up']").text
    assert text == "Sign Up"