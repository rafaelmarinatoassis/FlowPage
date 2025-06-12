# 🔁 Troca Automática de Abas do Google Chrome

Este é um aplicativo em Python com interface gráfica que permite alternar automaticamente entre abas do Google Chrome, com controle individual do tempo de exibição de cada aba.

## 📦 Funcionalidades

- Escolha a quantidade de abas a serem controladas (limite de 10)
- Defina qual aba (1 a 9) será exibida e por quanto tempo
- Interface gráfica moderna e intuitiva feita com Tkinter
- Botão para iniciar e parar o ciclo de troca
- Aviso automático se o número de abas ultrapassar o limite

## 🖼️ Interface

A interface é simples e clara:

1. Digite a **quantidade de abas** (máximo 10)
2. Clique em **"Configurar"**
3. Preencha os campos:
   - Número da aba (entre 1 e 9)
   - Tempo que ela ficará visível (em segundos)
4. Clique em **"▶ Iniciar"**
5. Para parar a execução, clique em **"⏹ Parar"**

---

## 🚀 Requisitos

- Python 3.8 ou superior
- Biblioteca `keyboard` para controlar atalhos de teclado

Instale com:

```bash
pip install keyboard
