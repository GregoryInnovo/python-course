# RESTFUL API with Flask

A Restful API with localhost mongodb

## Requirements

- [Python install](https://www.python.org/downloads/)

- Rest Client:

  - Option 1: [Insomnia](https://github.com/Kong/insomnia/releases/tag/core@2021.7.2)
  - Option 2: [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
  - Option 3: [JaSON](https://chrome.google.com/webstore/detail/jason/oealdlhfjifhgbmjnenhkgffglaibojf?hl=es)

- [Mongodb Community](https://www.mongodb.com/try/download/community)

## Create virtual environment (venv)

In the command line create a new venv:

```
# create venv
py -m venv venv
# activate to venv (win)
.\venv\Scripts\activate
# exit to venv
deactivate
```

## Install dependencies

In the virtual environment run:

```
pip install -r requirements.txt
```

## Environment variables to execute project

```
set FLASK_APP=platzi-api
set FLASK_ENV=development
```

## Run the server

```
flask run
```

## Some request body

### Create a career

In route <http://127.0.0.1:5000/carreras>
With POST method

```json
{
  "name": "Fullstack Developer",
  "description": "You will understand front end, back end and restful API architecture"
}
```

### Create a course

In route <http://127.0.0.1:5000/cursos>
With POST method

```json
{
  "name": "AWS fundamentals",
  "description": "In this course you will learn how to deploy in the AWS cloud",
  "courses": [
    {
      "order": 1,
      "name": "Course 1",
      "description": "description de la Course 1",
      "video": "https://youtube.com"
    },
    {
      "order": 2,
      "name": "Course 2",
      "description": "description de la Course 1",
      "video": "https://youtube.com"
    },
    {
      "order": 3,
      "name": "Course 3",
      "description": "description de la Course 1",
      "video": "https://youtube.com"
    },
    {
      "order": 4,
      "name": "Course 4",
      "description": "description de la Course 1",
      "video": "https://youtube.com"
    }
  ]
}
```

### Relation a course to a career

In route <http://127.0.0.1:5000/carreras/agregar-curso>
With PUT method

```json
{
  "id_carrera": "<career_id>",
  "id_curso": "<course_id>"
}
```
