FROM python:3.7-alpine

ARG project_dir=/app

ENV PORT 5000

RUN pip install --upgrade pip && \
    pip install flask requests janome markovify python-dotenv

COPY ./src /app

WORKDIR ${project_dir}

CMD ["python", "app.py"]