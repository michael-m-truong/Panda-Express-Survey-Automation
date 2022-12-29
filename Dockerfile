FROM python:alpine3.7
COPY . /app
WORKDIR /
RUN ["sudo apt purge google-chrome-stable", "sudo apt purge chromium-browser", "sudo apt install -y chromium-browser", "pip install -r requirements.txt"]
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]