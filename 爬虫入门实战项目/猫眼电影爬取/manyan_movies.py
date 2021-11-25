"""
@author：makerchen
@time：2019-10-12
原创微信公众号：小鸿星空科技
"""

import requests
import re
import time
from requests import exceptions
import json
import pymongo

def get_one_page(url):
	try:
		headers = {'User-Agent':'Mozilla/5.0'}
		response = requests.get(url,headers=headers)
		if response.status_code == 200:
			return response.text
		else:
			return None
	except exceptions.RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
	movies_information = re.findall(pattern,html)
	for movie_information in movies_information:
		yield {
			'电影排名':movie_information[0],
			'图片地址':movie_information[1],
			'电影名':movie_information[2].strip(),
			'演员':movie_information[3].strip()[3:] if len(movie_information) > 3 else '',
			'上映时间':movie_information[4].strip()[5:] if len(movie_information) > 5 else '',
			'评分':movie_information[5].strip() + movie_information[6].strip()
		}

def write_movies_data_to_file(movie_information):
	"""请自行替换数据存储路径"""

	with open('../txt_file/maoyan_movies_information.txt','a',encoding='utf-8') as f:
		f.write(json.dumps(movie_information,indent=2,ensure_ascii=False) + '\n')

def main(offset):
	url = f'https://maoyan.com/board/4?offset={offset}'
	html = get_one_page(url)
	for movie_information in parse_one_page(html):
		print(movie_information)
		write_movies_data_to_file(movie_information)
		insert_to_mongodb(movie_information)

def insert_to_mongodb(content):
	"""请自行替换数据库名和集合名"""

	client = pymongo.MongoClient(host='localhost',port=27017)
	db = client['spiders']
	collection = db['maoyan_movies_data']
	try:
		if content:
			collection.insert(content)
			print('Success to insert!')
	except:
		print('Failed to insert!')

if __name__ == '__main__':
	for i in range(10):
		main(offset=i*10)
		time.sleep(1)

