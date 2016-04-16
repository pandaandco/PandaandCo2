questions1 = [("At a party do you", "interact with many, including strangers", "interact with a few, known  to you"),
    ("At parties do you", "Stay late, with increasing energy", "Leave early, with decreasing energy"),
    ("In your social groups do you", "Keep abreast of others happenings", "Get behind on the news"),
    ("Are you usually rather", "Quick to agree to a time", "Reluctant to agree to a time"),
    ("In company do you", "Start conversations", "Wait to be approached"),
    ("Does new interaction with others", "Stimulate and energize you", "Tax your reserves"),
    ("Do you prefer", "Many friends with brief contact", "A few friends with longer contact"),
    ("Do you", "Speak easily and at length with strangers", "Find little to say to strangers"),
    ("When the phone rings do you", "Quickly get to it first", "Hope someone else will answer"),
    ("At networking functions you are", "Easy to approach", "A little reserved")]


counter_a, counter_b, counter_c,counter_d, counter_e = 0, 0, 0, 0, 0,

for question in questions1:
    question_string = "%s:\n\tA. %s\n\tB. %s\n[a/b]:  " % (question[0], question[1], question[2])
    answer = raw_input(question_string).lower()
    while answer not in ("a", "b"):
        print("Please choose A or B")
        answer = raw_input(question_string).lower()
    if answer == "a":
        counter_a += 1
    else:
        counter_b += 1

#print "A total is %d" % counter_a
#print "B total is %d" % counter_b
