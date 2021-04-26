import pandas as pd

# Scalar = 45
# Vetor = [1, 1, 2, 3]
# Matriz = [[1, 2], [3, 4]]
# Tensor = [[[1], [2]], [[3], [4]]]

# matriz = [["Gustavo", 102], ["Amanda", 16], ["Gustavo", 102]]
# df = pd.DataFrame(matriz, columns=["Nome", "Idade"])
# # print(df.set_index("Nome"))

# print(df["Nome"])
# print(df["Nome"][0])
# print(df[df["Nome"] == "Gustavo"])

# df = pd.read_csv("teste.csv", dtype=str)
# print("Gustavo" in df["Nome"].values)
# print(df.columns)
# print(df.values)

# df = pd.read_csv("teste.csv", dtype=str)
# df = df.drop("Cpf", axis=1)
# df.to_csv("teste.csv", index=False)

df = pd.read_csv("teste.csv", dtype=str)
print(df.to_json(orient="records"))
