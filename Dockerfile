ARG PYTHON_VERSION=3.9.10

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080

#CMD ["daphne", "-b", "0.0.0.0", "-p", "8080", "main.asgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

