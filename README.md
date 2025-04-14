# 🖐️ Jokenpô com Visão Computacional

Este é um projeto em Python que usa **OpenCV** e **MediaPipe** para jogar **Pedra, Papel e Tesoura** com **as mãos detectadas pela webcam** em tempo real!

## 🚀 Integrantes do grupo

- Gabriel Arbigaus Carvalho de Souza RM93372
- Guilherme Cardoso Barreiro RM94726
- Henrique Copatti Cruz RM94751
- Nicolas Estrella Porciuncula RM94236
- Osvaldo José Sandoli Neto RM93220

## 🧠 Como funciona

O programa detecta até **duas mãos** simultaneamente e identifica qual gesto cada uma está fazendo com base nos dedos levantados:

As mãos são identificadas como:
- **Mão 1** (mais à esquerda da tela)
- **Mão 2** (mais à direita da tela)

Após reconhecer os gestos, o programa mostra quem venceu a rodada!

---

## 📦 Instalação

Antes de rodar, instale as dependências:

```bash
pip install opencv-python mediapipe
