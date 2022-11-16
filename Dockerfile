FROM python:3.10-slim-buster
RUN mkdir /code
WORKDIR /code
#COPY . /app
#EXPOSE 8000
COPY requirements.txt /code/
RUN pip install --user -r requirements.txt
COPY . /code/
#docker run --mount src=%cd%,target=/code,type=bind -p 8001:8000 -it --rm ration-card
CMD python manage.py runserver 0.0.0.0:8000