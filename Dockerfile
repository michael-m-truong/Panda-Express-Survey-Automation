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

# Sets the base image for subsequent instructions
FROM ubuntu:22.04

# Sets the working directory in the container  
WORKDIR /app

# Copies the files to the working directory
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    unzip \
    wget \
    libgconf-2-4 \
    libfontconfig1 \
    libx11-6 \
    libasound2 \
    libpulse0 \ 
    chromium-browser \ 
    python3-pip

RUN pip install -r requirements.txt

# Download and install ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_linux64.zip && \
unzip chromedriver_linux64.zip && \
ls && \
echo hereeeeeeeeeeeee && \
rm chromedriver_linux64.zip && \
echo hereeeeeeeeeeeee && \
ls && \
echo hereeeeeeeeeeeee && \
pwd && \ 
echo hereeeeeeeeeeeee && \
ls && \
chmod +x chromedriver && \
mv chromedriver /usr/local/bin/
ENV PATH='/usr/local/bin:${PATH}'

# CMD chromium-browser
# Copies everything to the working directory
# Command to run on container start
EXPOSE 5000
ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]