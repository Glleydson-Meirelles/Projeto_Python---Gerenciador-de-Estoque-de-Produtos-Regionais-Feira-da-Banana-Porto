# Gerenciador de Estoque de Produtos Regionais (Porto de Manaus / Feira da Banana)

Este projeto foi desenvolvido como requisito avaliativo para a disciplina de **Programação em Python (AV4)** no **Curso Técnico em Inteligência Artificial**. Trata-se de uma aplicação em linha de comando (CLI) projetada para otimizar a gestão e logística interna de pequenos comerciantes locais que operam com produtos da biodiversidade amazônica (como açaí, farinha, cupuaçu e castanhas).

## Objetivo do Projeto

Atender às necessidades operacionais de feirantes do Porto de Manaus:

* Controle sobre o valor financeiro imobilizado no estoque.
* Prevenção de rupturas na cadeia de fornecimento por meio de alertas.
* Separação clara entre o cadastro inicial do item e as entradas diárias de mercadoria.

\---

## Lógica Computacional Implementada

O sistema adota boas práticas de engenharia de software e otimização para IA:

### 1\. Estruturas de Dados Dinâmicas Otimizadas

A arquitetura do banco de dados em memória utiliza um **Dicionário de Dicionários** indexado por uma chave primária numérica (`ID`). Isso garante operações de busca, atualização e exclusão em **tempo constante $O(1)$**, superando a ineficiência de varredura $O(n)$ das listas convencionais.

### 2\. Ciclo CRUD Separado por Responsabilidade

* **Create:** Cadastro isolado de novos produtos com geração de IDs sequenciais automáticos.
* **Update:** Adição exclusiva de novas quantidades (`QTD`) via código identificador, implementando operadores de acumulação composto (`+=`).
* **Read:** Listagem completa do inventário e algoritmo híbrido de busca (indexado por ID ou sequencial por Nome).
* **Delete:** Remoção física e segura do nó do dicionário usando métodos integrados da linguagem.

### 3\. Tratamento de Exceções e Sanitização

O sistema intercepta erros de entrada (`ValueError`) usando blocos `try-except` para evitar falhas de execução caso letras sejam digitadas em campos numéricos. Adicionalmente, processa strings nativamente para substituir vírgulas por pontos, adequando o sistema ao teclado numérico padrão do usuário brasileiro.

### 4\. Inteligência Artificial (Sistema Especialista Simbólico)

A função de Recomendação Inteligente implementa a abordagem clássica da IA Baseada em Regras. Avaliando de forma cruzada as restrições logísticas de quantidade física e o impacto financeiro (capital retido), o algoritmo gera diagnósticos de tomada de decisão em tempo real sobre compras e reposições.

\---

## 

