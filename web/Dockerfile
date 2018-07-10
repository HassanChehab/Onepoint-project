FROM alpine:latest

RUN apk --update add \
    python2 \
    python2-dev \
    py2-pip \
    build-base

ADD requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app/main.py"]