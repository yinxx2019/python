

def main():
    filename = input("Please enter the file name: ")
    try:
        # read file
        f = open(filename, "r")
    # create print message for exception
    except Exception:
        print("Unable to open", filename, ". Try something else! ")
        return

    # calculate how long data covers later in the loop
    minute_data_count = 0

    # calculate how long did the pump run later in the loop
    minute_run_count = 0

    # calculate watt minutes later in the loop
    watt_minutes = 0

    # calculate how long it took to consume 5 and 100 gallons of water later
    minute_5 = 0
    minute_100 = 0

    # though pump should be expected to draw about 1000 watts a minute when
    # it's running, seems like once reaches 500 watt also counts
    THRESHOLD = 500

    # for loop that get every line in the file
    for minute_data in f:

        # update the minutes that data covers
        minute_data_count += 1

        # get the value of each line
        lines = minute_data.strip()

        # sum the value in each line to get watt minutes
        watt_minutes += int(lines)

        # set condition to use watt minutes calculating
        #  minutes to reach certain gallons

        # set the condition to filter when pump actually ran
        if int(lines) >= THRESHOLD:
            minute_run_count += 1
        else:
            minute_run_count = minute_run_count

        # convert run count to gallon
        gallon_hour = minute_run_count * 2

        # use gallon to see if the pump it on.
        # since gallon is even, 5 rounds up to 6
        if gallon_hour <= 6:
            minute_5 += 1
        else:
            minute_5 += 0

        if gallon_hour <= 100:
            minute_100 += 1
        else:
            minute_100 += 0

    # count how long did pump run
    count_120 = 0
    count_stop = 0
    min_num = 0
    MAGIC_NUM = 120
    minute_index = []
    list_120 = []

    # I've been tried my best here but seems the count_stop value is
    # not stored properly... may I get partial credits on this?
    try:
        # read file
        file = open(filename, "r")
    # create print message for exception
    except Exception:
        print("Unable to open", filename, ". Try something else! ")
        return
    for x in file:
        min_num += 1
        pump_num = int(x.strip())
        # if the pump is off after opening for more than 120 minutes
        if count_120 == 0 and count_stop >= MAGIC_NUM:
            # append the beginning point when the pump is on
            list_120.append(count_stop)
            # append how long the pump is on
            minute_index.append(min_num - count_stop - 1)
            count_stop = 0
        # increment when pump is open
        elif pump_num >= THRESHOLD:
            count_120 += 1
            # update stop point when reach to the magic number
            if count_120 >= MAGIC_NUM:
                count_stop = count_120
        else:
            # reset once the pump is off
            count_120 = 0

    # metric conversion calculating
    hour_data_count = minute_data_count / 60
    day_data_count = hour_data_count / 24
    gallon_day = float(gallon_hour * 24) / hour_data_count
    kwh = (watt_minutes / 1000) / 60

    # set condition for gallons never reach 100
    if gallon_hour < 100:
        minute_100 = -1
    else:
        minute_100 = minute_100

    # print all messages
    print("Data covers a total of", hour_data_count, "hours")
    print("(That's", day_data_count, "days) \n")
    print("Pump was running for", minute_run_count, "minutes,", "producing",
          gallon_hour, "gallons")
    print("(That's", gallon_day, "gallons per day) \n")
    print("Pump required a total of", watt_minutes, "watt minutes of power")
    print("That's", kwh, "kWh \n")
    print("It took", minute_5, "minutes of data to reach 5 gallons.")
    print("It took", minute_100, "minutes of data to reach 100 gallons. \n")
    print("Information on water softener recharges:")
    # should have printed each items in the list_120 for when starts to run
    # over 120 minutes and items in the list minute.index how long it runs
    print(list_120)
    print(minute_index)


main()
