---
name: 🔍 Checklist de Revisão por Pares (Reviewer Checklist)
description: Template do processo de revisão por pares aberta da RBCS para ser preenchido pelos revisores.
title: "[Revisão]: "
labels: ["review", "in-review"]
---

# Processo Editorial e Revisão por Pares — RBCS
**Revista Brasileira de Computação e Software Científico**

- **Artigo / Software**: <!-- Nome do Software -->
- **Repositório**: <!-- URL do Repositório -->
- **Versão sob Revisão**: <!-- Tag / Release -->
- **Editor Responsável**: <!-- @editor -->
- **Revisores Designados**: <!-- @revisor1, @revisor2 -->

---

## 📋 Instruções aos Revisores
A revisão por pares na RBCS é aberta, colaborativa e pública. O objetivo é assegurar o rigor científico, a facilidade de instalação e a reprodutibilidade do software.
Marque as caixas de seleção (`[x]`) conforme for validando cada item. Utilize os comentários deste issue para dialogar com os autores e solicitar correções ou esclarecimentos.

---

## Checklist de Avaliação — Revisor 1 (@username)

### 1. Licença & Repositório
- [ ] **Licença Aberta**: O repositório contém um arquivo `LICENSE` com uma licença de código aberto reconhecida pela [OSI](https://opensource.org/licenses).
- [ ] **Acesso ao Código**: O código-fonte está completo, versionado e disponível publicamente no GitHub.
- [ ] **Versionamento**: O software possui uma tag de versão clara (ex: `v1.0.0`).

### 2. Documentação e Instalação
- [ ] **Guia de Instalação**: Existem instruções claras e completas de instalação em um ambiente limpo (ex: via `pip`, `conda`, `docker`, `cargo`, etc.).
- [ ] **Instalação Funcional**: O revisor conseguiu instalar o software com sucesso seguindo rigorosamente as instruções da documentação.
- [ ] **Dependências**: Todas as dependências externas e versões mínimas requeridas estão especificadas.
- [ ] **Exemplos de Uso**: Há um tutorial básico (*Quickstart*) ou exemplos reproduzíveis de uso com dados de demonstração.

### 3. Funcionalidade & Testes
- [ ] **Suíte de Testes**: O repositório contém testes automatizados (testes unitários e/ou testes de integração).
- [ ] **Execução dos Testes**: Os testes puderam ser executados com sucesso pelo revisor e passaram sem falhas.
- [ ] **Tratamento de Erros**: O software lida adequadamente com entradas inválidas e apresenta mensagens de erro informativas.

### 4. Manutenção e Boas Práticas
- [ ] **Diretrizes de Contribuição**: O repositório possui diretrizes para colaboração (`CONTRIBUTING.md`) ou orientações claras para abertura de *issues* e *pull requests*.
- [ ] **Código Limpo**: O código está organizado, legível e documentado com comentários ou docstrings.

### 5. Conteúdo do Artigo (`paper.md` e `paper.bib`)
- [ ] **Declaração de Necessidade (*Statement of Need*)**: O artigo explica claramente por que o software foi desenvolvido e qual problema científico ele resolve.
- [ ] **Público-Alvo**: O público acadêmico-científico beneficiado pela ferramenta está bem delineado.
- [ ] **Estado da Arte**: O texto cita e compara brevemente o software com outras soluções existentes na literatura científica.
- [ ] **Referências Bibliográficas**: O arquivo `paper.bib` contém referências completas, válidas e com DOIs/links quando disponíveis.
- [ ] **Compilação**: O PDF gerado via Inara está livre de erros de formatação e os metadados (autores, afiliações, orcid) estão corretos.

---

## 💬 Comentários e Parecer Geral do Revisor

<!-- Descreva aqui seus comentários qualitativos, sugestões de melhoria ou pontos que necessitam de ajustes pelos autores -->

---

## ⚖️ Recomendação Editorial (Preenchido pelo Editor)
- [ ] **Aprovado para Publicação**: Todos os itens foram atendidos e verificados.
- [ ] **Revisão Requerida**: Aguardando respostas e ajustes dos autores nos itens apontados acima.
- [ ] **Recusado / Fora de Escopo**: O software não atende aos critérios fundamentais de escopo ou qualidade.
