# set base image (host OS)
FROM python:3.7.6

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/webapp

# set the working directory in the container
WORKDIR $PROJECT_DIR

# copy the content of the local src directory to the working directory
COPY ./ $PROJECT_DIR

# install dependencies
RUN pipenv install --system --deploy

EXPOSE 5000

# command to run on container start
CMD [ "python", "./api.py" ] 