import requests
import json, re


urls = [
    'https://hidden.url',
]
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}

review_dict = dict()
COUNTER = 1
for url in urls:
    response = requests.get(url, headers=headers)
    response.encoding = "ISO-8859-15"

    response_text = response.text.split("(", 1)[-1]  # split step 1
    response_text = response_text.rsplit(")", 1)[0]  # splist step 2
    # response_json = json.loads(response_text)

    regex_pattern = re.compile(r'\"ReviewText\":\"(.*?)","Title')
    review_text = re.findall(regex_pattern, response_text)
    
    for review in review_text:
        review_dict.update({
            f"review_{COUNTER}": review,
        })
        COUNTER += 1

with open("ratings.json", "w", encoding="utf-8") as f:
    json.dump(review_dict, f, ensure_ascii=False, indent=4)
