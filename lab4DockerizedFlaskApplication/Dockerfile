FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /flask
WORKDIR /flask
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["Activity2.py", "run", "--host", "0.0.0.0"]