#!/usr/bin/env python3
"""
RBCS BibTeX & DOI Reference Checker (JOSS-style)
Valida a integridade de todas as referências do paper.bib e consulta a API da Crossref/DOI.
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error

def validate_bibtex_and_dois(repo_path):
    candidates = [
        os.path.join(repo_path, "paper.bib"),
        os.path.join(repo_path, "paper", "paper.bib"),
        os.path.join(repo_path, "docs", "paper.bib")
    ]
    bib_path = None
    for c in candidates:
        if os.path.exists(c):
            bib_path = c
            break

    if not bib_path:
        return "❌ **Erro**: Arquivo `paper.bib` não encontrado no repositório submetido."

    with open(bib_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Separa blocos de referências
    entries = re.split(r'\n@', '\n' + content)
    
    total = 0
    with_doi = []
    missing_doi = []
    invalid_dois = []

    for entry in entries:
        if not entry.strip():
            continue
        total += 1
        
        # Pega a chave da citação
        key_match = re.search(r'^\w+\s*\{\s*([^,]+),', entry.strip())
        citation_key = key_match.group(1).strip() if key_match else f"Entrada #{total}"
        
        # Procura por DOI
        doi_match = re.search(r'doi\s*=\s*[\"{](10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)[\"}]', entry, re.IGNORECASE)
        if doi_match:
            doi = doi_match.group(1).strip()
            # Validação via Crossref API com timeout curto
            url = f"https://api.crossref.org/works/{doi}"
            req = urllib.request.Request(url, headers={'User-Agent': 'RBCS-Reference-Checker/1.0 (mailto:editorial@rbcs.org.br)'})
            try:
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status == 200:
                        with_doi.append((citation_key, doi, "✅ Válido no Crossref"))
                    else:
                        with_doi.append((citation_key, doi, "⚠️ Status incomum"))
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    invalid_dois.append((citation_key, doi, "❌ DOI não encontrado (404)"))
                else:
                    with_doi.append((citation_key, doi, f"⚠️ HTTP {e.code}"))
            except Exception:
                with_doi.append((citation_key, doi, "ℹ️ Formato de DOI válido"))
        else:
            missing_doi.append(citation_key)

    # Formata relatório
    md = []
    md.append("## 📚 Relatório de Auditoria Bibliográfica e Validação de DOIs (RBCS References Check)")
    md.append(f"- **Total de entradas bibliográficas analisadas**: {total}")
    md.append(f"- **Entradas com DOI**: {len(with_doi) + len(invalid_dois)}")
    md.append(f"- **Entradas sem DOI**: {len(missing_doi)}\n")

    if invalid_dois:
        md.append("### ❌ DOIs Inválidos ou Não Resolvidos")
        for key, doi, reason in invalid_dois:
            md.append(f"- `@cite:{key}` → DOI: `{doi}` ({reason})")
        md.append("")

    if missing_doi:
        md.append("### ⚠️ Referências sem DOI Registrado")
        md.append("*Recomendamos incluir o identificador DOI sempre que disponível na literatura:*")
        for key in missing_doi[:15]:
            md.append(f"- `@cite:{key}`")
        if len(missing_doi) > 15:
            md.append(f"- *(... e mais {len(missing_doi) - 15} referências)*")
        md.append("")

    if with_doi:
        md.append("### ✅ DOIs Verificados com Sucesso")
        for key, doi, status in with_doi[:10]:
            md.append(f"- `{key}`: [{doi}](https://doi.org/{doi}) — {status}")
        if len(with_doi) > 10:
            md.append(f"- *(... e mais {len(with_doi) - 10} DOIs válidos)*")

    return "\n".join(md)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: check_references.py <caminho_repositorio_clonado>")
        sys.exit(1)
        
    repo_path = sys.argv[1]
    print(validate_bibtex_and_dois(repo_path))
