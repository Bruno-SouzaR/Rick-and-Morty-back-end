FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV DATABASE_URI=${DATABASE_URI}
ENV FRONT_END_URL=${FRONT_END_URL}
ENV ENVIRONMENT=${ENVIRONMENT}

EXPOSE 5000