### Управление сервисами AWS с помощью командной строки

Всё, что делали в предыдущем пункте в графическом режиме на сайте AWS,  
можно выполнить непосредственно в терминале нашего компьютера.


---

#### Установка AWS CLI на Windows, MacOS и Amazon Linux

[https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions)


* Для **Windows** Amazon рекомендует установку через PowerShell
* Простое решение: 
  * скачать `*.msi` - файл 
  * далее запустить и следовать инструкции установщика

* Для **MacOS** Amazon рекомендует установку через `install.sh`
* Простое решение: 
  * выполнить в терминале команду `brew install awscli` 

---

#### Установка AWS CLI на Ubuntu

Старую версию (если есть) желательно предварительно удалить:

```bash
# Если ранее была установлена AWS CLI через apt:
sudo apt remove awscli
```

Установка новой:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

---

#### Универсальная проверка установки AWS CLI для всех операционных систем

```bash
$ aws --version
```

Должно быть что-то вроде этого:
```bash
aws-cli/2.37.9 Python/3.14.6 Linux/6.8.0-138-generic exe/x86_64.ubuntu.22
```