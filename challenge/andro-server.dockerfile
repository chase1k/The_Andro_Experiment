FROM python:3.11

WORKDIR ~/andro-server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY Server/ .
RUN chmod 444 flag.txt
expose 5000
RUN useradd -ms /bin/bash ctf
USER ctf
ENTRYPOINT python3 main.py