# Diretrizes para Revisores — RBCS

A revisão por pares na **RBCS** é pública, aberta e conduzida diretamente nos issues do GitHub. O objetivo central é **ajudar os autores a aprimorar o software e garantir a reprodutibilidade científica**.

---

## O Papel do Revisor

Como revisor da RBCS, seu papel não é apenas avaliar o texto descritivo (`paper.md`), mas também atuar como um usuário real do software:

1. **Instalar o software**: Tente instalar o pacote seguindo estritamente as instruções fornecidas no README ou na documentação.
2. **Rodar os testes**: Execute a suíte de testes do repositório (ex: `pytest`, `cargo test`, `npm test`, etc.).
3. **Executar um exemplo prático**: Utilize os dados de exemplo fornecidos pelos autores para verificar se os resultados gerados correspondem ao esperado.
4. **Avaliar o Artigo**: Verifique se a declaração de necessidade (*Statement of Need*) e as referências científicas estão completas e precisas.

---

## Como Interagir

* **Seja Construtivo e Cordial**: Aponte falhas de documentação, bugs ou problemas de instalação como oportunidades de melhoria.
* **Marque os Itens**: À medida que verificar cada ponto, edite o comentário inicial do issue marcando as caixas `[x]`.
* **Discuta Abertamente**: Se encontrar um erro na instalação, copie o *traceback* nos comentários do issue para que os autores possam lançar uma correção (*patch*) ou esclarecer a dúvida.
