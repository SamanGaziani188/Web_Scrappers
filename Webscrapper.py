# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:48:26 2020

@author: Saman
"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

path = "E:/Corona Dashboard/Webscrapper/chromedriver/chromedriver_win32/chromedriver.exe"
driver = Chrome(executable_path = path)
driver.get("http://covid.gov.pk/stats/punjab")

act = ActionChains(driver)
act.context_click().perform() 