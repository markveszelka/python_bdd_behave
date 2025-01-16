# Description: Makefile for running BDD tests with Allure report

# Local variables:
ALLURE_RESULTS_DIR = $(shell pwd)/allure-results
ALLURE_REPORT_DIR = $(shell pwd)/allure-report

# Docker variables:
DOCKER_IMAGE = python-bdd
DOKCER_ALLURE_RESULTS_DIR = $(shell pwd)/docker-allure-results
DOCKER_ALLURE_REPORT_DIR = $(shell pwd)/docker-allure-report

### LOCAL PYTHON RUN: ##########################################
# FIXME: update script to run e2e tests instead of medium
run-level-e2e-tests:
	source .venv/bin/activate && behave --tags=priority_medium --no-skipped

generate-allure-report:
	allure generate --single-file $(ALLURE_RESULTS_DIR) --clean -o $(ALLURE_REPORT_DIR)

open-local-allure-report:
	allure open $(ALLURE_REPORT_DIR)

clean-local-reports:
	rm -rf allure-report/* allure-results/* allure-screen-shots/*

# To run it use command: 'make run-local-all'
run-local-all: clean-local-reports run-level-e2e-tests generate-allure-report open-local-allure-report


### LOCAL DOCKER RUN: ##########################################
build:
	docker buildx build --platform linux/amd64 -t $(DOCKER_IMAGE) --load --no-cache .

run-tests-and-generate-allure-report:
	docker run --rm -it \
		-v $(DOCKER_ALLURE_REPORT_DIR):/app/allure-report \
		-v $(DOKCER_ALLURE_RESULTS_DIR):/app/allure-results $(DOCKER_IMAGE)

# Clean up allure files
clean-docker-reports:
	rm -rf docker-allure-report/* docker-allure-results/* allure-screenshots allure-results allure-report

open-docker-allure-report:
	open docker-allure-report/index.html

# To run it use command: 'make run-docker-all', and make sure that you have docker installed
# and in 'environment.py' the headless mode is set to 'True'
run-docker-all: clean-docker-reports build run-tests-and-generate-allure-report open-docker-allure-report
