import pandas as pd
data = {
    "name":"somnath",
    "age": 20,
    "gender":"male"
}
data.pop('age')
print(data)
print(pd.DataFrame(data))
