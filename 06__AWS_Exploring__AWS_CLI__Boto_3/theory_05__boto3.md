### Что такое `boto3`?

`boto3` — это Python-библиотека, которая позволяет программе на Python обращаться к сервисам AWS через их API.

```
   Python-код
      │
      │ boto3
      ▼
   AWS API
      │
      ├── S3
      ├── EC2
      ├── RDS
      ├── DynamoDB
      ├── Lambda
      ├── SQS
      ├── SNS
      └── ...
```

### Инсталляция пакета `boto3`

`pip install boto3`



### 1. Что такое "бакет"?

`S3 (Simple Storage Service)` — объектное хранилище AWS.

Основная структура:

```text
AWS account
│
├── bucket-1
│   ├── file1.txt
│   ├── photo.jpg
│   └── documents/report.pdf
│
└── bucket-2
    └── data.json
```

Бакет (`bucket`) — это контейнер для объектов.

Файл в S3 называется объектом (`object`).

У объекта есть как минимум:

```text
Bucket -> имя бакета
Key    -> имя объекта
Body   -> содержимое объекта
```

Например:

```text
Bucket = ich-student-aws-lab-test
Key    = documents/report.pdf
```

Важно: **S3 не является обычной файловой системой!**  

* `documents/report.pdf` — это имя (ключ) объекта,  
* а `documents/` не обязательно настоящая директория.

---

### 2. Как правильно выбрать имя бакета?

Имя бакета должно быть уникальным глобально, то есть среди всех пользователей AWS,   
а не только в одном конкретном аккаунте.

Например:

```text
ich-student-aws-lab-test
```

Имя должно соответствовать правилам именования S3: 
* использовать строчные буквы, цифры, точки и дефисы.

---

### 3. Как создать бакет и увидеть ошибку

Регион можно получить из конфигурации AWS:

```python
import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = 'ich-student-aws-lab-test'

s3 = boto3.client('s3')

REGION = s3.meta.region_name

try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            'LocationConstraint': REGION
        }
    )
    print(f'Бакет {BUCKET_NAME} создан')

except ClientError as e:
    print(f'Ошибка: {e}')
```

Если имя занято или содержит ошибку, исключение вернёт эту информацию.


---

### 4. Как добавить файл в бакет?

Для обычного локального файла:

```python
s3.upload_file(
    'local_name.txt',
    BUCKET_NAME,
    'object_name.txt'
)
```

Здесь:

```text
'local_name.txt'     -> имя файл на компьютере
BUCKET_NAME          -> бакет S3
'object_name.txt'    -> имя объекта в S3
```

Часто удобно сразу "помещать файл в папку":

```python
s3.upload_file(
    'test.txt',
    BUCKET_NAME,
    'documents/my_test.txt'
)
```

В S3 получится:

```text
ich-student-aws-lab-test
└── documents/my_test.txt
```

---

### 5. Как получить список файлов в бакете

Используем:

```python
response = s3.list_objects_v2(
    Bucket=BUCKET_NAME
)
```

А затем:

```python
for obj in response.get('Contents', []):
    print(obj['Key'])
```

Например:

```text
test.txt
photo.jpg
documents/report.pdf
```


---

### 6. Как скачать файл из бакета?

```python
s3.download_file(
    BUCKET_NAME,
    'test.txt',
    'downloaded.txt'
)
```

где
`BUCKET_NAME`    -> имя бакета.
`test.txt`       -> `Key` объекта в S3.
`downloaded.txt` -> файл будет выгружен под этим именем

---

### 7. Как удалить файл?

```python
s3.delete_object(
    Bucket=BUCKET_NAME,
    Key='test.txt'
)
```

---

### 8. Как удалить бакет?

```python
s3.delete_bucket(
    Bucket=BUCKET_NAME
)
```

Но бакет должен быть пустым.

То есть сначала:

```python
s3.delete_object(
    Bucket=BUCKET_NAME,
    Key='test.txt'
)
```

а затем:

```python
s3.delete_bucket(
    Bucket=BUCKET_NAME
)
```

Если в бакете остались объекты, AWS не позволит удалить сам бакет.

---

### Методы `boto3`:

| Задача                   | Метод               |
| ------------------------ | ------------------- |
| Создать бакет            | `create_bucket()`   |
| Загрузить файл           | `upload_file()`     |
| Получить список объектов | `list_objects_v2()` |
| Скачать файл             | `download_file()`   |
| Удалить файл             | `delete_object()`   |
| Удалить бакет            | `delete_bucket()`   |

