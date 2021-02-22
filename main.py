#!/usr/bin/env python3

from selenium import webdriver
from monster import Monster
import json

url = "https://www.purpleworm.org/rules/"

driver = webdriver.Chrome()

driver.get(url)

driver.switch_to.frame("toc")
driver.find_element_by_css_selector(
    "#span00004outer > table > tbody > tr > td.nodeText18"
).click()
driver.find_element_by_css_selector(
    "#span00004\.00007outer > table > tbody > tr > td.nodeText18"
).click()

# elems = driver.find_elements_by_id("span00004.00007.00001outer")
monsters = []
elems = driver.find_elements_by_css_selector(
    "span[id^='span00004.00007.0'][id$='outer']"
)
for elem in elems:
    elem.click()
    driver.switch_to.parent_frame()
    driver.switch_to.frame("data")
    table = driver.find_elements_by_css_selector("body > table")
    # skip multiple species for now
    if len(table) > 1:
        driver.switch_to.parent_frame()
        driver.switch_to.frame("toc")
        continue
    try:
        monsters.append(Monster.from_table(table[0]))
    except:
        print(f"could not parse {table.text}")
        driver.switch_to.parent_frame()
        driver.switch_to.frame("toc")
        continue
    driver.switch_to.parent_frame()
    driver.switch_to.frame("toc")

driver.close()

json_string = json.dumps([ob.__dict__ for ob in monsters])
print(json_string)