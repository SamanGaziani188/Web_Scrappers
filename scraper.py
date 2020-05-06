import requests
from bs4 import BeautifulSoup
page = requests.get("https://datastudio.google.com/embed/u/0/reporting/1PLVi5amcc_R5Gh928gTE8-8r8-fLXJQF/page/R24IB")



soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()
print(soup)
#print(type(page.content)
#
#stats_div = soup.find("div", id="statistics")
#confirmed_cases = stats_div.select_one(".numbers-main").text
#print(f"Confirmed Cases {confirmed_cases}")
#
#
#all_cases = stats_div.select_one(".numbers-child > .row")
#all_values = all_cases.findAll("h4")
#all_keys = all_cases.findAll("h6")
#
#dictionary = {}
#for i in range(len(all_keys)):
#    dictionary[all_keys[i].text] = all_values[i].text
#print(dictionary)
