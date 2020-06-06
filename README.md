# cursoead_python_django

Projeto cursoead uma plataforma de curso online simples, feito com o objetivo de estudo em Django.

## Rodando em SO Linux Ubuntu versão 18.04 LTS e
## Docker container

Python, Django e Postgresql "containeirizados", descritos nos arquivos:

Dockerfile e docker-compose

prontos para execução.

## Para usar:
Subir o serviço django, com os programas python/django escutando a porta 8000 (conforme descrito no docker-compose.yml)

sudo docker-compose up

## Acessar a aplicação:

Pelo navegador, com localhost ou 127.0.0.1 ou o ip da máquina rodando o django:

http://localhost:80000

## Dicas com o Docker:
#### Para criar o Projeto inicialmente:

sudo docker-compose run web django-admin.py startproject cursoead .

#### Para criar novas aplicações no Projeto do django:

sudo docker-compose run web django.admin startapp core

sudo docker-compose run web django.admin.py startapp courses

#### Para acessar o banco de dados postgresql:

sudo docker ps
( para obter o hash correspondente ao container postgres, por exemplo: ff2edb1b9307 )

sudo docker exec -it ff2edb1b9307 sh
( uma vez no shell:
     su - postgres
     psql

