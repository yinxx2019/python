def main():

    # store strings in variables to avoid typing same things later
    are = "Are you "
    do = "Do you have "
    insufficient = "Insufficient information to list possibilities."

    # function for infection type that will be called later
    def infection(infection_type):
        print("Possibilities include " + infection_type)

    # store conditions after aching bones that are asked in multiple paths
    # to avoid typing same things by calling the function later
    def aching_bones_follow_up():
        q = input(do + "aching bones or aching joints? ")
        if q.capitalize() == "Yes":
            infection("viral infection.")
        elif q.capitalize() == "No":
            q = input(do + "a rash? ")
            if q.capitalize() == "Yes":
                print(insufficient)
            elif q.capitalize() == "No":
                q = input(do + "a sore throat? ")
                if q.capitalize() == "Yes":
                    infection("throat infection.")
                elif q.capitalize() == "No":
                    q = input(do + "back pain just above the waist "
                                   "with chills and fever? ")
                    if q.capitalize() == "Yes":
                        infection("kidney infection.")
                    elif q.capitalize() == "No":
                        q = input(do + "pain urinating or are urinating "
                                       "more often? ")
                        if q.capitalize() == "Yes":
                            infection("urinary tract infection.")
                        elif q.capitalize() == "No":
                            q = input("Have you spent the day in the "
                                      "sun or in hot conditions? ")
                            if q.capitalize() == "Yes":
                                infection("sunstroke or heat exhaustion.")
                            elif q.capitalize() == "No":
                                print(insufficient)

    # function for the fever diagnosis system with conditions
    def conditions():
        # q is the input question variable for conditions
        q = input(are + "coughing? ")
        if q.capitalize() == "Yes":
            q = input(are + "short of breath or wheezing "
                            "or coughing up phlegm? ")
            if q.capitalize() == "Yes":
                infection("pneumonia or infection of airways.")
            if q.capitalize() == "No":
                q = input(do + "a headache? ")
                if q.capitalize() == "Yes":
                    infection("viral infection.")
                elif q.capitalize() == "No":
                    aching_bones_follow_up()
        elif q.capitalize() == "No":
            q = input(do + "a headache? ")
            if q.capitalize() == "Yes":
                q = input(are + "experiencing any of the following: pain when"
                                "bending your head forward, nausea or "
                                "vomiting, bright light hurting your eyes, "
                                "drosiness or confusion? ")
                if q.capitalize() == "Yes":
                    infection("menigitis.")
                elif q.capitalize() == "No":
                    q = input(are + "vomiting or had diarrhea? ")
                    if q.capitalize() == "Yes":
                        infection("digestive tract infection.")
                    elif q.capitalize() == "No":
                        aching_bones_follow_up()
            elif q.capitalize() == "No":
                aching_bones_follow_up()

    conditions()


main()
