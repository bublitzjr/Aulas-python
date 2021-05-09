import pandas as pd

def convert_to_json(cursor):
    columns = [i[0] for i in cursor.description]  # Importando todos
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    json = df.to_json(orient="records")        

    return json