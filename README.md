# Política Aleatória em um Ambiente de Sala | Machine Learning

## 📖 Descrição

Este projeto implementa um exemplo prático de aprendizado por reforço utilizando uma política **aleatória** para movimentar um agente em um ambiente de sala. A estrutura do código segue padrões de projeto para facilitar a organização e a manutenção.

---

<p align="center">
  <img src="https://user-images.githubusercontent.com/91018438/204195385-acc6fcd4-05a7-4f25-87d1-cb7d5cc5c852.png" alt="animated" />
</p>

---


## 📁 Estrutura do Projeto

```plaintext
project/
├── main.py           # Arquivo principal para executar o programa
├── environment/
│   ├── __init__.py   # Inicialização do pacote do ambiente
│   └── room.py       # Classe para gerenciar o ambiente da sala
├── agents/
│   ├── __init__.py   # Inicialização do pacote de agentes
│   └── random_agent.py # Implementação do agente com política aleatória
├── utils/
│   ├── __init__.py   # Inicialização do pacote de utilitários
│   └── logger.py     # Classe para gerenciar logs

```

## ✈️ Funcionamento

- O agente começa na posição inicial (0, 0) e tenta alcançar a posição objetivo (ex.: (4, 4)).
- Ele realiza movimentos aleatórios (cima, baixo, esquerda, direita).
- O ambiente retorna recompensas:
  - **+10**: Quando o agente alcança a posição objetivo.
  - **-1**: Para cada movimento em outras direções.

Durante a execução, o progresso do agente é registrado no terminal, incluindo:
- Estados visitados.
- Recompensas recebidas.
- Recompensa total acumulada ao final de cada episódio.

---

## 🛠️ Como Executar

1. Certifique-se de que os arquivos estão organizados corretamente conforme a estrutura do projeto.
2. No terminal, execute o arquivo principal:
   ```bash
   python main.py
   ``` 
