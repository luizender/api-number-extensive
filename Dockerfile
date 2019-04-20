FROM alpine:3.9
COPY ./requirements.txt /build/requirements.txt
RUN apk add --no-cache --update python3 make && \
    apk add --no-cache --update --virtual .build-deps python3-dev gcc musl-dev && \
    pip3 install -r /build/requirements.txt --no-cache-dir && \
    apk del .build-deps
ADD . /code/
WORKDIR /code/
CMD [ "make", "run" ]