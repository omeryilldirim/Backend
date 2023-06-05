# INSTRUCTION arguments

FROM python:3.10.8-slim-bullseye

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /teamwork

COPY . .

RUN pip install -r requirements.txt --no-cache-dir
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# CMD python manage.py runserver 0.0.0.0:8000