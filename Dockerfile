# syntax=docker/dockerfile:1

FROM python:3.11.0 as base

WORKDIR DevOpsEx5

RUN apt-get update
RUN apt-get install -y gunicorn

COPY . .

RUN pip3 install poetry
Run poetry install


FROM base as development
CMD [ "poetry", "run" , "flask", "run", "--host=0.0.0.0"]

FROM base as production 
RUN pip3 install gunicorn flask
#CMD [ "poetry", "run", "gunicorn", "--bind 0.0.0.0 "todo_app.app:create_app()"]
RUN chmod +x ./run_gunicorn.sh
ENTRYPOINT ["./run_gunicorn.sh"]

