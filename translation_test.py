import requests

text = "I love music."

source_language = "en"
target_language = "hi"

url = "https://api.mymemory.translated.net/get"

params = {
    "q": text,
    "langpair": f"{source_language}|{target_language}"
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)

data = response.json()

print("API response:")
print(data)

print("Translation:")
print(data["responseData"]["translatedText"])