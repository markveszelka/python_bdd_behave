ARG PYTHON_VERSION=3.9
ARG NODE_VERSION=latest
ARG ALLURE_VERSION=2.24.0
ARG CHROME_DRIVER_VERSION=latest

FROM circleci/python:${PYTHON_VERSION}-node-browsers

WORKDIR /app
COPY requirements.txt /app/

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip && \
    unzip allure.zip -d /app/ && \
    rm allure.zip && \
    sudo ln -s /app/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure

USER circleci
COPY . /app/

RUN mkdir -p /app/allure-results &&  \
    chmod -R 777 /app/allure-results &&  \
    chown circleci /app/allure-results

ENV PATH="/app/venv/bin:$PATH"

CMD ["bash", "-c", "behave --tags=priority_medium --no-skipped && \
                    allure generate --single-file ./allure-results --clean -o ./allure-report && \
                    echo 'Allure report generated at ./allure-report'"]
