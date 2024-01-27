import requests


def get_coin_info_func(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    data = response.json()

    formated_data = {
        "name": data["name"],
        "symbol": data["symbol"],
        "hashing_algorithm": data["hashing_algorithm"],
        "categories": data["categories"],
        "links1": data["links"]["blockchain_site"][0],
        "links2": data["links"]["blockchain_site"][1],
        "links3": data["links"]["blockchain_site"][2],
        "linksh": data["links"]["homepage"][0],
        "genesis_date": data["genesis_date"],
        "current_price": data["market_data"]["current_price"]["usd"],
        "market_cap": data["market_data"]["market_cap"]["usd"],
    }
    return formated_data


def get_cryptocurrency_history(coin_id, date):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history?date={date}"
    response = requests.get(url)
    data = response.json()
    return data


def get_current_price(time, coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    data = response.json()
    if time == "1h":
        price = [data["market_data"]["price_change_percentage_1h_in_currency"]["usd"]]
        return price
    elif time == "24h":
        price = [data["market_data"]["price_change_24h"], data["market_data"]["price_change_percentage_24h"]]
        return price
    elif time == "7d":
        price = [data["market_data"]["price_change_percentage_7d"]]
        return price
    elif time == "1m":
        price = [data["market_data"]["price_change_percentage_30d"]]
        return price
    elif time == "1y":
        price = [data["market_data"]["price_change_percentage_1y"]]
        return price


def get_trending_coins(limit=3):
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    data = response.json()

    all_coins_info = []
    for i in range(limit):
        coin_info = {
            "name": data["coins"][i]["item"]["name"],
            "large": data["coins"][i]["item"]["large"],
            "price": data["coins"][i]["item"]["data"]["price"],
            "price_change_percentage_24h": data["coins"][i]["item"]["data"]["price_change_percentage_24h"]["usd"],
            "sparkline": data["coins"][i]["item"]["data"]["sparkline"],
            "content": data["coins"][i]["item"]["data"]["content"],
        }
        all_coins_info.append(coin_info)

    return all_coins_info


def get_top_exchanges(limit=5):
    url = "https://api.coingecko.com/api/v3/exchanges"
    response = requests.get(url)
    data = response.json()

    all_exchanges_info = []
    for i in range(limit):
        exchange_info = {
            "name": data[i]["name"],
            "year_established": data[i]["year_established"],
            "country": data[i]["country"],
            "url": data[i]["url"],
            "trust_score": data[i]["trust_score"],
            "trust_score_rank": data[i]["trust_score_rank"],
            "trade_volume_24h_btc": data[i]["trade_volume_24h_btc"],
        }
        all_exchanges_info.append(exchange_info)

    return all_exchanges_info


def get_top_categories(limit=3):
    url = "https://api.coingecko.com/api/v3/coins/categories"
    response = requests.get(url)
    data = response.json()

    all_categories_info = []
    for i in range(limit):
        coins_names = []
        for j in range(limit):
            coins_names.append(data[i]["top_3_coins"][j].split("/")[-1].split(".")[0])

        categories_info = {
            "name": data[i]["name"],
            "top_3_coins": coins_names,
            "market_cap": data[i]["market_cap"]
        }
        all_categories_info.append(categories_info)

    return all_categories_info
