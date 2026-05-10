[![Publish Docker image](https://github.com/prr133f/yadro_devops_intership_2026/actions/workflows/docker-image.yml/badge.svg?branch=main)](https://github.com/prr133f/yadro_devops_intership_2026/actions/workflows/docker-image.yml)

# Возникшие проблемы и их решения
Проблема: Сервис httpstat.us оказался недоступен

Решение: Поднят self-hosted сервис из официального Docker образа
```
ghcr.io/aaronpowell/httpstatus:f1c763d1f33cd10566f18ec190fc853895bdbdd7
```
Арендована виртуалка на Yandex cloud, на которой был раскатан сервис. В скрипте используется доступ к self-hosted решению. 

ВМ с сервисом не будет отключена до окончания проверки тестового задания.
