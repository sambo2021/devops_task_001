FROM python:alpine3.8

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV PORT 5000

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]