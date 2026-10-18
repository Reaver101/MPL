import pandas as pd

data = pd.read_csv("EXP12/Iris.csv")

print("First 8 rows:")
print(data.head(8))


print("\nColumn Names:")
print(data.columns)


data_filled = data.copy()

data_filled["SepalLengthCm"] = data_filled["SepalLengthCm"].fillna(
    data_filled["SepalLengthCm"].mean()
)

data_filled["SepalWidthCm"] = data_filled["SepalWidthCm"].fillna(
    data_filled["SepalWidthCm"].mean()
)

data_filled["PetalLengthCm"] = data_filled["PetalLengthCm"].fillna(
    data_filled["PetalLengthCm"].mean()
)

data_filled["PetalWidthCm"] = data_filled["PetalWidthCm"].fillna(
    data_filled["PetalWidthCm"].mean()
)

print("\nData after filling missing values:")
print(data_filled)


data_removed = data.dropna()

print("\nData after removing rows with missing values:")
print(data_removed)


grouped_data = data.groupby("Species")

print("\nData grouped by Species:")
for species, group in grouped_data:
    print("\n", species)
    print(group)


mean_value = data["SepalLengthCm"].mean()
min_value = data["SepalLengthCm"].min()
max_value = data["SepalLengthCm"].max()

print("\nSepal Length Statistics:")
print("Mean =", mean_value)
print("Minimum =", min_value)
print("Maximum =", max_value)