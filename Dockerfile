# Sets the base image for subsequent instructions
FROM python:3.8-slim
# Sets the working directory in the container  
WORKDIR /app
# Copies the files to the working directory
COPY . /app
# Install dependencies
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
RUN apt purge google-chrome-stable
RUN apt purge chromium-browser
RUN apt install -y chromium-browser
RUN pip install -r requirements.txt
# Copies everything to the working directory
# Command to run on container start
EXPOSE 5000
ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "app.wsgi:app"]