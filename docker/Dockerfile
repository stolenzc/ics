FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

EXPOSE 8000

CMD uvicorn app.main:app
