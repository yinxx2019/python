def main():
    age = int(input("Please enter your age: "))
    rest_heart_rate = int(input("Please enter your resting heart rate: "))

    maximum_heart_rate = 208 - 0.7 * age
    reserve = maximum_heart_rate - rest_heart_rate

    zone1_min = round(rest_heart_rate + reserve * 0.5, 2)
    zone1_max = round(rest_heart_rate + reserve * 0.6, 2)

    zone2_min = round(rest_heart_rate + reserve * 0.6 + 0.01, 2)
    zone2_max = round(rest_heart_rate + reserve * 0.7, 2)

    zone3_min = round(rest_heart_rate + reserve * 0.7 + 0.01, 2)
    zone3_max = round(rest_heart_rate + reserve * 0.8, 2)

    zone4_min = round(rest_heart_rate + reserve * 0.8 + 0.01, 2)
    zone4_max = round(rest_heart_rate + reserve * 0.93, 2)

    zone5_min = round(rest_heart_rate + reserve * 0.93 + 0.01, 2)
    zone5_max = round(rest_heart_rate + reserve * 1, 2)

    print("Your heart rate reserve is: ", reserve, "bpm")
    print("Here is a breakdown of your training zones: ")
    print("Zone 1: ",zone1_min,"to",zone1_max,"bpm")
    print("Zone 2: ",zone2_min,"to",zone2_max,"bpm")
    print("Zone 3: ",zone3_min,"to",zone3_max,"bpm")
    print("Zone 4: ",zone4_min,"to",zone4_max,"bpm")
    print("Zone 5: ",zone5_min,"to",zone5_max,"bpm")

main()