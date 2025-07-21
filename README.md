# Marcador OCR

## Objetivo

Este repositório contém uma aplicação desenvolvida em Python para identificação automática de nomes em tela utilizando OCR (Reconhecimento Óptico de Caracteres). O sistema realiza uma captura de parte da tela, aplica OCR com a biblioteca EasyOCR e destaca visualmente os nomes encontrados de uma lista pré-definida.

## Descrição

A ferramenta foi criada para facilitar a marcação visual de elementos textuais exibidos em uma interface gráfica, especialmente nomes constantes em uma lista de interesse. Ela realiza:

- Captura da tela (região definida manualmente) utilizando `pyautogui`
- Conversão da imagem e aplicação de OCR com `easyocr`
- Comparação dos textos encontrados com os nomes buscados (sem acentuação)
- Realce dos nomes identificados com retângulos coloridos usando OpenCV
- Exibição do resultado e impressão de quais nomes foram ou não encontrados

## Tecnologias Utilizadas

- Python 3.x
- OpenCV
- EasyOCR
- PyAutoGUI
- PIL (Pillow)
- NumPy
- Unidecode
