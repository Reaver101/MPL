import numpy as np

daily_temp = np.array([30, 32, 31, 33, 34, 32, 35])

print("1D Array - Daily Temperature:")
print(daily_temp)

print("\nTemperature on 3rd day:", daily_temp[2])

print("Temperature from 2nd to 5th day:", daily_temp[1:5])


city_temp = np.array([
    [30, 32, 31, 33, 34],
    [25, 27, 26, 28, 29],
    [35, 36, 34, 37, 38]
])

print("\n2D Array - Temperature of Cities:")
print(city_temp)

print("\nTemperature of first city on 2nd day:", city_temp[0][1])

print("Temperature readings of first city:", city_temp[0, :])


reshaped = city_temp.reshape(5, 3)

print("\nReshaped 2D Array:")
print(reshaped)


weekly_temp = np.array([
    [
        [30, 31, 32],
        [25, 26, 27]
    ],
    [
        [33, 34, 35],
        [28, 29, 30]
    ]
])

print("\n3D Array - Temperature for Different Weeks:")
print(weekly_temp)

print("\nTemperature:", weekly_temp[0][1][2])

print("Temperature data of first week:")
print(weekly_temp[0])

new_shape = weekly_temp.reshape(3, 2, 2)

print("\nReshaped 3D Array:")
print(new_shape)