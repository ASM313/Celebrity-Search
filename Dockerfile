# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Expose port 8501 for the Streamlit app
EXPOSE 8501

# Set the Streamlit configuration to avoid the browser warning about accepting connections from outside localhost
ENV STREAMLIT_SERVER_HEADLESS true
ENV STREAMLIT_SERVER_PORT 8501

# Run the Streamlit app
CMD ["streamlit", "run", "example1.py"]
