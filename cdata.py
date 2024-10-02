import threading 
import socket
import json 
from msg import MSGTYPES, mkmsg, decouple, MSG_REQ, MSG_RES

    


sock = None
client_thread = None

def init_client_socket():
    global sock, client_thread
    sock = socket.socket()
    sock.connect( ( input("SERVER IP (X.X.X.X): ", int(input("SERVER PORT: "))) ) )
    client_thread = threading.Thread( target=recv )

class cars_wrapper( ):
    def __init__(self) -> None:
        self.cars = []
    
    def set(self,cars):
        self.cars = cars  

    def get_iter(self):
        return iter( self.cars )

    def has_plyrs(self):
        return len(self.cars)
    
global_manager = cars_wrapper()



def request_join():
    sock.send(mkmsg(MSG_REQ.JOIN, MSGTYPES.REQUEST))
    if sock.recv( 64 ).decode() == MSG_RES.OK:
        return True
    return False

def encode_json(_car):
    data = _car.json().encode()
    return data

def decode( data: (bytes | str) ):
    if isinstance(data, bytes):
        inf = data.decode()
    else:
        inf = data
    cars = json.loads( inf )
    return cars

def send_client_info( car ):
    data = encode_json( car )
    sock.send( mkmsg( data, MSGTYPES.INFO ) )


def lock_till_game_start():
    STARTED = False
    while not STARTED:
        data = sock.recv( 128 ).decode() 
        mtype, msg = decouple(data)
        if mtype == MSGTYPES.RESPONSE:
            STARTED = msg == MSG_RES.STARTED



def recv():
    while True:
        data = sock.recv( 1024 )
        cars = decode( data )
        global_manager.set( cars )



def start_client():
    client_thread.start() 



