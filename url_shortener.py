import requests

class URLShortener:
    def __init__(self, access_token):
        self.access_token = access_token
 # self.access_token = access_token        self.base_url = "https://api-ssl.bitly.com/v4"

    def shorten_url(self, long_url):
        url = f"{self.base_url}/shorten"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "long_url": long_url
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data['link']
 # 19        else:
            print(f"Error shortening URL: {response.status_code} - {response.text}")
            return None

    def expand_url(self, short_url):
        url = f"{self.base_url}/expand"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "bitlink_id": short_url.replace("https://", "").replace("http://", "")
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data['long_url']
        else:
            print(f"Error expanding URL: {response.status_code} - {response.text}")
            return None

