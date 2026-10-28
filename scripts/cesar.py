import os
import random
from pathlib import Path


def cesar(texto, deslocamento):
    resultado = ""
    for letra in texto:
        if letra.isascii() and letra.isalpha():
            base = ord("A") if letra.isupper() else ord("a")
            resultado += chr((ord(letra) - base + deslocamento) % 26 + base)
        else:
            resultado += letra
    return resultado

mensagem = os.environ.get("MENSAGEM", "").strip()

if mensagem:
    original = mensagem
else:
    original = Path("entrada/mensagem.txt").read_text(encoding="utf-8")

chave = random.randint(1, 25)
codificado = cesar(original, chave)

Path("saida/mensagem_codificada.txt").write_text(codificado, encoding="utf-8")
Path("saida/chave.txt").write_text(str(chave), encoding="utf-8")

print("Texto original:", original)
print("Deslocamento sorteado:", chave)
print("Texto codificado:", codificado)