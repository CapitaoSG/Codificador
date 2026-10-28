from pathlib import Path

DESLOCAMENTO = 3

def cesar(texto, deslocamento):
    resultado = ""
    for letra in texto:
        if letra.isascii() and letra.isalpha():
            base = ord("A") if letra.isupper() else ord("a")
            resultado += chr((ord(letra) - base + deslocamento) % 26 + base)
        else:
            resultado += letra
    return resultado


original = Path("entrada/mensagem.txt").read_text(encoding="utf-8")
codificado = cesar(original, DESLOCAMENTO)

Path("saida/mensagem_codificada.txt").write_text(codificado, encoding="utf-8")

print("Texto original:", original)
print("Texto codificado:", codificado)