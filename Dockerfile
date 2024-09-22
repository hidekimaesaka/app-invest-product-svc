FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN pip install gunicorn

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "app:create_app()"]
