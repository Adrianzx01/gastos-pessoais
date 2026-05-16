# 💰 Gerenciador de Gastos Pessoais CLI

![Pipeline Status](https://github.com/Adrianzx01/gastos-pessoais/actions/workflows/ci.yml/badge.svg)

🔗 **Link para a aplicação:** [[https://gastos-peappais-ywbztkcpaztv9ui9tmdokp.streamlit.app/](https://gastos-peappais-ywbztkcpaztv9ui9tmdokp.streamlit.app/)]

🔗 **Documentação da API:** [[https://docs.awesomeapi.com.br/api-de-moedas](https://docs.awesomeapi.com.br/api-de-moedas)]
## 📝 Descrição do Projeto
Este projeto foi desenvolvido como parte de uma atividade de Arquitetura de Software. Ele consiste em uma ferramenta de linha de comando (CLI) para auxiliar no controle financeiro pessoal, permitindo o registro de despesas e o cálculo automático do total acumulado.

## 🎯 Problema Real
Muitas pessoas perdem o controle de suas finanças por não registrarem pequenos gastos cotidianos. Esta ferramenta oferece uma interface simples e rápida para garantir que nenhum gasto passe despercebido.

## 🚀 Tecnologias e Boas Práticas
* **Linguagem:** Python 3.13
* **Qualidade:** Análise estática com `flake8` e Testes Unitários com `pytest`.
* **CI/CD:** Pipeline automatizado via **GitHub Actions**.
* **Versionamento:** Segue o padrão de Versionamento Semântico (v1.0.0).
* **Interface web e Dashboard:** Streamlit
* **Deploy e hospedagem:** Streamlit Cloud
* **Requests:** Consumo da API pública (AwesomeAPI)

## 🛠️ Como Executar
1. Clone o repositório.
2. Ative seu ambiente virtual: `venv\Scripts\activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o app: `python src/main.py`

## ✅ Testes e Qualidade
Para rodar os testes manualmente:
```bash
python -m pytest
```
## 🧑‍💻 Executar a Aplicação
```bash
streamlit run app.py
```
## 📝 Observações de Resiliência
O sistema possui uma lógica de fallback. Caso a API de cotações atinja o limite de requisições ou esteja instável, o sistema utilizará um valor padrão de R$ 5.50 para garantir que a interface continue funcional.
