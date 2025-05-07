import json
import boto3
import csv

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket = event['Records'][0]['s3']['bucket']['name']
    objeto = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=objeto)
    linhas = response['Body'].read().decode('utf-8').splitlines()

    reader = csv.reader(linhas)
    next(reader)  # pula cabeçalho
    total_linhas = sum(1 for linha in reader)

    print(f"Arquivo '{objeto}' tem {total_linhas} linhas")

    return {
        'statusCode': 200,
        'body': json.dumps(f'{total_linhas} linhas processadas com sucesso.')
    }
