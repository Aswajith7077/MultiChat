FROM python:3.9

WORKDIR /code



COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./main.py /code/main.py

COPY ./RequestSchema /code/RequestSchema
COPY ./Config /code/Config
COPY ./Schemas /code/Schemas
COPY ./database.db /code/database.db
COPY ./Scripts  /code/Scripts

CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "80"]
