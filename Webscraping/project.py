"""
Task  3: Web scraper program
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Module for wait
from time import sleep


# Define the Path of the driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()


def main():
    command()  # Calls the function for input value
    screenshot()  # TAkes the screenshot
    quit()  # Quit the program


def command():  # Creates an Option if the user would prefer Google or Bing search
    print("Enter [g] for Google Search or [b] for Bing search engine: ")
    a = input()
    if a == 'g':
        return google_search()
    elif a == 'b':
        return bing_search()
    else:
        return quit()


# Define the search engine website


def google_search():
    driver.get("https://search.google.com")
    print(driver.title)
    search = driver.find_element_by_name("q")  # search box
    # send a search value to the search box
    search.send_keys("Africans Top Models")
    search.send_keys(Keys.RETURN)  # enter button to search

    link = driver.find_element_by_xpath(
        '//*[@id="xjs"]/div/table/tbody/tr/td[3]/a')
    sleep(2)
    link.click()  # Execute to click link of the next page because my MAtriculation numeber is (9), therefore the search result +1 would be in the next page
    sleep(2)  # Sleep to delay the next action so that the page can load up fully

    found = driver.find_element_by_xpath('//*[@id="rso"]/div[3]/div/div[1]/a')
    found.click()
    sleep(5)


def bing_search():
    driver.get("http://bing.com")
    print(driver.title)
    search = driver.find_element_by_xpath('//*[@id="sb_form_q"]')  # search box
    # send a search value to the search box
    search.send_keys("Africans Top Models")
    search.send_keys(Keys.RETURN)  # enter button to search

    link = driver.find_element_by_xpath(
        '//*[@id="b_results"]/li[12]/nav/ul/li[2]/a')
    sleep(2)
    link.click()  # Execute to click link of the next page because my MAtriculation numeber is (9), therefore the search result +1 would be in the next page
    sleep(2)  # Sleep to delay the next action so that the page can load up fully

    found = driver.find_element_by_xpath('//*[@id="b_results"]/li[3]/h2/a')
    found.click()
    sleep(5)


def screenshot():    # TAking a screenshot
    driver.save_screenshot("screenshot.png")
    sleep(5)
    print("Screenshot Taken")


def quit():
    driver.quit()
    print("Program has ended")


main()
