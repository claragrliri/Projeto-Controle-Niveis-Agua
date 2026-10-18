# ***🌊Monitoramento do Nível de Água🌊***

> Sistema em Python para simulação e monitoramento em tempo real do nível de um reservatório de água com alertas visuais coloridos no terminal.

![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)


## ***Um pouco sobre o Projeto***

Este projeto é um sistema interativo executado via terminal para monitorar os níveis de água de um reservatório. O objetivo é facilitar a identificação rápida do estado de risco por meio de um sistema de alertas codificado por cores.

O projeto utiliza a biblioteca **[Colorama](https://pypi.org/project/colorama/)** para garantir o desenvolvimento correto das cores no terminal em diferentes sistemas operacionais.


## ***Níveis e Status de Alerta 📊***

Cada nível de água do reservatório possui uma mensagem de alerta e uma cor correspondente, seguindo uma escala progressiva de risco:

| *Nível* | *Situação* | *Cor do Alerta* | *Risco* |
| :---: | :--- | :---: | :---: |
| **Nível 1** | Muito baixo (crítico) | 🔴 Vermelho | Crítico |
| **Nível 2** | Baixo | 🟡 Amarelo | Atenção |
| **Nível 3** | Médio | 🟢 Verde | Normal |
| **Nível 4** | Alto | 🔵 Ciano | Monitoramento |
| **Nível 5** | Muito alto (alerta) | 🟦 Azul | Alerta Máximo |


##  ***Pré-requisitos e Instalação ​🙏​✨​***

Antes de executar o projeto, certifique-se de ter o *Python* instalado no seu computador.

### Instalação da biblioteca `colorama` 👇​​

O projeto utiliza a biblioteca **Colorama** para colorir e formatar os textos no terminal. Para instalá-la, siga os passos abaixo:

1. Abra o terminal no seu VS Code.
2. Verifique se o seu ambiente está nos coformes e execute o comando:

```text
pip install colorama
```
Se retornar informações como versão e local de instalação, o Colorama já está pronto para ser usado!

## ***Simulação no Terminal***

```text
=== Sistema de Monitoramento de Reservatório de Água ===
Simulando leituras consecutivas do sensor:

[Nível 1] Situação do reservatório: Muito baixo (crítico)
[Nível 3] Situação do reservatório: Médio
[Nível 5] Situação do reservatório: Muito alto (alerta)
[Nível 2] Situação do reservatório: Baixo
[Nível 4] Situação do reservatório: Alto
```
