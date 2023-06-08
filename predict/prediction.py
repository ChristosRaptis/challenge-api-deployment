import joblib
from preprocessing.cleaning_data import preprocess

lr = joblib.load("model/lr_model.pkl")
ct = joblib.load("model/lr_transformer.pkl")


def predict(dataframe: dict) -> float:
    df = preprocess(dataframe)
    transformed_df = ct.transform(df)
    prediction = lr.predict(transformed_df)
    return round(prediction[0])
