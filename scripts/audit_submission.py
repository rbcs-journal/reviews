#!/usr/bin/env python3
"""
RBCS Automated Submission & Repository Auditor (JOSS-style)
Analisa o repositório do autor submetido à RBCS:
1. Licença Open Source (OSI)
2. Artigo (paper.md, frontmatter, Statement of Need, contagem de palavras)
3. Referências (paper.bib, integridade BibTeX, checagem de DOIs)
4. Código & Métricas de Linguagem
5. Suíte de Testes e CI (GitHub Actions)
6. Documentação e Diretrizes de Comunidade
"""

import os
import re
import sys
import glob
import json
import urllib.request
import urllib.error

def check_license(repo_path):
    license_files = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "COPYING"]
    found = None
    for f in license_files:
        p = os.path.join(repo_path, f)
        if os.path.exists(p):
            found = p
            break
            
    if not found:
        return {"status": "FAIL", "msg": "Arquivo de licença (LICENSE) não encontrado na raiz do repositório."}
        
    try:
        with open(found, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()
            
        detected = "Desconhecida"
        if "mit license" in content or "permission is hereby granted, free of charge" in content:
            detected = "MIT"
        elif "apache license" in content or "apache.org/licenses" in content:
            detected = "Apache-2.0"
        elif "gnu general public license" in content or "gpl" in content:
            detected = "GPL"
        elif "bsd" in content:
            detected = "BSD"
        elif "mozilla public license" in content:
            detected = "MPL-2.0"
            
        return {"status": "PASS", "license": detected, "file": os.path.basename(found), "msg": f"Licença detectada: **{detected}** (em `{os.path.basename(found)}`)."}
    except Exception as e:
        return {"status": "WARN", "msg": f"Erro ao ler arquivo de licença: {str(e)}"}

def check_paper(repo_path):
    candidates = [
        os.path.join(repo_path, "paper.md"),
        os.path.join(repo_path, "paper", "paper.md"),
        os.path.join(repo_path, "docs", "paper.md")
    ]
    paper_path = None
    for c in candidates:
        if os.path.exists(c):
            paper_path = c
            break
            
    if not paper_path:
        return {
            "status": "FAIL",
            "msg": "Arquivo `paper.md` não encontrado na raiz ou no diretório `paper/`."
        }
        
    with open(paper_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Frontmatter YAML
    has_frontmatter = content.startswith("---")
    frontmatter_text = ""
    body_text = content
    if has_frontmatter:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1]
            body_text = parts[2]

    # Checa título, autores e afiliações
    has_title = bool(re.search(r"^title\s*:", frontmatter_text, re.MULTILINE))
    has_authors = bool(re.search(r"^authors\s*:", frontmatter_text, re.MULTILINE))
    has_affiliations = bool(re.search(r"^affiliations\s*:", frontmatter_text, re.MULTILINE))
    has_orcid = "orcid:" in frontmatter_text

    # Declaração de Necessidade (Statement of Need)
    need_pattern = re.compile(r"#+\s*(statement\s+of\s+need|declaração\s+de\s+necessidade|declaración\s+de\s+necesidad)", re.IGNORECASE)
    has_need = bool(need_pattern.search(body_text))

    # Contagem de palavras do corpo (sem código)
    text_clean = re.sub(r"```[\s\S]*?```", "", body_text)
    words = len(re.findall(r"\b\w+\b", text_clean))
    
    word_status = "PASS"
    if words < 200:
        word_status = "WARN (Muito curto, < 200 palavras)"
    elif words > 2000:
        word_status = "WARN (Muito longo, > 2000 palavras; JOSS recomenda texto conciso)"

    return {
        "status": "PASS",
        "path": os.path.relpath(paper_path, repo_path),
        "has_frontmatter": has_frontmatter,
        "has_title": has_title,
        "has_authors": has_authors,
        "has_affiliations": has_affiliations,
        "has_orcid": has_orcid,
        "has_statement_of_need": has_need,
        "word_count": words,
        "word_status": word_status
    }

def check_bibliography(repo_path, paper_info):
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
        return {"status": "FAIL", "msg": "Arquivo `paper.bib` não encontrado."}

    with open(bib_path, "r", encoding="utf-8", errors="ignore") as f:
        bib_content = f.read()

    entries = re.findall(r"@(\w+)\s*\{\s*([^,]+),", bib_content)
    dois = re.findall(r"doi\s*=\s*[\"{](10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)[\"}]", bib_content, re.IGNORECASE)

    return {
        "status": "PASS",
        "file": os.path.relpath(bib_path, repo_path),
        "total_entries": len(entries),
        "entries_with_doi": len(dois),
        "entry_keys": [e[1].strip() for e in entries[:10]]
    }

def check_code_and_tests(repo_path):
    # Detecta linguagens e extensões comuns
    extensions = {
        "Python": [".py"],
        "R": [".r", ".R"],
        "C/C++": [".c", ".cpp", ".cc", ".h", ".hpp"],
        "Rust": [".rs"],
        "Julia": [".jl"],
        "Java/Kotlin": [".java", ".kt"],
        "JavaScript/TypeScript": [".js", ".ts"]
    }
    
    lang_counts = {lang: 0 for lang in extensions}
    total_source_files = 0

    for root, dirs, files in os.walk(repo_path):
        if ".git" in root or "node_modules" in root or "venv" in root or "__pycache__" in root:
            continue
        for file in files:
            ext = os.path.splitext(file)[1]
            for lang, exts in extensions.items():
                if ext in exts:
                    lang_counts[lang] += 1
                    total_source_files += 1

    main_languages = [f"{lang} ({cnt} arquivos)" for lang, cnt in lang_counts.items() if cnt > 0]

    # Testes
    test_dirs = ["test", "tests", "spec", "specs", "testing", "unit_tests"]
    has_test_dir = any(os.path.exists(os.path.join(repo_path, td)) for td in test_dirs)
    
    test_files = []
    for root, dirs, files in os.walk(repo_path):
        if ".git" in root:
            continue
        for f in files:
            if f.startswith("test_") or f.endswith("_test.py") or f.endswith("_test.go") or f.endswith("Test.java"):
                test_files.append(f)

    # CI (GitHub Actions)
    workflows = glob.glob(os.path.join(repo_path, ".github", "workflows", "*.yml")) + \
                glob.glob(os.path.join(repo_path, ".github", "workflows", "*.yaml"))

    return {
        "languages": main_languages,
        "total_source_files": total_source_files,
        "has_test_suite": has_test_dir or len(test_files) > 0,
        "test_files_count": len(test_files),
        "has_ci": len(workflows) > 0,
        "ci_workflows_count": len(workflows)
    }

def check_docs_and_community(repo_path):
    has_readme = any(os.path.exists(os.path.join(repo_path, f)) for f in ["README.md", "README.rst", "README.txt", "README"])
    has_contributing = any(os.path.exists(os.path.join(repo_path, f)) for f in ["CONTRIBUTING.md", "CONTRIBUTING", ".github/CONTRIBUTING.md"])
    has_docs_dir = any(os.path.exists(os.path.join(repo_path, d)) for d in ["docs", "documentation", "doc"])
    
    return {
        "has_readme": has_readme,
        "has_contributing": has_contributing,
        "has_docs_dir": has_docs_dir
    }

def generate_report(repo_path, repo_url):
    lic = check_license(repo_path)
    paper = check_paper(repo_path)
    bib = check_bibliography(repo_path, paper)
    code = check_code_and_tests(repo_path)
    docs = check_docs_and_community(repo_path)

    # Monta parecer em Markdown (Estilo JOSS Bot)
    md = []
    md.append("## 🤖 Relatório de Auditoria Automática de Submissão (JOSS Automated Checks)")
    md.append(f"> **Repositório auditado**: [{repo_url}]({repo_url})\n")

    # Tabela Resumo
    md.append("| Critério de Verificação | Status | Detalhes |")
    md.append("| :--- | :---: | :--- |")
    
    # 1. Licença
    if lic["status"] == "PASS":
        md.append(f"| **Licença de Código Aberto (OSI)** | ✅ PASS | `{lic['license']}` identificada no arquivo `{lic.get('file', 'LICENSE')}` |")
    else:
        md.append(f"| **Licença de Código Aberto (OSI)** | ❌ FAIL | {lic['msg']} |")

    # 2. Paper.md
    if paper["status"] == "PASS":
        md.append(f"| **Arquivo do Artigo (`paper.md`)** | ✅ PASS | Localizado em `{paper['path']}` |")
        
        # Statement of need
        if paper["has_statement_of_need"]:
            md.append("| **Declaração de Necessidade (*Statement of Need*)** | ✅ PASS | Seção presente no artigo |")
        else:
            md.append("| **Declaração de Necessidade (*Statement of Need*)** | ❌ FAIL | Seção `# Statement of Need` ausente no `paper.md` |")

        # Contagem de palavras
        md.append(f"| **Contagem de Palavras** | ℹ️ INFO | ~{paper['word_count']} palavras ({paper['word_status']}) |")

        # Autores & ORCID
        if paper["has_authors"] and paper["has_orcid"]:
            md.append("| **Metadados de Autores e ORCIDs** | ✅ PASS | Autores e identificadores ORCID presentes no YAML |")
        else:
            md.append("| **Metadados de Autores e ORCIDs** | ⚠️ WARN | Verifique se todos os autores possuem ORCID no cabeçalho YAML |")
    else:
        md.append(f"| **Arquivo do Artigo (`paper.md`)** | ❌ FAIL | {paper['msg']} |")

    # 3. Referências
    if bib["status"] == "PASS":
        md.append(f"| **Bibliografia (`paper.bib`)** | ✅ PASS | {bib['total_entries']} referências ({bib['entries_with_doi']} com DOI) |")
    else:
        md.append(f"| **Bibliografia (`paper.bib`)** | ❌ FAIL | {bib['msg']} |")

    # 4. Código & Métricas
    langs = ", ".join(code["languages"]) if code["languages"] else "Não detectada"
    md.append(f"| **Linguagens e Código-fonte** | ℹ️ INFO | {code['total_source_files']} arquivos ({langs}) |")

    # 5. Testes e CI
    if code["has_test_suite"]:
        md.append(f"| **Suíte de Testes Automatizados** | ✅ PASS | Detectada estrutura de testes ({code['test_files_count']} arquivos) |")
    else:
        md.append("| **Suíte de Testes Automatizados** | ⚠️ WARN | Nenhuma pasta de testes ou arquivo `test_*.py` detectado |")

    if code["has_ci"]:
        md.append(f"| **Integração Contínua (CI / Workflows)** | ✅ PASS | {code['ci_workflows_count']} workflow(s) do GitHub Actions configurados |")
    else:
        md.append("| **Integração Contínua (CI / Workflows)** | ⚠️ WARN | Recomendado configurar GitHub Actions para rodar testes na branch principal |")

    # 6. Documentação
    if docs["has_readme"]:
        md.append("| **Documentação (README)** | ✅ PASS | Arquivo de documentação inicial presente |")
    else:
        md.append("| **Documentação (README)** | ❌ FAIL | `README.md` ausente |")

    md.append("\n---")
    md.append("### 💡 Instruções aos Autores e Editores:")
    md.append("- Autores: Por favor, corrijam qualquer item marcado com ❌ antes do início formal da revisão.")
    md.append("- Para gerar uma prévia em PDF do manuscrito compilado via **Inara**, digite `/compile-pdf` nos comentários.")
    md.append("- Para reexecutar esta auditoria após realizar commits de ajuste, digite `/check-repository`.")

    return "\n".join(md)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: audit_submission.py <caminho_repositorio_clonado> <url_repositorio_autor>")
        sys.exit(1)
        
    repo_path = sys.argv[1]
    repo_url = sys.argv[2]
    
    report = generate_report(repo_path, repo_url)
    print(report)
