# !usr/bin/python3
# -*- encoding=utf-8 -*-
# author: makerchen
# time: 2021-04-29

import requests
from urllib.parse import urlencode
import os
from hashlib import md5
# from multiprocessing.pool import Pool


def get_page():
	headers = {
		'Host':'www.toutiao.com',
		'referer':'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		'x-requested-with':'XMLHttpRequest'
	}

	params = {
		'aid':'24',
		'app_name':'web_search',
		'offset':'0',
		'format':'json',
		'keyword':'美女图片',
		'autoload':'true',
		'count':'20',
		'en_qc':'1',
		'cur_tab':'1',
		'from':'search_tab',
		'pd':'synthesis',
		'timestamp':'1619697085015',
		'_signature':'_02B4Z6wo00f01MkO4UwAAIDDAbIoUaRrGNzJKuXAAFLOMSOq9xP5e5Nm3d.J5rGlfElptIX8x1zAjVQjm5KalOlDDFeZUpi0zoxGewIkNXgB59MAdAIrtrliMXfJVrCiBRNXuIcED7cy6Xsc34'
	}
	base_url = 'https://www.toutiao.com/api/search/content/?'
	url = base_url + urlencode(params)
	try:
		response = requests.get(url,headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return None
	except requests.ConnectionError as e:
		print('Error:',e.args)

def get_images_url_and_title(json):
	if json:
		items = json.get('data')
		for item in items:
			title = item.get('title')
			images_url = item.get('detail_image_list')
			if images_url is None:
				continue
			else:
				for image_url in images_url:
					yield {
						'title':title,
						'image_url':image_url.get('url'),
						
					}

def save_images(item):
	if not os.path.exists('../images_file/{}'.format(item.get('title'))):
		os.mkdir('../images_file/{}'.format(item.get('title')))
	try:
		response = requests.get(item.get('image_url'))
		if response.status_code == 200:
			with open('../images_file/{filepath}/{filename}.{form}'.format(filepath=item.get('title'),filename=md5(response.content).hexdigest(),form='jpg'),'wb') as f:
				f.write(response.content)
		else:
			return print('None')
			# file_path = '../images_file/{filepath}/{filename}.{form}'.format(filepath=item.get('title'),filename=md5(response.content).hexdigest(),form='jpg')
			# if not os.path.exists(file_path):
			# 	with open('file_path','wb') as f:
			# 		f.write(response.content)
			# else:
			# 	print('Already Download',file_path)
	except requests.ConnectionError:
		print('Failed to save image')

def main():
	json = get_page()
	for item in get_images_url_and_title(json):
		print(item)
		save_images(item)

if __name__ == '__main__':
	main()
