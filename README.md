# Dockerized Django Resume Builder

## Common Usage
Python command-line tool allows to:
- create resume by filling out personal information, education background and etc
- view created resume, edit or delete it

---
## Prerequsites
- Python 3.9.x
- Python Virtual Environment (preferable)
- Git
- Docker
---
## Common setup
Clone the repo and install the dependencies.
```
git clone https://github.com/ana-gujabidze/django-resume-builder.git
cd django-resume-builder/
```

Download Docker Desktop from [the official website](https://docs.docker.com/desktop/). It will automatically install docker for you.

The app has required paramter in settings SECRET_KEY that was moved to .env file. Create `.env` file similar to `.env_sample` file and specify environmental variables.

### Run application locally

If virtual environment is available run the following command

```
python3 -m pip install -r requirements.txt
```

else:
```
pip3 install -r resume/requirements.txt
``` 

Navigate to the root directory of the django project.

First makemigrations and then start the server
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
Open http://127.0.0.1:8000 in the browser to check that server started successfully.

### Build Images and Run Containers With Docker Client

Navigate to the source directory and from there run command in order to build the image
```
docker build -t django-app .
```
After successful build, run the container by the command
```
docker run -it -p 8000:8000 --env-file .env django-app
```

After running python app image, in CLI URL of localhost will appear, http://0.0.0.0:8000.
Follow the link, in the browser the same page will appear just like running locally. 
