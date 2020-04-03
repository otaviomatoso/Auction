from requests import post, get, put
import os, json, time
from random import randint, uniform
############

def createAgent(agent):
    print(f'Creating agent {agent}')
    endpoint = f'agents/{agent}'
    url = url_base + endpoint
    req = post(url)
    print(req.text)

def createMsg(sender,receiver,performative,content,msgId):
    msg = json.dumps({"sender": f"{sender}", "receiver": f"{receiver}", "performative": f"{performative}", "content": f"{content}", "msgId": f"{msgId}"})
    return msg

def sendMsg(message, agent):
    endpoint = f'agents/{agent}/mb'
    url = url_base + endpoint
    headers = {'Content-Type':'application/json'}
    post(url, headers=headers, data=message)

def getPlans(agent):
    endpoint = f'agents/{agent}/plans'
    url = url_base + endpoint
    req = get(url)
    return req.text

def postPlans(agent, plans):
    print(f'\nSending plans to agent {agent}...')
    endpoint = f'agents/{agent}/plans'
    url = url_base + endpoint
    currentDir = os.getcwd()
    filePath = currentDir + '\plan'
    files = {'file': open(filePath)} # Why is it necessary?
    payload = {'plans': plans}
    req = post(url, files=files, data=payload)
    print(req.text)

def getBeliefs(agent):
    endpoint = f'agents/{agent}/mind/bb'
    url = url_base + endpoint
    req = get(url)
    return req.text

def execOp(ws, art, op, args):
    endpoint = f'workspaces/{ws}/{art}/operations/{op}'
    url = url_base + endpoint
    headers = {'Content-Type':'application/json'}
    put(url, headers=headers, data=args)

def getObsProps(ws, art, obsProps):
    endpoint = f'workspaces/main/a1/obsprops/{obsProps}'
    url = url_base + endpoint
    req = get(url)
    return req.text



print('Starting...\n')
url_base = 'http://192.168.1.106:8080/'
myName = 'python'
# execOp("main", "a1", "bid", "[7]")
prop = getObsProps("main", "a1", "winner")
print(f'OBS PROPS = {prop}')
name = json.loads(prop)[0]["functor"]
# print(f'OBS PROPS = {propJson["functor"]}')
print(f'NAME = {name}')
