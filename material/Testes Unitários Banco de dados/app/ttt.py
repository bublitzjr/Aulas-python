def convert_dict_to_sql_string(data: dict, separator=",") -> str:
    converted_to_sql_data = []
    for key, value in data.items():
        if isinstance(value, str) and value.upper() != "DEFAULT" and value.upper() != "NULL":
            converted_to_sql_data.append(f"{key} = '{value}'")
        else:
            converted_to_sql_data.append(f"{key} = {value}")

    string_values = f"{separator}".join(converted_to_sql_data)
    return string_values


valores = dict(Nome="Gustavo", Idade=100)
where = dict(Nome="Amanda", Idade=20)
string_values = convert_dict_to_sql_string(valores)
string_where = convert_dict_to_sql_string(where, " and ")

print(f"UPDATE TABELA SET {string_values} WHERE {string_where}")
