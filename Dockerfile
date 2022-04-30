FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY start.sh  Pipfile  Procfile  requirements.txt ./

RUN chmod +x start.sh && chmod +x start.sh && pip install -r requirements.txt


COPY . .

CMD [ "/code/start.sh"]

