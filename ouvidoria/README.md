<p align="center">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-3776AB?style=for-the-badge">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="MySQl" src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white">
</p>

# Sobre a aplicação

Aplicação CRUD de um sistema de ouvidoria, fazendo a implementação de categorias (reclamação, ideia/sugestão e outros) e armazenando as informações em um banco de dados MySQL em conexão local.

Desenvolvido a fim de ser utilizado como avaliação da disciplina de Linguagem Estruturada do curso de Sistemas de Informação da Unifacisa.

## Getting Started ▶️

Para rodar a aplicação, clone o repositório com:

```bash
$ git clone https://github.com/darllinsonazvd/unifacisa-python.git
```

No MySQL Workbench crie uma nova conexão com o user _root_ e o password _root_ e crias as tabelas com os seguintes comandos:

```sql
CREATE DATABASE db_ouvidoria;

USE db_ouvidoria;

CREATE TABLE claims (
	id int not null auto_increment primary key,
    author varchar(45) not null,
    claim varchar(250) not null
);

CREATE TABLE ideas (
	id int not null auto_increment primary key,
    author varchar(45) not null,
    idea varchar(250) not null
);

CREATE TABLE othersFeedbacks (
	id int not null auto_increment primary key,
    author varchar(45) not null,
    feedback varchar(250) not null
);
```

Depois é só rodar o arquivo _main.py_ com:

```bash
$ python ouvidoria/main.py
```

## Tecnologias 🚀

- Python 3
- MySQL
