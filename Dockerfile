FROM python:3.8-alpine as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --no-warn-script-location --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY app /app

WORKDIR /
ENTRYPOINT ["python", "-m", "app"]
