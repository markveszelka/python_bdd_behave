# Description: Makefile for running BDD tests with Allure report

# Local variables:
ALLURE_RESULTS_DIR = $(shell pwd)/allure-results
ALLURE_REPORT_DIR = $(shell pwd)/allure-report

# Docker variables:
DOCKER_IMAGE = python-bdd
DOKCER_ALLURE_RESULTS_DIR = $(shell pwd)/docker-allure-results
DOCKER_ALLURE_REPORT_DIR = $(shell pwd)/docker-allure-report

# LOCAL PYTHON RUN:
run-level-e2e-tests:
	source .venv/bin/activate && behave --tags=priority_medium --no-skipped

generate-allure-report:
	allure generate --single-file $(ALLURE_RESULTS_DIR) --clean -o $(ALLURE_REPORT_DIR)

open-allure-report:
	allure open $(ALLURE_REPORT_DIR)

# To run it use command: 'make run-local-all'
run-local-all: run-level-e2e-tests generate-allure-report open-allure-report


# LOCAL DOCKER RUN:
build:
	docker buildx build --platform linux/amd64 -t $(DOCKER_IMAGE) --load --no-cache .

run-allure-report:
	docker run --rm -it -v $(DOCKER_ALLURE_REPORT_DIR):/app/allure-report -v $(DOKCER_ALLURE_RESULTS_DIR):/app/allure-results $(DOCKER_IMAGE)

# Clean up allure files
clean:
	rm -rf docker-allure-report/* docker-allure-results/*

# To run it use command: 'make run-docker-all'
run-docker-all: clean build run-allure-report
