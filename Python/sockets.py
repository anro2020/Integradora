'''
import json
from websocket import create_connection

ws = create_connection("ws://invernanderointeligente.herokuapp.com/adonis-ws")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
result = ws.recv()
print("Received '%s'" % result)
ws.send(json.dumps({
"t":1,
"d":{
"topic":"chat",
"event":"message",
"data":"putoss"
}
}))



result = ws.recv()
result = json.loads(result)
ws.send(json.dumps({
"t":7,
"d":{
"topic":"chat",
"event":"message",
"data":"14"
}
}))
print("Received '%s'")


ws.send(json.dumps({
"t":7,
"d":{
"topic":"chat",
"event":"message",
"data":"Soy luisangel"
}
}))
print("Received '%s'")'''

import json
from websocket import create_connection
ws = create_connection("ws://invernanderointeligente.herokuapp.com/adonis-ws")


ws.send(json.dumps({
"t":1,
"d":{
"topic":"chat",
"event":"message",
"data":"putoss"
}
}))
result = ws.recv()
result = json.loads(result)
ws.send(json.dumps({
"t":7,
"d":{
"topic":"chat",
"event":"message",
"data":"14"
}
}))

ws.send(json.dumps({
"t":7,
"d":{
"topic":"chat",
"event":"message",
"data":"EDUARDO Y LUIS NOBIOS"
}
}))
print("Received '%s'")