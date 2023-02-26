# Conversor de sistemas numéricos (CSN) 🏛️

## Índice

- [Conversor de sistemas numéricos (CSN) 🏛️](#conversor-de-sistemas-numéricos-csn-️)
  - [Índice](#índice)
  - [Sobre](#sobre)
  - [Descrição](#descrição)
  - [Instalação](#instalação)
  - [Comandos](#comandos)
  - [Contribuir](#contribuir)

## Sobre

Conversor de sistemas numéricos (CSN) é um utilitário de linha de comandos que converte números das bases numéricas decimal (D), octal (O), binária (B), hexadecimal (H) e romana (R). Para além da conversão, o CSN tem embutido outros subcomandos.

---

## Descrição

O CSN possui 2 principais funcionalidades (até agora), que são:

1- Converter números de uma base para outra. Ex.:
```txt
python[versão] main.py convert [número] [base_de_origem] [base_destino]
```

2- Somar números de diferentes bases. Ex.:
```txt
python[versão] main.py sum [[--bin | --dec | --oct | --hex | --rom] n1 n2 ... n*]
```

---

## Instalação

Antes de clonar este repositório, certifique-se que a sua máquina cumpra com estes requisitos:

- Sistema Unix-like (Linux, MacOS, BSD, etc..)
- Git
- Python3.x, x >= 10

1- Clone este repositório
```bash
git clone https://github.com/HelioPC/csn.git
```
2- Navegue até a pasta do repositório
```bash
cd <pasta_do_projeto>
```

Para confirmar se a instalação foi bem sucedida:

```bash
python main.py --help
```

---

## Comandos

- convert
  ```txt
  Converte um número de uma base numérica para outra
  ```
  ```txt
  convert [-h] [-v] number [-m mantiss] base_from base_to
  ```
  ```txt
  convert -v -m 8 10010.0110 B D # 18.375
  ```

- sum
  ```txt
  Efetua a soma de listas de números das variadas bases numéricas
  ```
  ```txt
  sum [-h] [-v] [-f] [--bin [BIN ...]] [--dec [DEC ...]] [--hex [HEX ...]] [--oct [OCT ...]] [--rom [ROM ...]]
  ```
  ```txt
  sum -v --bin 101 1 100001 --rom CM # 939
  ```

- translate
  ```txt
  Escreve um número por extenso (apenas em português)
  ```
  ```txt
  translate [-h] [-v] -n NUMBER [-b BASE]
  ```
  ```txt
  translate -v -n 2023 -b D # Dois Mil e Vinte e Três
  ```

---

## Contribuir

Caso encontre um bug ou uma possível melhoria para o projeto, crie uma `issue` ou uma `pull request`.
