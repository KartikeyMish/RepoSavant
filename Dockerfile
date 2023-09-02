# using python 3.11
FROM python:3.11

# set a directory for the app
WORKDIR /reposavant

# copy all the files to the container
COPY requirements.txt requirements.txt 
COPY ./static ./static 
COPY ./templates ./templates 
COPY analyze.py analyze.py

# install dependencies
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000
CMD [ "python", "app.py" ]