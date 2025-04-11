# Use an official Python image (slim version for a smaller footprint)
FROM python:3.9-slim

# Prevent Python from writing .pyc files to disk and disable output buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update package lists and install build-essential for compiling dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port that Streamlit uses (8501)
EXPOSE 8501

# Command to run your Streamlit app on the dynamic $PORT (provided by the hosting platform) with CORS disabled
CMD sh -c "streamlit run riskweaver_app.py --server.port $PORT --server.enableCORS false"


