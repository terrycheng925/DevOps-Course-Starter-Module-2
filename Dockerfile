# syntax=docker/dockerfile:1

FROM python:3.11.0

WORKDIR DevOpsEx5

RUN apt-get update
RUN apt-get install -y gunicorn

COPY . .

RUN pip3 install poetry
Run poetry install

CMD [ "poetry", "run" , "flask", "run", "--host=0.0.0.0"]

#EXPOSE 8084
#RUN chmod +x ./run_gunicorn.sh
#ENTRYPOINT ["./run_gunicorn.sh"]

