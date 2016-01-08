#!/usr/bin/python
# encoding: utf-8
'''
@author: jaak
'''

from lxml import html
import requests

url = 'http://meteo.physic.ut.ee/et/frontmain.php?m=2'

page = requests.get(url)
tree = html.fromstring(page.content)
#temp = tree.xpath('/html/body/table[1]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/b')
temp = tree.xpath('//b')
print 'Tartu '+temp[1].text.encode('utf-8')