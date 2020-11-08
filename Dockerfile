FROM alpine:latest

RUN apk add py-cryptography
RUN apk add py3-josepy
# RUN apk add py3-bcrypt
# RUN apk add py3-passlib

RUN apk add py3-pip

RUN pip install fastapi uvicorn

RUN pip install python-multipart
RUN pip install python-jose[cryptography]
# RUN pip install passlib[bcrypt]
RUN pip install SQLAlchemy

COPY ./app /app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
