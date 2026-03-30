FROM python:3.12-alpine

# Set working directory
WORKDIR /usr/src/app

# Prevent Python from buffering and creating .pyc files
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy entrypoint script and make executable
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# Copy the rest of the application code
COPY . .