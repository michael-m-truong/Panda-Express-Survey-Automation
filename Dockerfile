# # Sets the base image for subsequent instructions
# FROM ubuntu:22.04
# # Sets the working directory in the container  
# WORKDIR /app
# # Copies the files to the working directory
# COPY . /app
# # Install dependencies
# # RUN apt-get update && apt-get install -y \
# #     libgconf-2-4 \
# #     libfontconfig1 \
# #     libx11-6 \
# #     libasound2 \
# #     libpulse0
# RUN apt-get update -y
# RUN apt-get install -y python3-pip
#     # RUN wget https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_linux64.zip && \
#     # unzip chromedriver_linux64.zip && \
#     # rm chromedriver_linux64 && \
#     # chmod +x chromedriver && \
#     # mv chromedriver /usr/local/bin/
#     # ENV PATH='/usr/local/bin:${PATH}'
# # RUN apt purge google-chrome-stable
# RUN apt purge chromium-browser
# RUN apt install -y chromium-browser
# RUN pip install -r requirements.txt
# # Copies everything to the working directory
# # Command to run on container start
# EXPOSE 5000
# ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]

# FROM ubuntu:20.04

# # Create a new non-root user
# RUN useradd -m myuser

# # Set the working directory for the non-root user
# WORKDIR /home/myuser/app

# # Copy the files to the working directory
# COPY . /home/myuser/app

# # Install dependencies
# RUN apt-get update && apt-get install -y \
#     unzip \
#     wget \
#     libgconf-2-4 \
#     libfontconfig1 \
#     libx11-6 \
#     libasound2 \
#     libpulse0 \ 
#     chromium-browser \ 
#     python3-pip \ 
#     libnss3 \
#     coreutils \
#     snapd

# # RUN snap --version
# RUN systemctl start snapd.service
# #RUN systemctl enable --now snapd.service
# RUN snap install chromium
# # RUN chromium-browser --version

# # Change ownership of the app directory to the non-root user
# # RUN chromium-browser
# RUN chown -R myuser:myuser /home/myuser/app

# RUN pip install -r requirements.txt

# # Download and install ChromeDriver
# RUN wget https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_linux64.zip && \
# unzip chromedriver_linux64.zip && \
# rm chromedriver_linux64.zip && \
# chmod +x chromedriver && \
# mv chromedriver /usr/local/bin/
# ENV PATH='/usr/local/bin:${PATH}'

# # Switch to the non-root user
# USER myuser

# # Expose the port for the app
# EXPOSE 5000

# # Run the app
# ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]

FROM python:3.9-alpine

COPY . .

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
#RUN apk add chromium chromium-chromedriver

# Download and install ChromeDriver
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.62/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    rm chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver

# upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade gevent

# expose port for app
EXPOSE 5000

# Run the app
ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]
#ENTRYPOINT ["forever", "--trace-warnings", "start", "-c", "/start.sh"]
#ENTRYPOINT ["forever", "start", "-c", "gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]