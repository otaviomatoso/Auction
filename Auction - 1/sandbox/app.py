from flask import Flask, request
from requests import post, put
import json
from random import randint, uniform

app = Flask(__name__)

# Global variables
url_base = 'http://192.168.1.106:8080/' # jacamo-rest address
my_name = 'python'
my_address = 'http://127.0.0.1:5000'
id = 1
task = ''
offer = 0

# --- FUNCTIONS ---

def wp_register(name, address):
    body = json.dumps({"agentid": f"{name}", "uri": f"{address}"})
    endpoint = 'wp'
    url = url_base + endpoint
    headers = {'Content-Type':'application/json'}
    post(url, headers=headers, data=body)

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
    if (literal['functor'] == 'focus'):
        art_name = literal["args"]
        print(f'\nARTNAME = {art_name}')
        endpoint = f'workspaces/market_place/{art_name}/operations/bid'
        url = url_base + endpoint
        value = f'[{uniform(0, 10)}]'
        print(f'\nMY PROPOSAL = {value}')
        headers = {'Content-Type':'application/json'}
        put(url, headers=headers, data=value)

# --- MAIN ---
print('\nRegistering myself at WP...')
wp_register(my_name, my_address)

# Mailbox to receive messages from agents
# PS.: When agent acts as client, the path '/mb'
#      is added at the end of the endpoint
@app.route('/mb', methods=['POST'])
def mailBox():
    # print("ENTROU NA MAILBOX")
    msg = json.loads(request.data)
    sender = msg['sender']
    content = msg['content']
    # print(f'\nI have just received a message from {sender} with the content = {content}')
    literal = process_content(content)
    process_msg(literal, sender)
    return ''
