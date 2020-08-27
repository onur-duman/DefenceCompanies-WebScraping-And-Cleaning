from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pandas as pd
import numpy as np

import time

driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
driver.get("https://people.defensenews.com/top-100/")
time.sleep(5)
defence_corps = pd.DataFrame(columns=["Year", "Rank", "Company", "Leadership", "Country",
                                      "Defense_Revenue_From_A_Year_Ago", "Defense_Revenue_From_Two_Years_Ago",
                                      "%Defense Revenue Change",
                                      "Total Revenue", "%of Revenue from Defence"])

act = ActionChains(driver)

def getDataFrame():
    global defence_corps
    for year in range(2020, 2004, -1):
        list_view = driver.find_element_by_xpath("//*[@id='dropyears']")
        list_view.click()
        time.sleep(1)
        list_view.send_keys(year)
        time.sleep(1)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        print("Year {} selected!".format(year))
        for row in range(1, 101):
            list_of_each_corp = [year]
            if 2021 > year > 2014:
                for column in [1, 3, 4, 5, 6, 7, 8, 9, 10]:
                    text = driver.find_element_by_xpath("//*[@id='topHS']/tbody/tr[{}]/td[{}]".format(row, column))
                    list_of_each_corp.append(text.text)
            elif 2015 > year > 2009:
                for column in [1, 2, 3, 10, 5, 6, 7, 8, 9]:
                    text = driver.find_element_by_xpath("//*[@id='topHS']/tbody/tr[{}]/td[{}]".format(row, column))
                    list_of_each_corp.append(text.text)
            else:
                for column in [1, 2, 3, 9, 5, 6, 111, 7, 8]:
                    if column == 111:
                        list_of_each_corp.append(np.nan)
                    else:
                        text = driver.find_element_by_xpath("//*[@id='topHS']/tbody/tr[{}]/td[{}]".format(row, column))
                        list_of_each_corp.append(text.text)

            defence_corps.loc[len(defence_corps)] = list_of_each_corp
        print("Year {}'s Data Took!".format(year))

if __name__ == '__main__':
    getDataFrame()
    defence_corps.to_csv("defence_companies_from_2005.csv", index=False, header=True)




