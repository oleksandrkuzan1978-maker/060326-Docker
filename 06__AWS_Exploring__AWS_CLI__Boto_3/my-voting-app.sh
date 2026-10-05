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
