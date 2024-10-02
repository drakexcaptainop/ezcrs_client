import shutil as sh 
from car import car 
from cons import out 
import time 
from cdata import start_client, global_manager, cars_wrapper, lock_till_game_start, request_join, init_client_socket


def recv_car_info():
    pass 

     

init_client_socket()

h = sh.get_terminal_size().lines
w = sh.get_terminal_size().columns 

wr = out(w, h)

c1 = car( 2, 2, 1, 0, 0 )

if not request_join():
    exit(1)
else:
    lock_till_game_start()

dt = 1 
pt = time.time( )



ellapsed = 0
while 1:
    ct = time.time()
    dt = ct - pt 
    pt = ct 
    ellapsed += dt 

    if ellapsed >= 16.66/1000:
        wr.clear_car(c1)    
        c1.step(1)
        wr.set_car(c1)
        wr.print_buffer()
        ellapsed = 0

    if global_manager.has_plyrs():
        c: car 
        for c in global_manager.get_iter():
            wr.clear_car()
            c.step()
            wr.set_car( c )
            wr.print_buffer(  )
    





