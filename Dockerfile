# TODO: add variables for magic numbers
FROM circleci/python:3.9-node-browsers

WORKDIR /app
COPY requirements.txt /app/

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.zip && \
    unzip allure.zip -d /app/ && \
    rm allure.zip && \
    sudo ln -s /app/allure-2.24.0/bin/allure /usr/local/bin/allure

USER circleci
COPY . /app/

RUN mkdir -p /app/allure-results &&  \
    chmod -R 777 /app/allure-results &&  \
    chown circleci /app/allure-results

ENV PATH="/app/venv/bin:$PATH"

CMD ["bash", "-c", "behave --tags=priority_medium --no-skipped && \
                    allure generate --single-file ./allure-results --clean -o ./allure-report && \
                    echo 'Allure report generated at ./allure-report'"]
