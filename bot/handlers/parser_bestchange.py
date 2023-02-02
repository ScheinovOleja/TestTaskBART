import json
import re

from aiohttp import ClientSession
from bs4 import BeautifulSoup


async def get_the_difference(exchange: str):
    async with ClientSession() as session:
        async with session.get('https://www.bestchange.ru/bitcoin-to-tether-trc20.html') as response:
            soup = BeautifulSoup(await response.text(), "lxml")
    leader = soup.select_one('table#content_table > tbody > tr:nth-child(1)')
    leader_name = leader.select_one('td.bj > div.pa > div.pc > div.ca').text
    leader_get = float(leader.find_all('td', class_='bi')[1].text.replace(" USDT TRC20", '').replace(' ', ''))

    requested = soup.find(string=re.compile(exchange, re.I)).find_parent('tr')
    requested_name = requested.select_one('td.bj > div.pa > div.pc > div.ca').text
    requested_get = float(requested.find_all('td', class_='bi')[1].text.replace(" USDT TRC20", '').replace(' ', ''))
    return requested_name, requested_get, leader_name, leader_get
