import base64

def codificar (texto):
    return base64.b64encode(texto.encode("utf-8")).decode("ascii")