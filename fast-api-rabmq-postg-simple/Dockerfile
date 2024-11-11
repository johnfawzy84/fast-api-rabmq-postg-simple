# Use a lightweight Python base image
FROM python:3.12-slim-bookworm

# Set the working directory in the container
WORKDIR /fast-api-rabmq-postg-simple/fast-api-rabmq-postg-simple

# Install dependencies
RUN pip install uv

# Copy the rest of the application code
COPY main.py main.py
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

RUN uv pip install

# Expose the port on which the app will run
EXPOSE 8000

# Command to run the app when the container starts
CMD ["uvicorn", "main:app", "--reload", "--workers", "1"]