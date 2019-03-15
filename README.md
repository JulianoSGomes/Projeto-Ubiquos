# Projeto de Sistemas Ubíquos 
imagem ISO compatível com  Raspberrypi 3B / 3B+ 
https://drive.google.com/drive/folders/1_j1xjECIMcgfBg9zIqjuU9spgfP-RJ4k

## Modo de uso mainCLI

`python3 mainCLI.py <string com comandos>`
  
String com comandos pode ser formada por qualquer combinação  das letras "f", "t", "d" e "e". Onde:
F = Frente
T = Trás
D = Direita
E = Esquerda

`python3 mainCLI.py ffdfe`

Nesse exemplo o Jabuti andará 2 segundos para frente, virará a direita, anda mais 1 segundo para frente e vira a  esquerda.

## Modo de uso do site

`python3 main.py`

Acessar de qualquer navegador a página http://192.168.1.2:5000
