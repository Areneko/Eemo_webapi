FROM python:3.7-alpine

ARG project_dir=/app

RUN pip install --upgrade pip && \
    pip install flask requests janome markovify

COPY ./python/src /app

WORKDIR ${project_dir}

CMD ["python", "app.py"]