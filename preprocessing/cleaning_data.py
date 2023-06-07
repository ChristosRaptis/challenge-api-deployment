import pandas as pd

def preprocess(input: dict) -> dict:
        df = pd.DataFrame.from_dict([input.dict()])
        df.applymap(lambda x: int(x) if type(x)==bool else x)
        return df