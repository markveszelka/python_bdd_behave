FROM circleci/python:3.9-node-browsers

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt /app/
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application files
COPY . /app/

# Default command to run behave with the specified options
CMD ["behave", "--tags=level_e2e", "--no-skipped"]
