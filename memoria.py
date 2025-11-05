import json, os, re

arquivo = "memoria.json"

def carregar():
    if not os.path.exists(arquivo):
        return {"lembrancas": []}
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar(memoria):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=2)

def gravar_info(tipo, valor):
    """Guarda uma lembrança com tipo e valor."""
    memoria = carregar()
    memoria.setdefault("lembrancas", []).append({"tipo": tipo, "valor": valor})
    salvar(memoria)

def mostrar_lembrancas():
    memoria = carregar()
    return memoria.get("lembrancas", [])

def formatar_lembrancas():
    """Gera respostas amigáveis para cada tipo de lembrança."""
    respostas = []
    for item in mostrar_lembrancas():
        if item["tipo"] == "nome":
            respostas.append(f"Ah, seu nome é {item['valor']}, certo?")

        elif item["tipo"] == "cidade":
            respostas.append(f"Você mora em {item['valor']}.")
        else:
            respostas.append(f"Lembro que {item['valor']}.")
    return respostas


def extrair_info(frase: str) -> dict:
    info = {}

    # --- Nome ---
    nome_match = re.search(r"(?:meu nome é|eu me chamo|chamo-me)\s+([A-ZÁÉÍÓÚÇ][a-záéíóúç]+(?:\s[A-ZÁÉÍÓÚÇ][a-záéíóúç]+)*)", frase, re.IGNORECASE)
    if nome_match:
        nome = nome_match.group(1)
        # Para antes de palavras-chave que indicam outras infos
        nome = re.split(r'\b(tenho|moro|sou|trabalho|,|e)\b', nome, flags=re.IGNORECASE)[0].strip()
        info['nome'] = nome

    # --- Idade ---
    idade_match = re.search(r"\btenho\s+(\d{1,3})\s+anos?\b", frase, re.IGNORECASE)
    if idade_match:
        info['idade'] = int(idade_match.group(1))

    # --- Cidade ---
    cidade_match = re.search(r"(?:moro em|moro no|resido em|cidade é)\s+(.+?)(?=\s+e\s+|\s+tenho\s+|\s+sou\s+|$|,)", frase, re.IGNORECASE)
    if cidade_match:
        info['cidade'] = cidade_match.group(1).strip()

    # --- Profissão ---
    profissao_match = re.search(r"(?:sou|trabalho como|profissão é)\s+([a-zA-Záéíóúç\s]+?)(?=\s+e\s+|\s+tenho\s+|\s+meu nome|$|,)", frase, re.IGNORECASE)
    if profissao_match:
        profissao = profissao_match.group(1).strip()
        info['profissao'] = profissao

    return info

def limpar_lembrancas():
    salvar({"lembrancas": []})
    return ""
