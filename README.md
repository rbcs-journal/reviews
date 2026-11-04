# 🔍 RBCS Reviews — Repositório de Revisão por Pares Aberta
### *The JOSS-style Editorial Engine for RBCS*

Bem-vindo ao repositório de revisão editorial da **Revista Brasileira de Computação e Software Científico (RBCS)**.

Este repositório é o núcleo operacional da revista. Aqui, todo o processo de submissão, triagem (*pre-review*), revisão por pares e recomendação de aceite é conduzido publicamente através de **GitHub Issues**, apoiado por robôs e GitHub Actions automatizadas idênticas ao fluxo do **JOSS (*Journal of Open Source Software*)**.

---

## 🚀 Como Submeter um Artigo

1. Vá para a aba **[Issues](https://github.com/rbcs-journal/reviews/issues)**.
2. Clique no botão verde **"New Issue"**.
3. Selecione o template **"📝 Nova Submissão de Software"**.
4. Preencha as informações do repositório, versão, autores e trilha editorial.

Assim que o issue for criado, a **Auditoria Automática de Submissão** será disparada imediatamente para analisar a conformidade do repositório.

---

## 🛠️ Comandos Automatizados nos Issues (JOSS Actions & Bot)

Autores, revisores e editores podem interagir com os robôs e com as GitHub Actions nos comentários dos issues:

| Comando | Descrição | O que a Action faz? |
| :--- | :--- | :--- |
| `/check-repository`<br>`@rbcs-bot check repository` | **Auditoria Geral do Repositório** | Clona o repositório do autor e verifica: Licença OSI (`LICENSE`), estrutura do `paper.md`, seção `# Statement of Need`, contagem de palavras, metadados ORCID, suíte de testes (`tests/`), automação de CI (GitHub Actions) e `README.md`. |
| `/check-references`<br>`@rbcs-bot check references` | **Validação Bibliográfica e DOIs** | Lê o `paper.bib`, analisa cada entrada e consulta a API da Crossref/DOI para checar se todos os DOIs existem e estão ativos. |
| `/compile-pdf`<br>`@rbcs-bot generate pdf` | **Compilação do PDF Oficial** | Executa o container Docker oficial do **Inara** (`openjournals/inara:latest`), gerando o PDF do artigo, JATS XML e metadados Crossref para download imediato. |
| `@rbcs-bot assign @editor as editor` | **Designação de Editor** | O bot atribui o editor de trilha ao issue e atualiza as etiquetas. |
| `@rbcs-bot add @revisor as reviewer` | **Adicionar Revisor** | Envia mensagem formal de boas-vindas e checklist ao revisor. |
| `@rbcs-bot recommend accept` | **Recomendação de Aceite** | Marca o artigo com a etiqueta `recommend-accept` para homologação e depósito de DOI. |

---

## 📚 Documentação e Políticas

* 🇧🇷 [Diretrizes para Autores](docs/author_guidelines.md)
* 🇺🇸 [Author Guidelines (English)](docs/author_guidelines_en.md)
* 🇪🇸 [Directrices para Autores (Español)](docs/author_guidelines_es.md)
* [Diretrizes para Revisores](docs/reviewer_guidelines.md)
* [Código de Conduta](https://github.com/rbcs-journal/.github/blob/main/CODE_OF_CONDUCT.md)
