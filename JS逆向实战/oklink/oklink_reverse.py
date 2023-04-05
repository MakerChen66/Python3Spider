# -*- coding: utf-8 -*-

"""
@author: makerchen
@微信公众号：小鸿星空科技
"""

import requests
import time
import random
import base64


def get_apikey(now_time):
	API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
	key1 = API_KEY[0:8]
	key2 = API_KEY[8:]
	new_key = key2 + key1
	new_time = str(1 * now_time + 1111111111111)
	random1 = str(random.randint(0, 9))
	random2 = str(random.randint(0, 9))
	random3 = str(random.randint(0, 9))
	now_time = new_time + random1 + random2 + random3
	last_key = new_key + '|' + now_time
	x_apiKey = base64.b64encode(last_key.encode('utf-8'))
	return str(x_apiKey, encoding='utf-8')


now_time = int(time.time()) * 1000
headers = {
	'x-apikey': 'a2c903cc-b31e-4547-9299-b6d07b7631ab',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
api = f'https://www.oklink.com/api/explorer/v1/eth/address/0xdac17f958d2ee523a2206206994597c13d831ec7/more?t={now_time}'
res = requests.get(url=api, headers=headers)
print(res.json())