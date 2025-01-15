FROM circleci/python:3.9-node-browsers

WORKDIR /app

COPY requirements.txt /app/
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN mkdir -p /app/allure-results && chmod -R 777 /app/allure-results

COPY . /app/

ENV PATH="/app/venv/bin:$PATH"

CMD ["behave", "--tags=level_e2e", "--no-skipped"]
