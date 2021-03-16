#!/usr/bin/env python3

import sys
from selenium import webdriver
from monster import Monster
import json
import logging

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
    monster_name = elem.text
    elem.click()
    driver.switch_to.parent_frame()
    driver.switch_to.frame("data")
    image_url = driver.find_element_by_tag_name("img")
    tables = driver.find_elements_by_css_selector("body > table")
    # skip multiple species for now
    logging.info(f"multi table {monster_name}")
    for t in tables:
        try:
            monsters.append(
                Monster.from_table(monster_name, image_url.get_property("src"), t)
            )
            continue
        except:
            if t == tables[-1]:
                logging.error(f"could not parse {monster_name}: {sys.exc_info()[0]}")
    driver.switch_to.parent_frame()
    driver.switch_to.frame("toc")

driver.close()

json_string = json.dumps([ob.__dict__ for ob in monsters])
print(json_string)