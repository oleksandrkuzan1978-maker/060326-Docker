### С помощью графического интерфейса AWS EC2

1. Поднимаем виртуальный EC2 сервер `example-voting-app`
2. Устанавливаем на него docker и git
3. Скачиваем с GitHub проект на сервер
4. Запускаем этот проект в докере сервера



#### 1. Поднимаем виртуальный EC2 сервер `example-voting-app`

1. Проверяем регион (`Europe (Frankfurt)`)
2. Выбираем созданный в прошлый раз ключ (`AWS_key`)
3. Настраиваем группу

![Настройка группы `example-voting-app-group`:](./img/group-creation-1.png)

4. Добавляем скрипт стартового запуска:

```bash
#!/bin/bash

set -ex

# Сохраняем stdout и stderr скрипта в лог и одновременно выводим их в консоль
exec > >(tee -a /var/log/ec2-setup.log) 2>&1

dnf update -y
dnf install -y docker git

systemctl enable docker
systemctl start docker

usermod -aG docker ec2-user

mkdir -p /usr/local/lib/docker/cli-plugins

# Docker Compose V2
curl -SL \
  https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
  -o /usr/local/lib/docker/cli-plugins/docker-compose

chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

# Docker Buildx
curl -SL \
  https://github.com/docker/buildx/releases/download/v0.37.2/buildx-v0.37.2.linux-amd64 \
  -o /usr/local/lib/docker/cli-plugins/docker-buildx

chmod +x /usr/local/lib/docker/cli-plugins/docker-buildx

docker compose version
docker buildx version

cd /opt
git clone https://github.com/it-career-hub/example-voting-app.git
cd example-voting-app

docker compose up -d
```

5. После создания инстанса голосуем на 5000-м порту и смотрим результаты на 5001-м
6. Подключается к инстансу по SSH и смотрим основные команды:
```bash
docker compose ps
docker compose logs
docker compose logs -f
```
