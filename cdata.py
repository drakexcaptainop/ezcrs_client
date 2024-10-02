import threading 
import socket
import json 
from msg import MSGTYPES, mkmsg, decouple

    


sock = socket.socket()
sock.connect( ( input("SERVER IP (X.X.X.X): ", int(input("SERVER PORT: "))) ) )

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
    sock.send(mkmsg("join", MSGTYPES.REQUEST))
    if sock.recv( 64 ).decode() == 'OK':
        return True
    return False


def decode( data: bytes ):
    inf = data.decode()
    cars = json.loads( inf )
    return cars

def lock_till_game_start():
    STARTED = False
    while not STARTED:
        data = sock.recv( 128 ).decode() 
        mtype, msg = decouple(data)
        if mtype == MSGTYPES.RESPONSE:
            STARTED = msg == "STARTED"

def recv():
    while True:
        data = sock.recv( 1024 )
        cars = decode( data )
        global_manager.set( cars )

client_thread = threading.Thread( target=recv )

def start_client():
    client_thread.start() 



