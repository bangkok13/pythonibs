import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebScrapper:

    def __init__(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://www.google.com")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

        search = driver.find_element_by_name('q')
        search.send_keys("Selenide")
        search.send_keys(Keys.RETURN)

        results = driver.find_elements_by_css_selector('div.g')
        link = results[0].find_element_by_tag_name("a")
        first_href = link.get_attribute("href")

        if not 'selenide' in first_href:
            print('First link is not selenide')
            return
        else:
            print(f'First link is {first_href}\nFinding image...')
            search_elements = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hdtb-mitem [href]")))
            if not search_elements:
                print('images not found')
                return
            else:
                print('images found')
                driver.get(search_elements[1].get_attribute('href'))
                images = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".isv-r.PNCib.MSM1fd.BUooTd [href]")))
                search_menu_elements = driver.find_elements_by_css_selector(".T47uwc [href]")
                first_image_href = images[0].get_attribute('href')
                if 'selenide' in first_image_href:
                    print('Image has references to Selenide')
                else:
                    print('Image has no references to Selenide')
                driver.get(search_menu_elements[0].get_attribute('href'))
                results = driver.find_elements_by_css_selector('div.g')
                link = results[0].find_element_by_tag_name("a")
                new_first_href = link.get_attribute("href")
                if first_href == new_first_href:
                    print('Links are the same')
                else:
                    print('links are different')

def main():
    p = WebScrapper()


if __name__ == '__main__':
    main()