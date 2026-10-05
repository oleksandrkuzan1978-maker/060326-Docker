### 1. Создание AWS EC2 instance через AWS CLI

Ссылка на описание команд создания и запуска EC2 instance:   
[https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html)


```bash
aws ec2 run-instances \
    --image-id ami-09903cd4fe0670a06 \
    --count 1 \
    --instance-type t3.micro \
    --key-name AWS_key \
    --associate-public-ip-address \
    --security-group-ids sg-00852e8407c919d4a \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=voting_app_GROUP_NAME}]' \
    --region eu-central-1 \
    --user-data file://my-voting-app.sh
```

---

`--image-id ami-09903cd4fe0670a06`
id образа.  
Можно найти в AWS Console: `EC2` -> `AMIs`

---

`--count 1`
Сколько интсансов создавать этой командой

---

`--instance-type t3.micro`
Тип инстанса

---

`--key-name AWS_key`
Имя ключа, который мы создали на AWS
(**ВАЖНО**: именно имя ключа **без всяких расширений**, а не имя файла с расширением `*.pem`!)

---

`--associate-public-ip-address`
Ассоциировать публичный ip-адрес с нашим сервером

---

`--security-group-ids sg-00852e8407c919d4a`
id группы безопасности.  
Можно найти в AWS Console: `EC2` -> `Network & Security` - > `Security Groups`

---

`--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=voting_app_GROUP_NAME}]'`
Эта часть задаёт тег, который будет автоматически присвоен создаваемому EC2-инстансу. 

    То есть после запуска инстанса в EC2 он будет иметь: `Name = voting_app_GROUP_NAME`

---

`--region eu-central-1`
В каком регионе создаётся инстанс

---

`--user-data file://path/to/your/my-voting-app.sh`
Для простоты файл `my-voting-app.sh` удобнее поместить в ту же папке, откуда будет запущена эта команда.  
Внутри `my-voting-app.sh` находится скрипт, который будет выполнен при первом запуске инстанса.


---


### 2. Удаление AWS EC2 instance через AWS CLI

`aws ec2 terminate-instances --instance-ids INSTANCE_ID`

Например: `aws ec2 terminate-instances --instance-ids i-07419ab67e2f5451d`