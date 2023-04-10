FROM python:3.10.6


WORKDIR /app

RUN pip install --upgrade pip 

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./board_site ./board_site

CMD ["python3", "./board_site/manage.py", "runserver", "0.0.0.0:8000"]