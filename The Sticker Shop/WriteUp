# **Step 1:** Reconnaissance with Nmap

--> Command: nmap -sS -sV -sC -A -T4 IP

![Screenshot from 2024-12-13 21-48-31](https://github.com/user-attachments/assets/2bb6f193-c5aa-46a5-b53c-dc59a0ea16f1)


# **Step 2**: Exploring the Website

--> The website was analyzed and we found a feedback endpoint that could be vulnerable to something.

--> Attempting an HTML injection if it is enabled, we can use stored XSS to obtain flag.txt.

-->I f we add the /flag.txt file to the website, we'll find out that we're not allowed.

--> To determine if the feedback is vulnerable, we intercept the request and examine if we have received a get request to our server.

![Screenshot from 2024-12-13 21-22-13](https://github.com/user-attachments/assets/169d22ea-2e6b-4a6c-b218-e19817e228af)



--> We have received the request, which means that the endpoint is vulnerable.

![Screenshot from 2024-12-13 21-38-07](https://github.com/user-attachments/assets/206b2ffa-4818-45b9-8269-072b58b09e9f)



# **Step 3 : Exploit**


--> We are left with the task of intercepting the request again and using our script to obtain the flag.

![Screenshot from 2024-12-13 17-59-53](https://github.com/user-attachments/assets/4b75d74f-0a96-43cc-9e7d-add22242c694)



--> after a few seconds we got the flag
