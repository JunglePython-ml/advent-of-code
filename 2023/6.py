with open("6.in") as f:
    lines = f.readlines()


def get_times(time, distance):
    x = 1
    for t, d in zip(time, distance):
        total = 0
        for t_test in range(1, int(t)):
            if (int(t) - t_test) * int(t_test) > int(d):
                total += 1
        x *= total

    return x

time, distance = [line.split()[1:] for line in lines]
big_time, big_distance = "".join(time).split(","), "".join(distance).split(",")
print(get_times(time, distance))
print(get_times(big_time, big_distance))