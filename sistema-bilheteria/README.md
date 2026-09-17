# Sistema de Gestão de Bilheteria
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"><img src="https://img.shields.io/badge/Athletico_Paranaense-cc0000?style=for-the-badge&labelColor=000000" alt="Athletico Paranaense">

Este projeto é um sistema interativo de bilheteria de terminal desenvolvido em Python. O objetivo principal foi consolidar os fundamentos da linguagem, saindo da teoria e construindo uma aplicação real do zero, simulando a gestão de ingressos da Ligga Arena.

## Funcionalidades
* **Menu de Navegação Contínua:** Sistema operando em loop seguro até o encerramento manual.
* **Emissão Inteligente:** Cálculo automatizado de preços com aplicação de descontos para Sócios Furacão e Meia-entrada.
* **Cancelamento Seguro:** Tratamento lógico que permite cancelar ingressos sem quebrar os índices ou corromper a leitura dos relatórios.
* **Métricas Financeiras:** Geração de relatório final com total vendido, faturamento global, ticket médio e picos de preço (maior/menor valor arrecadado).
* **Interface Visual Customizada:** Uso de códigos de escape ANSI (como \033[31m) para manipular o estilo do terminal, aplicando a identidade visual rubro-negra do clube diretamente no console para criar uma imersão real durante a navegação.

## Estruturas e Conceitos Aplicados
O código foi desenhado para colocar em prática conceitos estruturais essenciais:
* **Tuplas (Imutáveis):** Utilizadas estrategicamente para mapear os nomes dos setores e a tabela de preços fixa, protegendo os dados essenciais de alterações em tempo de execução.
* **Listas Dinâmicas (Mutáveis):** Aplicadas para gerenciar a entrada e saída de torcedores na sessão, permitindo anexar novos cadastros, anular registros e utilizar lógicas de fatiamento (como `[-1]` para buscar a última venda realizada)[cite: 2].
* **Controle de Fluxo Avançado:** Uso de condições aninhadas (`if`/`elif`/`else`) combinadas com laços `while` para validar entradas de usuário e evitar quebras no sistema.
* **Tipos Primitivos e Interface ANSI:** Conversão rigorosa de `str`, `int` e `float`, além de uso de códigos de cor no terminal para criar uma interface visual imersiva e amigável.
