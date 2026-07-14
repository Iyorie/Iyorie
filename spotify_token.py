import requests
from requests.auth import HTTPBasicAuth

CLIENT_ID = "4747416f69a4412bba80a9b79e4ce33e"
CLIENT_SECRET = "799e3aaa4cd24e7aad0c918a803698d6"
CODE = "AQDVyCvUqAmmn-el73n1O3_xQg1emEERBA9B9jhTXxoSFmp4P44NnHEoVgBUWqKi8K7F2iSDLwV-Z8oRoOQ63hgC6qHHboVCicOJ3jyqE3oNTNgRzNI9f6iiGgwhW-Rot9nBWYxjSN14yfJ5uwFwxy8pVZwwAvAs1WTyWQVo3Kg7ULf3hQ3s7EV-5P4MzAHj0O0_kYgXS3MnRZWrs8UMyWzKUobvYOWICvhDsO0KEybrNIOyFtGEHNfKdzM5ygDKHUjI1PagJxdDtDCPEYIsmFOa5utaT5rqMtuAIVKqipY"
REDIRECT_URI = "http://127.0.0.1:8080/callback"

r = requests.post(
    "https://accounts.spotify.com/api/token",
    auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
    data={
        "grant_type": "authorization_code",
        "code": CODE,
        "redirect_uri": REDIRECT_URI,
    },
)

print(r.status_code)
print(r.text)