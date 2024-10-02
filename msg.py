class MSGTYPES:
    REQUEST = 'req'
    INFO = 'info'
    RESPONSE = 'res'

class MSG_REQ:
    JOIN = 'JOIN'

class MSG_RES:
    OK = 'OK'
    STARTED = "STARTED"


def mkmsg( msg, type: MSGTYPES, encode=True ):
    msg = F'{type}|{msg}'
    if encode:
        return msg.encode()
    return msg

def decouple(msg: (bytes|str)) -> tuple[MSGTYPES, str]:
    if isinstance(msg, bytes):
        msg = msg.decode()
    type, msg = msg.split('|')
    return type, msg

