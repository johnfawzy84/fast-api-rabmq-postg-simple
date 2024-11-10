# Use a lightweight Python base image
FROM python:3.12-slim-bookworm

# Set the working directory in the container
WORKDIR /fast-api-rabmq-postg-simple

# Install dependencies
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy the rest of the application code
COPY . .

RUN uv --version

# Expose the port on which the app will run
EXPOSE 8000

# Command to run the app when the container starts
CMD ["uvicorn", "main:app", "--reload", "--workers", "1"]