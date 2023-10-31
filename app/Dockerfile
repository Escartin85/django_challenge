# pull official base image
FROM python:3.11.4-slim-buster
#SHELL ["/bin/bash", "-c", "apt update && apt install curl -y && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash && source ~/.nvm/nvm.sh && nvm install --lts && npm install -g npm"]

#SHELL ["/bin/bash", "-c", "apt-get update && apt-get install -y python-dev python-pip"]
#RUN apt-get update && apt-get install -y python-dev python-pip
# set work directory
WORKDIR /usr/src/app

# set environment variables
# prevents Python from writing pyc files to disc 
ENV PYTHONDONTWRITEBYTECODE 1
# prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
#SHELL ["/bin/bash", "-c", "pip install --upgrade pip"]
RUN pip install --upgrade pip
COPY ./requirements.txt ./
#SHELL ["/bin/bash", "-c", "pip install -r ./requirements.txt"]
RUN pip install -r requirements.txt

# copy project
COPY . .