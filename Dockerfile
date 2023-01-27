FROM python:3.8
WORKDIR /code
COPY . .
ADD docker_cmd.sh /
CMD ["/bin/bash","-c","./docker_cmd.sh"]
