"""
@author：makerchen
@time：2019-7-22
@原创微信公众号：小鸿星空科技
"""

import requests
from bs4 import BeautifulSoup

headers = {"user-agent":"Mozilla/5.0"}

def hack_number(text):
  text = text.encode('utf-8')
  text = text.replace(b'\xef\x82\x9d', b'0')
  text = text.replace(b'\xee\xa6\x88', b'1')
  text = text.replace(b'\xee\xa8\xb4', b'2')
  text = text.replace(b'\xef\x91\xbe', b'3')
  text = text.replace(b'\xee\x88\x9d', b'4')
  text = text.replace(b'\xef\x97\x80', b'5')
  text = text.replace(b'\xee\x85\x9f', b'6')
  text = text.replace(b'\xee\x98\x92', b'7')
  text = text.replace(b'\xef\x80\x95', b'8')
  text = text.replace(b'\xef\x94\x9b', b'9')
  text = text.decode()

  return text

def detail_page(url):
  req = requests.get(url,headers=headers)
  html = req.text
  
  soup = BeautifulSoup(html,'lxml')
  job_name = soup.select('.new_job_name')[0].text.strip()
  job_money = hack_number(soup.select('.job_money')[0].text.strip())
  job_position = soup.select('.job_position')[0].text.strip()
  job_academic = soup.select('.job_academic')[0].text.strip()
  job_detail = soup.select('.job_detail')[0].text.strip()
  job_week = hack_number(soup.select('.job_week')[0].text.strip())
  job_time = hack_number(soup.select('.job_time')[0].text.strip())

  print(job_name,job_money,job_position,job_academic,job_week,job_time)
  print(job_detail)


#detail_page('https://www.shixiseng.com/intern/inn_1k3vhcwwguaf?pcm=pc_SearchList')
#detail_page('https://www.shixiseng.com/intern/inn_uk1lm380lngh?pcm=pc_SearchList')
#detail_page('https://www.shixiseng.com/intern/inn_fr1o1nii5knw?pcm=pc_SearchList')

#爬取多少页可自行调式
for pages in range(1,3):
  url = f'https://www.shixiseng.com/interns?page={pages}&keyword=Python&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E8%B4%B5%E9%98%B3&internExtend='
  req = requests.get(url,headers=headers)
  html = req.text

  soup = BeautifulSoup(html,'lxml')
  for item in soup.select('a.title ellipsis font'):
    detail_url = f"https://www.shixiseng.com{item.get('href')}"
    detail_page(detail_url)