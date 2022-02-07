# Jokenpo
 
Esse é um projeto que consiste em identificar qual foi a jogada de cada jogador e determinar qual o jogador vencedor com o auxílio de Visão Computacional. <br><br>
<img src = "https://github.com/Italoko/Jokenpo/blob/main/screenshot_example/jokenpo_example.jpg?raw=true" />
<br>

## Jogo

Pedra, papel e tesoura, também chamado em algumas regiões do Brasil de jokenpô (do japonês じゃんけんぽん, jankenpon), é um jogo de mãos recreativo e simples para duas ou mais pessoas, que não requer equipamentos nem habilidade.
No Janken-pon, os jogadores devem simultaneamente esticar a mão, na qual cada um formou um símbolo (que significa pedra, papel ou tesoura).
A pedra é simbolizada por um punho fechado; a tesoura, por dois dedos esticados; e o papel, pela mão aberta.
### Regras
* Pedra ganha da tesoura (amassando-a ou quebrando-a).
* Tesoura ganha do papel (cortando-o).
* Papel ganha da pedra (embrulhando-a).
* Caso dois jogadores façam o mesmo gesto, ocorre um empate.
<br><a href="https://pt.wikipedia.org/wiki/Pedra,_papel_e_tesoura">Fonte</a>

## Dependencias

* OpenCV - Para processamento das imagens <br>
```pip install opencv-python```
* MediaPipe - Para reconhecimento das mãos <br>
```pip install mediapipe```
* O módulo ```hands_detector.py``` contém funcionalidades baseadas no resultado do processamento e rastreamento das mãos e seus pontos chaves. 
  * Repositório do ```hands_detector.py``` : ```https://github.com/Italoko/Jokenpo``` <br>
* Numpy - Para manipulação de arrays <br>
```pip install numpy```

## Como usar

Para usar em seu projeto siga os passos abaixo: 

1. Clone o repositório em sua maquina
 ```bash git clone https://github.com/Italoko/Virtual-Mouse ```

2. Execute o aquivo ```main.py``` python file.

## Conteúdo

* O arquivo ```main.py``` contém o lógica principal para execução.
* O arquivo ```jokenpo_moviments.py``` é modulo responsável identificar qual foi a jogada (Pedra, Papel ou Tesoura).
* O arquivo ```screen.py``` contém funcionalidades para iterações na tela.
* O arquivo ```util.py``` contém algumas funcionalidades genéricas (Controle de FPS, menu, etc..).
