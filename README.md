Documentação do trabalho de Linguagens Formais e Computabilidade[cite: 5, 21]. 

---

# Analisador Sintático de Expressões Aritméticas 🧮

Este projeto consiste na implementação de um **Analisador Sintático Descendente Recursivo** para uma Gramática Livre de Contexto (GLC) simples[cite: 13, 19, 38]. O objetivo é validar expressões e demonstrar sua estrutura através de sequências de derivação[cite: 37, 44].

Trabalho desenvolvido para a disciplina de **Linguagens Formais e Computabilidade** da **UFPB**[cite: 1, 3].

## 📋 A Gramática

O analisador foi construído com base nas seguintes regras de produção[cite: 22, 23]:

1.  **$E \rightarrow (E Op E)$**
2.  **$E \rightarrow a$**
3.  **$Op \rightarrow + \mid - \mid * \mid /$**

**Terminais:** `(`, `)`, `+`, `-`, `*`, `/`, `a`[cite: 24].  
**Não-terminais:** `E`, `Op`[cite: 24].

---

## 💻 Funcionamento do Código

A implementação utiliza a técnica de **Análise Descendente Recursiva**, onde cada não-terminal da gramática é processado por uma função específica[cite: 38, 39].

### Estrutura de Dados (`Expr`)
Utilizamos `@dataclass` para representar a árvore sintática de forma clara:
* **`Var`**: Representa o terminal `a`[cite: 40].
* **`Node`**: Representa uma operação composta, armazenando a subexpressão esquerda, o operador e a subexpressão direita[cite: 42].

### Funções Principais
* **`parseExpr(expr)`**: Analisa o não-terminal **E**. Se encontrar um `a`, identifica a produção $E \rightarrow a$[cite: 40, 41]. Se encontrar um `(`, chama a si mesma recursivamente para processar a estrutura $(E~Op~E)$[cite: 42].
* **`parseOp(expr)`**: Analisa o não-terminal **Op**, validando se o próximo caractere é um dos quatro operadores aritméticos permitidos[cite: 23, 39].
* **`main()`**: Interface de linha de comando que recebe a entrada do usuário e exibe a sequência de derivação ou uma mensagem de erro em caso de falha sintática[cite: 36, 44].


---

## 🛠️ Como Executar

1.  Certifique-se de ter o **Python 3.10+** instalado.
2.  Clone este repositório.
3.  Execute o script principal:
    ```bash
    python3 main.py
    ```
4.  Insira as expressões para teste (ex: `(a+a)` ou `((a*a)/a)`)[cite: 32, 34].

---

## 📝 Requisitos da Entrega (APS 2)

Conforme as instruções da atividade[cite: 5, 6]:
* **Linguagem:** Python[cite: 7].
* **Saída:** Exibição da sequência de derivação/árvore sintática[cite: 37, 44].


---

**Integrantes:**
* Mikael Menezes da Rocha Barreto 20240008889
* Kaio Renato de Melo Marinho 20240009222

---
