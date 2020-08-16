FROM python:3.6.5
LABEL author="Shreyas Pimpalkar"

COPY . /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]