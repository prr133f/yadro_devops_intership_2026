[![Publish Docker image](https://github.com/prr133f/yadro_devops_intership_2026/actions/workflows/docker-image.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/prr133f/yadro_devops_intership_2026/actions/workflows/docker-image.yml)

# Порядок решения задания
## 1
Был написан простой скрипт на Python с использованием requests который посылает 5 запросов к сервису httpstat.us

## 2
Скрипт был упакован в Docker образ, зависимости качаются в образ из requirements.txt

В Github Actions образ собирается и выгружается в GHCR (GitHub Container Registry)

## 3
Создано 2 ансибл роли: Docker и App

Docker роль отвечает за установку Docker и настройку сервиса.

App роль отвечает за развертывание приложения в Docker контейнере.

В плейбуке роли объединяются, пингуются хосты и определяется ОС хоста.

В качестве тестового хоста была поднята ВМ на Yzndex Cloud с Ubuntu 22.04

# Возникшие проблемы и их решения
Проблема: Сервис httpstat.us оказался недоступен

Решение: Поднят self-hosted сервис из официального Docker образа
```
ghcr.io/aaronpowell/httpstatus:f1c763d1f33cd10566f18ec190fc853895bdbdd7
```
Арендована виртуалка на Yandex cloud, на которой был раскатан сервис. В скрипте используется доступ к self-hosted решению. 

ВМ с сервисом не будет отключена до окончания проверки тестового задания.
