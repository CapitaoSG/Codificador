import os
import random
from pathlib import Path

import base64_codec
from cesar import cesar

mensagem = os.environ.get("MENSAGEM", "").strip()
tipo = os.environ.get("TIPO", "").strip() or "cesar"

if mensagem:
    original = mensagem
else:
    original = Path("entrada/mensagem.txt").read_text(encoding="utf-8")

chave = "não se aplica"

if tipo == "cesar":
    chave = random.randint(1, 25)
    codificado = cesar(original, chave)
elif tipo == "base64":
    codificado = base64_codec.codificar(original)
else:
    raise SystemExit(f"Tipo de codificação desconhecido: {tipo}")

Path("saida/mensagem_codificada.txt").write_text(codificado, encoding="utf-8")
Path("saida/mensagem_original.txt").write_text(original, encoding="utf-8")
Path("saida/chave.txt").write_text(str(chave), encoding="utf-8")
Path("saida/tipo.txt").write_text(tipo, encoding="utf-8")

print("Tipo de codificação:", tipo)
print("Texto original:", original)
print("Chave:", chave)
print("Texto codificado:", codificado)