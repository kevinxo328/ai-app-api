# Use the official Python base image
FROM python:3.9-slim

# Set environment variables
ARG OPENAI_API_TYPE
ENV OPENAI_API_TYPE=${OPENAI_API_TYPE}
RUN echo $OPENAI_API_TYPE

ARG OPENAI_API_VERSION
ENV OPENAI_API_VERSION=${OPENAI_API_VERSION}
RUN echo $OPENAI_API_VERSION

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
RUN echo $OPENAI_API_KEY

ARG OPENAI_API_ENDPOINT
ENV OPENAI_API_ENDPOINT=${OPENAI_API_ENDPOINT}
RUN echo $OPENAI_API_ENDPOINT

ARG GPT35_MODEL
ENV GPT35_MODEL=${GPT35_MODEL}
RUN echo $GPT35_MODEL

ARG GPT4_MODEL
ENV GPT4_MODEL=${GPT4_MODEL}
RUN echo $GPT4_MODEL

ARG EMBEDDING_MODEL
ENV EMBEDDING_MODEL=${EMBEDDING_MODEL}
RUN echo $EMBEDDING_MODEL

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port that the FastAPI application will run on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
