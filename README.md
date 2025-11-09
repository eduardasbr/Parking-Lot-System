# 🚗 Sistema de Controle de Vagas — Estacionamento

Este é um programa simples em **Python** para controle de vagas de um estacionamento com **10 vagas numeradas de 1 a 10**.

O sistema permite visualizar, ocupar e liberar vagas, além de encerrar o programa de forma segura.

---

## 🧩 Funcionalidades

- Mostrar o **estado atual** das vagas (livres ou ocupadas)
- **Ocupar** uma vaga disponível
- **Liberar** uma vaga ocupada
- **Encerrar** o programa apenas quando o usuário escolher a opção 4
- Validação: o número da vaga deve estar entre **1 e 10**

---

## 🖥️ Exemplo de uso

--- MENU ---
1 - Mostrar estado das vagas
2 - Ocupar uma vaga
3 - Liberar uma vaga
4 - Encerrar o programa
Escolha: 1

Vaga 1: Livre
Vaga 2: Ocupada
...
Vaga 10: Livre

---

## 📘 Lógica do programa

As vagas são representadas por uma lista com 10 posições:

vagas = [0,0,0,0,0,0,0,0,0,0]


0 → vaga livre

1 → vaga ocupada

O programa usa um loop while para exibir o menu até o usuário escolher encerrar.

---

## 🧠 Conceitos aplicados

Estruturas de repetição (while)

Estruturas condicionais (if, elif, else)

Listas

Manipulação de entrada do usuário (input)

---

## 🏁 Objetivo educacional

Projeto desenvolvido para praticar raciocínio computacional e pensamento lógico, como parte da disciplina
Computational Thinking Using Python (CP3).
