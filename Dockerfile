FROM python:3.7.6-buster

RUN mkdir /leetcode/
COPY ./requirements.txt /leetcode/
COPY ./setup.py ./setup.py

RUN pip install --upgrade pip
RUN pip install -e .
RUN pip3 install -r /leetcode/requirements.txt

WORKDIR /leetcode/

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
