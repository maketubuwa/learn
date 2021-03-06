#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-04 21:57:15
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

from selenium import webdriver
from requests.exceptions import RequestException
import requests
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import json
from config import *



brower=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
wait=WebDriverWait(brower, 10)
def search(url):
	brower.get(url)
	try:
	    input = wait.until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
	    )
	    submit = wait.until(
	    	EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
	    input.send_keys("美食")
	    submit.click()
	    parse_page()
	    total = wait.until(
	    	EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
	    return total.text
	except TimeoutException:
		return None
   		

def next_page(page_num):
	try:
		input = wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
			)
		submit = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
			)
		input.clear()
		input.send_keys(page_num)
		submit.click()
		parse_page()
		num = wait.until(
			EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_num))
			)
	except:
		next_page(page_num)

def parse_page():
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-itemlist .items .item")))
	html = brower.page_source
	doc = pq(html)
	items = doc("#mainsrp-itemlist .items .item").items()
	for item in items:
		product = {	
			'image':item.find('.pic .img').attr('src'),
			'price':item.find('.price').text()[1:],
			'deal':item.find('.deal-cnt').text()[:-3],
			'title':item.find('.title').text(),
			'shop':item.find('.shop').text(),
			'location':item.find('.location').text()
		}
		write_to_file(product)


def write_to_file(content):
    with open('taobao.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main():
	url='https://www.taobao.com'
	total=search(url)
	total=int(re.compile('(\d+)').search(total).group(1))
	for i in range(2,total + 1):
		next_page(i)


if __name__ == '__main__':
		main()	