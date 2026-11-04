# Diretrizes para Autores — RBCS

A **Revista Brasileira de Computação e Software Científico (RBCS)** adota o modelo de publicação focado no software e na sua reprodutibilidade.

## 1. Critérios de Elegibilidade

Para ser publicado na RBCS, o trabalho deve atender a todos os seguintes requisitos:
* **Código Aberto**: O software deve estar sob licença de código aberto aprovada pela [OSI](https://opensource.org/licenses/) (ex: MIT, Apache 2.0, GPL 3.0, BSD).
* **Hospedado no GitHub**: O repositório deve ser público.
* **Contribuição Científica**: O software deve ter uma aplicação clara para pesquisa científica (computação geral, bioinformática, informática médica ou ciência de dados).
* **Software Funcional e Testado**: O repositório deve incluir instruções reproduzíveis de instalação e uma suíte de testes funcionais.

---

## 2. Estrutura dos Arquivos do Artigo

O repositório do autor deve conter os arquivos `paper.md` e `paper.bib` na raiz ou no diretório `paper/`.

### Exemplo de `paper.md`
```markdown
---
title: 'PyBioFast: Uma biblioteca de alto desempenho para análise genômica'
tags:
  - Python
  - Bioinformática
  - Genômica
  - Sequenciamento
authors:
  - name: Maria Silva
    orcid: 0000-0002-1825-0097
    affiliation: 1
  - name: João Santos
    orcid: 0000-0001-5727-2427
    affiliation: "1, 2"
affiliations:
 - name: Universidade de São Paulo (USP), Brasil
   index: 1
 - name: Instituto de Bioinformática, Brasil
   index: 2
date: 4 Novembro 2026
bibliography: paper.bib
---

# Resumo
PyBioFast é uma biblioteca open-source desenvolvida em Python e Rust para acelerar...

# Declaração de Necessidade (Statement of Need)
A crescente geração de dados de sequenciamento de nova geração (NGS) exige...

# Arquitetura e Implementação
O pacote foi estruturado em módulos independentes...

# Comparação com o Estado da Arte
Em comparação com ferramentas como Biopython [@Cock2009]...

# Agradecimentos
Este trabalho foi apoiado pela FAPESP e CNPq...

# Referências
```

### Exemplo de `paper.bib`
```bibtex
@article{Cock2009,
  author = {Cock, Peter J. A. and Antao, Tiago and Chang, Jeffrey T. and Chapman, Brad A. and Cox, Cymon J. and Dalke, Andrew and Friedberg, Iddo and Hamelryck, Thomas and Kauff, Frank and Wilczynski, Bartek and de Hoon, Michiel J. L.},
  title = {Biopython: freely available Python tools for computational molecular biology and bioinformatics},
  journal = {Bioinformatics},
  volume = {25},
  number = {11},
  pages = {1422--1423},
  year = {2009},
  doi = {10.1093/bioinformatics/btp163}
}
```

---

## 3. Como Submeter

1. Acesse a aba **[Issues](https://github.com/rbcs-journal/reviews/issues)** deste repositório.
2. Clique em **New Issue** e selecione o formulário **Nova Submissão de Software**.
3. Preencha os campos solicitados e envie o issue.
4. O processo editorial será conduzido publicamente naquele mesmo issue.
