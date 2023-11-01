FROM python:3.8

WORKDIR /app

# install dependencies
COPY ./requirements.txt /requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./app/ /app

CMD ["python3", "app.py"]
