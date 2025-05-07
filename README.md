
Função AWS Lambda para processar arquivos CSV carregados em um bucket S3, automatizando o processamento de dados.
# AWS Lambda: Processamento de Arquivos CSV

## Objetivo do Projeto

Este projeto tem como objetivo automatizar o processamento de arquivos CSV carregados em um bucket S3. Quando um novo arquivo é carregado no S3, a função Lambda é acionada automaticamente para processá-lo, realizar operações de leitura e manipulação dos dados.

## Tecnologias Usadas

- **AWS Lambda**
- **Amazon S3**
- **IAM (Permissões)**
- **Python (3.11)**

## Passos para Execução

1. Criação de um bucket S3 (lambda-processador-csv-ludmila-ramos) para armazenar os arquivos CSV.
2. Configuração da função AWS Lambda para processar arquivos CSV no S3.
3. Definição de um gatilho (trigger) no bucket S3 para chamar a função Lambda sempre que um novo arquivo CSV for carregado.
4. Teste realizado ao enviar um arquivo CSV para o S3 e a função Lambda processando-o automaticamente.

## Como Testar

1. Faça o upload de um arquivo CSV no bucket S3 configurado.
2. A função Lambda será acionada automaticamente, processando o arquivo CSV e realizando as operações programadas.

## Prints de Configuração

![Lambda Function](caminho/para/imagem-lambda.png)
*Figura 1: Configuração da função Lambda.*

![S3 Bucket](caminho/para/imagem-s3.png)
*Figura 2: Configuração do Bucket S3 com o trigger para Lambda.*


![Logs da Função](docs/lambda-logs.png)
*Figura 3: Logs da execução da função Lambda.*
