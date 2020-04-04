from flask import Flask, request
from requests import post
import json, re

# Global variables
url_base = 'http://192.168.1.106:8080/' # jacamo-rest address
my_address = 'http://127.0.0.1:5000'
id = 1
name = 'a'
# --- FUNCTIONS ---
def create_agent():
    endpoint = 'agents/proxy'
    url = url_base + endpoint
    response = post(url)
    name = re.findall(r"'([^']*)'", response.text)[0]
    return name

print(name+str(id))
id +=1
print(name+str(id))
id +=1
print(name+str(id))

# my_name = create_agent()
# print('MY NAME = ', my_name)
# msg2 = create_msg(my_name, 'bob', 'achieve', 'start(a7, "beer")', msg_id)
# send_msg(msg2,'bob') # ask auctioneer (bob) to start a new auction
# msg_id += 1
