import requests
import json

def fetch_tweets(query="#PakPrideFMAsimMunir"):
    url = "https://twitter241.p.rapidapi.com/search"
    querystring = {
        "type": "Latest",
        "count": "20",
        "query": query
    }

    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": "twitter241.p.rapidapi.com",
        "x-rapidapi-key": "91d805eeafmsh58718c243983d79p124e95jsn4276eb5b726c"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # print(data)

    tweets = []
    
    # Navigate into the API structure to reach tweets
    try:
        entries = data["result"]["timeline"]["instructions"][0]["entries"]
    except (KeyError, IndexError):
        print("Could not find tweets in response.")
        return []

    for entry in entries:
        try:
            result_node = entry["content"]["itemContent"]["tweet_results"]["result"]
            tweet_legacy = result_node["legacy"]
            user_core = result_node["core"]["user_results"]["result"]["core"]
            
            full_text = tweet_legacy.get("full_text", "")
            media_items = tweet_legacy.get("extended_entities", {}).get("media", [])
            media_urls = [m.get("media_url_https") for m in media_items if m.get("type") == "photo"]
            
            tweets.append({
                "text": full_text.strip(),
                "images": media_urls,
                "username": user_core.get("name", ""),
                "handle": f"@{user_core.get('screen_name', '')}",
                "likes": tweet_legacy.get("favorite_count", 0),
                "comments": tweet_legacy.get("reply_count", 0),
                "shares": tweet_legacy.get("retweet_count", 0),
                "tweet_created_at": tweet_legacy.get("created_at", ""),
                "user_created_at": user_core.get("created_at", "") or result_node.get("core", {}).get("user_results", {}).get("result", {}).get("legacy", {}).get("created_at", "")
            })
        except KeyError:
            continue

    return tweets

# res = fetch_tweets()
# print(res)


def get_trends():
    API_KEY = "91d805eeafmsh58718c243983d79p124e95jsn4276eb5b726c"

    url = "https://twitter241.p.rapidapi.com/trends-by-location"

    querystring = {"woeid": "2211096"}  # Karachi

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "twitter241.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    # Extract trends
    trends = data["result"][0]["trends"]

    return trends[:10]

import sys

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    tweets = fetch_tweets()
    if not tweets:
        print("No tweets found.")
    else:
        for i, t in enumerate(tweets, start=1):
            print(f"\nTweet {i}:")
            print(f"User: {t['username']} ({t['handle']})")
            print(t["text"])
            print(f"Likes: {t['likes']} | Comments: {t['comments']} | Shares: {t['shares']}")
            if t["images"]:
                print("Images:")
                for img in t["images"]:
                    print(f" - {img}")
