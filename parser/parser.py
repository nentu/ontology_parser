import json
import os

import requests
from fake_useragent import UserAgent
from tqdm import tqdm

from config import *
ua = UserAgent()


headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ua.random,
    'x-requested-with': 'XMLHttpRequest',
}

def save_product_json(id, filename):
    params = {
        'id': id,
    }

    response = requests.get('https://www.dns-shop.ru/pwa/pwa/get-product/', params=params, cookies=cookies, headers=headers)

    assert response.status_code == 200, f"{response.status_code} != 200"

    with open(filename, 'w', encoding='utf8') as f:
        f.write(response.text)

def save_type(type_name: str, n = None):

    path = f'./data/{type_name}/'
    if not os.path.exists(path):
        os.mkdir(path)

    data = json.loads(open(path[:-1] + '.json').read())
    ids = [i['data']['id'] for i in data['containers']]
    if n is not None:
        ids = ids[:n]

    for id in tqdm(ids):
        save_product_json(id, path + f'{id}.json')

if __name__ == '__main__':
    for type_name in os.listdir('../data/'):
        if not type_name.endswith('.json'):
            continue
        type_name = type_name[:-len('.json')]
        save_type(type_name)

