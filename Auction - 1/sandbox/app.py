from flask import Flask, request
from requests import post
import json, re

app = Flask(__name__)

# Global variables
url_base = 'http://192.168.1.106:8080/' # jacamo-rest address
my_address = 'http://127.0.0.1:5000'
msg_id = 1
price = 30

# --- FUNCTIONS ---
def create_agent(name):
    print(f'Creating agent {name}')
    endpoint = f'agents/{name}'
    url = url_base + endpoint
    req = post(url)
    return req.text

def create_msg(sender,receiver,performative,content,msgId):
    msg = json.dumps({"sender": f"{sender}", "receiver": f"{receiver}", "performative": f"{performative}", "content": f"{content}", "msgId": f"{msgId}"})
    return msg

def send_msg(message, agent):
    endpoint = f'agents/{agent}/mb'
    url = url_base + endpoint
    headers = {'Content-Type':'application/json'}
    post(url, headers=headers, data=message)

def process_content(content):
    d = dict();
    d['functor'] = content[0:content.find('(')]
    d['args'] = content[len(d['functor'])+1:len(content)-1]
    return d

def process_msg(literal, sender):
    if (literal['functor'] == 'result'):
        res = literal["args"]
        if (res == 'win'):
            print('I WON THE AUCTION!!!')
        elif (res == 'loss'):
            print('I LOST THE AUCTION!!!')

reply = create_agent('proxy')
# Regex is used to get the name of the created agent.
# The name is in the API response, in single quotes.
# If more than one agent is created using the same name,
# the given names are as follows: name, name_1, name_2, name_3,...
my_name = re.findall(r"'([^']*)'", reply)[0] # The result is a list, so the name is at index 0.
print(f'MY NAME = {my_name}')

msg = create_msg(my_name, my_name, 'tell', f'offer({price},\"{my_address}\")', msg_id)
send_msg(msg,my_name) # tell the agent my 'offer(price,address)''
msg_id += 1
msg2 = create_msg(my_name, 'bob', 'achieve', 'start(a7, "beer")', msg_id)
send_msg(msg2,'bob') # ask auctioneer (bob) to start a new auction
msg_id += 1

@app.route('/mb', methods=['POST'])
def mailBox():
    msg = json.loads(request.data)
    sender = msg['sender']
    content = msg['content']
    literal = process_content(content)
    process_msg(literal, sender)
    return ''
