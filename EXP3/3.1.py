speeds = []

for i in range(10):
    speed = float(input("Enter speed of Runner " + str(i + 1) + ": "))
    speeds.append(speed)

average_speed = sum(speeds) / len(speeds)

print("\nAverage Speed =", average_speed)

print("\nQualified Runners:")

for i in range(10):
    if speeds[i] > 1.5 * average_speed:
        print("Runner", i + 1, "- Speed:", speeds[i])
