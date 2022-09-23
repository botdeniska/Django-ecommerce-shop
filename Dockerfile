FROM python:3.10

RUN mkdir /site
COPY . /site/
WORKDIR /site

RUN pip install --upgrade pip
ADD requirements.txt /

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]