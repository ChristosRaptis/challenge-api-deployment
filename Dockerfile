FROM ubuntu:22.04
FROM python:3.10
RUN mkdir /app
RUN mkdir /app/model
COPY model/lr_model.pkl /app/model/lr_model.pkl
COPY model/lr_transformer.pkl /app/model/lr_transformer.pkl
RUN mkdir /app/predict
COPY predict/prediction.py /app/predict/prediction.py
RUN mkdir /app/preprocessing
COPY preprocessing/cleaning_data.py /app/preprocessing/cleaning_data.py
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0"]

