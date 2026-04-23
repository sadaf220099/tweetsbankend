import requests
import json

def fetch_test():
    url = "https://twitter241.p.rapidapi.com/search"
    querystring = {
        "type": "Latest",
        "count": "1",
        "query": "hello"
    }
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": "twitter241.p.rapidapi.com",
        "x-rapidapi-key": "91d805eeafmsh58718c243983d79p124e95jsn4276eb5b726c"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    with open("response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Done")

if __name__ == "__main__":
    fetch_test()
