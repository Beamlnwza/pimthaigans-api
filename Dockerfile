FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN useradd -m -u 1000 user

USER user

ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

RUN touch $HOME/app/.env

RUN --mount=type=secret,id=S3,mode=0444,required=true \
    echo "$(cat /run/secrets/S3)" >> $HOME/app/.env

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]