FROM python:alpine
LABEL maintainer="me@xiao-jin.xyz"

COPY . /nfslm/
WORKDIR /nfslm
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
    && pip config set install.trusted-host mirrors.aliyun.com \
    && pip install -r requirements.txt

CMD python3 main.py