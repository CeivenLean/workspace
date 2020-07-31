import requests

url = "https://www.birdiesearch.com/api/search"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",

}

cookies = {
    "userInfo": "Y2VpdmVuQGZveG1haWwuY29t_MjAxOS0wOC0zMSAwOTozOQ",
    "userInfo.sig": "EqIAgmtZvOVUQSfWCsi5uVqNmPk"
}

args = {
    "word": "vue",
    "pages": 1,
    "filter[type]": "vague",
    "filter[search]": "all",
    "filter[field]": "resources",
    "filter[cloud]": "all",
    "filter[sharerId]": "undefined"
}

res = requests.get(url=url, params=args, headers=headers, cookies=cookies)

print(res.text)
