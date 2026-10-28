def cesar(texto, deslocamento):
    resultado = ""
    for letra in texto:
        if letra.isascii() and letra.isalpha():
            base = ord("A") if letra.isupper() else ord("a")
            resultado += chr((ord(letra) - base + deslocamento) % 26 + base)
        else:
            resultado += letra
    return resultado