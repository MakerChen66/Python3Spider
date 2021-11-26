"""
@author：makerchen
@time：2019-10-13
原创微信公众号：小鸿星空科技
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from requests.exceptions import RequestException


def get_url_html():
	"""User-Agent可自行替换"""
  headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
      'Host':'www.qiushibaike.com',
      'Cookie':'_ga=GA1.2.2026142502.1558849033; gr_user_id=5d0a35ad-3eb6-4037-9b4d-bbc5e22c9b9f; grwng_uid=9bd612b3-7d0b-4a08-a4e1-1707e33f6995; _qqq_uuid_="2|1:0|10:1617119039|10:_qqq_uuid_|56:NjUxYWRiNDFhZTYxMjk4ZGM3MTgwYjkxMGJjNjViY2ZmZGUyNDdjMw==|fdce75d742741575ef41cd8f540465fb97b5d18891a9abb0849b3a09c530f7ee"; _xsrf=2|6d1ed4a0|7de9818067dac3b8a4e624fdd75fc972|1618129183; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1617119039,1617956477,1618129185; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1618129185; ff2672c245bd193c6261e9ab2cd35865_gr_session_id=fd4b35b4-86d1-4e79-96f4-45bcbcbb6524; ff2672c245bd193c6261e9ab2cd35865_gr_session_id_fd4b35b4-86d1-4e79-96f4-45bcbcbb6524=true'

    }

  try:
    for page in range(2,5):
      url = f'https://www.qiushibaike.com/hot/page/{page}/'
      req = requests.get(url,headers=headers)
      if req in not None:
        return req.text
      else:
        return None
  except RequestException:
    return None

def main():
  html = get_url_html()
  soup = BeautifulSoup(html,'lxml')
  for joke in soup.select('.contentHerf .content span'):
    if joke.string is not None:
      joke_data = f'笑话一则:{joke.string.strip()}\n\n'
      with open('../txt_file/joke.txt','ab') as f:
          pattern = re.compile('查看全文',re.S)
          jok = re.sub(pattern,'这里被替换了，嘻嘻!',joke_data)
          f.write(joke.encode('utf-8'))
          


if __name__ == '__main__':
  main()
  time.sleep(1)