FROM python:3.9.4

RUN pip install --upgrade pip

WORKDIR /bot

COPY requirements.txt /bot

RUN pip install -r requirements.txt

COPY main.py /bot

CMD ["python", "main.py"]
