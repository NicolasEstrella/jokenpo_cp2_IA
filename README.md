# 🖐️ Jokenpô com Visão Computacional

Este é um projeto em Python que usa **OpenCV** e **MediaPipe** para jogar **Pedra, Papel e Tesoura** com **as mãos detectadas pela webcam** em tempo real!

## 🚀 Integrantes do Grupo

- **RM93372:** Gabriel Arbigaus Carvalho de Souza 
- **RM94726:** Guilherme Cardoso Barreiro 
- **RM94751:** Henrique Copatti Cruz 
- **RM94236:** Nicolas Estrella Porciuncula 
- **RM93220:** Osvaldo José Sandoli Neto 

## 🧠 Como Funciona

O programa detecta até **duas mãos** simultaneamente e identifica qual gesto cada uma está fazendo com base nos dedos levantados:

As mãos são identificadas como:
- **Mão 1** (mais à esquerda da tela)
- **Mão 2** (mais à direita da tela)

Após reconhecer os gestos, o programa mostra quem venceu a rodada!

---

## 📦 Instalação

Antes de rodar, instale as dependências:
- Versão do python <= 3.12.3
- Versão do pip >= 19.3

```bash
pip install opencv-python mediapipe
