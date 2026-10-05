import boto3

BUCKET_NAME = 'ich-060326-ptm-bar'
FILE_NAME = 'tmp.txt'
FOLDER_NAME = 'documents'

s3 = boto3.client('s3')

# Загрузка файла в папку documents
s3.upload_file(
    FILE_NAME,
    BUCKET_NAME,
    f'{FOLDER_NAME}/{FILE_NAME}'
)

# Загрузка файла в корень documents
s3.upload_file(
    FILE_NAME,
    BUCKET_NAME,
    f'{FILE_NAME}'
)
print(f'Файл {FILE_NAME} загружен в корень бакета')

# Получение списка всех объектов
response = s3.list_objects_v2(
    Bucket=BUCKET_NAME
)

print('\nВсе объекты в бакете:')

for obj in response.get('Contents', []):
    print(obj['Key'])

# Получение списка объектов только в папке documents
response = s3.list_objects_v2(
    Bucket=BUCKET_NAME,
    Prefix=f'{FOLDER_NAME}/'
)

print(f'\nОбъекты в папке {FOLDER_NAME}:')

for obj in response.get('Contents', []):
    print(obj['Key'])