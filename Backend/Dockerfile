# FROM python:3.7-alpine
# # COPY . /code
# WORKDIR /code
# ENV FLASK_APP=api.py
# ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers jpeg-dev zlib-dev
# # RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
# # ENV LIBRARY_PATH=/lib:/usr/lib
# # RUN sudo apt install libjpeg8-dev zlib1g-dev
# # COPY requirements.txt backrequir.txt
# # RUN pip3 install --upgrade pip
# RUN pip install -r requirements.txt
# EXPOSE 4000
# COPY . .
# ENTRYPOINT [ "python" ]
# CMD ["api.py"]

# pip install --upgrade pip setuptools wheel
FROM python:3.8-slim-buster
# FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers jpeg-dev zlib-dev
# RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
# RUN apk add --update --no-cache py3-numpy py3-pandas@testing
# RUN apk add --no-cache --update \
#     python3 python3-dev gcc \
#     gfortran musl-dev g++ \
#     libffi-dev openssl-dev \
#     libxml2 libxml2-dev \
#     libxslt libxslt-dev \
#     libjpeg-turbo-dev zlib-dev
# RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
# ENV LIBRARY_PATH=/lib:/usr/lib
# RUN sudo apt install libjpeg8-dev zlib1g-dev
COPY requirements.txt requirements.txt
RUN pip install pandas
# RUN easy_install pandas
# RUN pip3 install --upgrade pip
# RUN apt-get update && \
#     apt-get -y install python3-pandas
RUN pip3 install -r requirements.txt
EXPOSE 4000
COPY . .
ENTRYPOINT [ "python" ]
CMD ["api.py"]
