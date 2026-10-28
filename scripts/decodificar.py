from pathlib import Path

import base64_codec
from cesar import cesar

original = Path("saida/mensagem_original.txt").read_text(encoding="utf-8")
codificado = Path("saida/mensagem_codificada.txt").read_text(encoding="utf-8")
chave = Path("saida/chave.txt").read_text(encoding="utf-8").strip()
tipo = Path("saida/tipo.txt").read_text(encoding="utf-8").strip()

if tipo == "cesar":
    decodificado = cesar(codificado, -int(chave))
elif tipo == "base64":
    decodificado = base64_codec.decodificar(codificado)
else:
    raise SystemExit(f"Tipo de codificação desconhecido: {tipo}")

Path("saida/mensagem_decodificada.txt").write_text(decodificado, encoding="utf-8")

print("Tipo de codificação:", tipo)
print("Texto codificado:", codificado)
print("Texto decodificado:", decodificado)

if decodificado == original:
    print("OK: o texto decodificado é igual ao original")
else:
    raise SystemExit("ERRO: o texto decodificado é diferente do original")