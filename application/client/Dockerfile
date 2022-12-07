FROM python:3

ENV HOST "http://host.docker.internal:5555/upload"

ARG FUNCTION_DIR="/function"

RUN mkdir -p ${FUNCTION_DIR}

COPY src/ ${FUNCTION_DIR}/
COPY files/ files/

RUN pip3 install --no-cache-dir -r ${FUNCTION_DIR}/requirements.txt

WORKDIR ${FUNCTION_DIR}

ENTRYPOINT [ "python3", "app.py" ]

