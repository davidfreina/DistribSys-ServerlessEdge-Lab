FROM python:3

ENV PORT 5555
ENV HOST 0.0.0.0
ENV DEBUG False

ARG FUNCTION_DIR="/function"

RUN mkdir -p ${FUNCTION_DIR}

COPY src/ ${FUNCTION_DIR}/

RUN pip3 install --no-cache-dir -r ${FUNCTION_DIR}/requirements.txt

WORKDIR ${FUNCTION_DIR}

EXPOSE $PORT

ENTRYPOINT [ "python3", "app.py" ]

