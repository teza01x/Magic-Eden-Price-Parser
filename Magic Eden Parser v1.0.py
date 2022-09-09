import requests
import time
import random
from cfg import *


def getNftPage():
    for i in data:
        if i['price'] == prices[0]:
            try:
                RScore = i['rarity']['merarity']['score']
            except:
                RScore = i['rarity']['moonrank']['absolute_rarity']
            return {
                'Price': i['price'],
                'RarityScore': RScore,
                'Links': f"https://magiceden.io/item-details/{i['tokenMint']}",
                'JPG': i['extra']['img']
            }


def getPriceRange():
    if (prices[0] > pRangeStart) and (prices[0] < pRangeEnd):
        print("Успешно, найдена NFT по цене: {} SOL".format(prices[0]))
        nftpage = getNftPage()
        print(nftpage)
    else:
        print("NFT в заданном диапазоне - Нет. Продолжаю поиск...")


def main():
    for i in data:
        # print(i)
        prices.append(i['price'])
    try:
        prices.sort()
        print(prices)
        getPriceRange()
    except:
        print("Непредвиденная ошибка, обратитесь к менеджеру.")


if __name__ == "__main__":
    while True:
        url = f"https://api-mainnet.magiceden.dev/v2/collections/{collection}/listings?offset=0&limit=20"
        payload = {}
        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        if response.status_code == 200:
            print(f"Начали в {time.strftime('%X')}")
            data = response.json()

            prices = []

            main()

            print(f"Закончили в {time.strftime('%X')}")
            break
        else:
            print("Ошибка: {}".format(response.status_code))
            print("Ждем пару минут...")
            time.sleep(random.randrange(120, 160))
            print("Делаю запрос на сервер MagicEden...")
