# greetings-test

##Greeting application

I recommend you to use a virual environment (```python3 -m venv env```).

### Installation
In terminal:

```git clone https://github.com/arttre/greetings-test.git -b main``` -- installing repository

```cd greetings-test``` -- moving to a _main directory_

```pip install -r requirements.txt``` -- installing all requirements

*_pip_ must be installed.

### Run with Docker
Inside _main directory_:

```docker-compose build``` -- building docker images
```docker-compose up``` -- running our images

You can work with application using _127.0.0.1_ url.

### Run without Docker

Inside _main directory_:
```python3 -m uvicorn main:app```
to run our local server.

After that open ```index.html``` file.
Here it is, you can work with application.

*of course, _python3_ must be installed.
