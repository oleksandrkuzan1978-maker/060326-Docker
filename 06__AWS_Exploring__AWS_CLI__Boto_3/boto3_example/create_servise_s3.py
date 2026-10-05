"""
ВАЖНО!
Имя бакета S3 должно быть уникально для всего Амазона!
"""

import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = 'ich-060326-ptm-bar'

# Регион берётся из ~/.aws/config
s3 = boto3.client('s3')
REGION = s3.meta.region_name

# Создание бакета
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            'LocationConstraint': REGION
        }
    )
    print(f'Бакет {BUCKET_NAME} создан')

except ClientError as e:
    print(f'Ошибка создания бакета: {e}')

# Получение списка бакетов
response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])