# Introduction
The Todolist app which was built with Python Flask and VueJS  
Only Python 3.5+ is supported
# Backend installation

1. Clone repository
```bash
$ git clone https://github.com/zshanabek/todo-app
$ cd todo-app
```
2. Install Python dependencies
```bash
$ cd server
$ pip install -r requirements.txt
```
3. Run server
```bash
$ python3 api.py
```
4. Get todos
```bash
$ curl localhost:5000/todos
```
Expect json response:
```json
[
    {
        "id": 1,
        "title": "build an API",
        "description": "this is desc1",
        "due_date": "2018-11-16",
        "completed": true,
        "created_at": "2018-11-15 15:10:29.706557",
        "updated_at": "2018-11-15 15:10:29.706557"
    },
    {
        "id": 2,
        "title": "write article",
        "description": "this is desc1",
        "due_date": "2018-11-17",
        "completed": true,
        "created_at": "2018-11-15 15:10:29.706557",
        "updated_at": "2018-11-15 15:10:29.706557"
    }
]

```
# Frontend installation

2. Install Javascript dependencies
```bash
$ cd client
$ npm install
```
3. Run server
```bash
$ npm run dev
```
4. Your application is running here: http://localhost:8080
