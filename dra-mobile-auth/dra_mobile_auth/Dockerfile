FROM python:alpine

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add jpeg-dev zlib-dev libjpeg libffi-dev

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
EXPOSE 8000

WORKDIR /app
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /app/
# ENTRYPOINT [ "./entrypoint.sh" ]