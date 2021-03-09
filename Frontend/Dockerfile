FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers jpeg-dev zlib-dev
# RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
# ENV LIBRARY_PATH=/lib:/usr/lib
# RUN sudo apt install libjpeg8-dev zlib1g-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
ENTRYPOINT [ "python" ]
CMD ["app.py"]




# CMD ["flask", "run"]




# FROM ubuntu:18.04
#
# #ENV PATH="/root/.local/bin:${PATH}"
# #ARG PATH="/root/.local/bin:${PATH}"
# EXPOSE 5000
#
# RUN apt-get update
# RUN apt-get install --assume-yes --fix-broken
# RUN apt-get install -y python3 wget git
# RUN apt-get install python3-pip -y
# #RUN apt-get install -y gcc
#
# RUN pip3 install --upgrade pip
#
# COPY . src/
# WORKDIR /src/
# RUN  pip3 install -r requirements.txt
# ENTRYPOINT ["python3"]
# CMD ["app.py"]