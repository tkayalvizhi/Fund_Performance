from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class Driver:
    def __init__(self):
        self.path = r'Resources\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.url = "https://www.iciciprulife.com/fund-performance/all-products-fund-performance-details.html"

    def open_url(self):
        self.driver.get(self.url)

    def get_date(self):
        heads = self.driver.find_elements(By.TAG_NAME, 'thead')
        head = heads[1]
        date = head.find_element_by_class_name('dateid')

        return date.text

    def get_data(self, funds):
        latest_nav = {}

        self.driver.find_element_by_xpath('//*[@id="byproduct"]/div[1]/div[1]/ul/li[4]/a').click()
        bodies = self.driver.find_elements(By.TAG_NAME, 'tbody')
        body = bodies[1]

        rows = body.find_elements_by_tag_name('tr')
        # print(rows)

        for row in rows:
            # print(row.text)
            cells = row.find_elements_by_tag_name('td')
            # print(cells.text)
            fund_name = cells[0].text.split('\n')[0]

            if funds.__contains__(fund_name):
                latest_nav[fund_name] = cells[3].text

        # print(data)
        data_frame = pd.DataFrame.from_dict(data=latest_nav, orient='index')
        print(data_frame)
        return latest_nav

    def close(self):
        self.driver.close()
        self.driver.quit()
