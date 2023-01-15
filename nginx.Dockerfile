FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY /static /home/public/static

#RUN nginx -t