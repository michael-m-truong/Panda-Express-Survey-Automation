FROM python:alpine3.7
COPY . /app
WORKDIR /
RUN python script.py
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]