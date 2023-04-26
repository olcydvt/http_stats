# Base image
FROM python:3

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip3 install scapy

ENV MY_VAR=""

# Copy the rest of the application code
COPY . .

# Run the application

CMD ["sh", "-c", "python3 http_stats.py $MY_VAR"]

