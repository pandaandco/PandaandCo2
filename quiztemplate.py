#!/usr/bin/python
#    questions.py



questions1 = [("Would your friends describe you as", "adventurous", "hard working","'the loud one'", "caring", "you don't have any friends"),
            ("Where would you rather be", "outside", "at your desk studying","at a party", "wherever your friends are", "hiding in a dark room by yourself"),
            ("What do you spend most of your day doing", "exploring", "eating","chilling with friends", "sleeping", "watching Netflix by yourself"),
            ("A panda is stuck in a tree, do you", "try to help him", "work out the best solution before acting","talk to it", "go and get help", "laugh at it"),
            ("There is only enough baboo left for one panda to eat sufficiently, do you", "challenge the other pandas for it", "try to find some more","share it with your best friend", "share it between all of the other pandas", "eat it all yourself"),
            ("A panda decides to become the leader of the group, do you:", "challenge him to be the leader", "tell him pandas don't have a leader","throw him a party", "let him do it", "nothing - you don't care"),
            ("Pick a panda", "A", "B","C", "D", "E"),
    ]


counter_a, counter_b, counter_c, counter_d, counter_e = 0, 0, 0, 0, 0


for question in questions1:
    question_string = "%s:\n\tA. %s\n\tB. %s\n\tC. %s\n\tD. %s\n\tE. %s\n[Type either a/b/c/d/e]:  " % (question[0], question[1], question[2], question[3], question[4], question[5])
    answer = raw_input(question_string).lower()
    while answer not in ("a", "b", "c", "d", "e"):
        print("Please choose A, B, C, D, E")
        answer = raw_input(question_string).lower()
    if answer == "a":
        counter_a += 1
    if answer == "b":
        counter_b += 1
    if answer == "c":
        counter_c += 1
    if answer == "d":
        counter_d += 1
    if answer == "e":
        counter_e += 1
#print "A total is %d" % counter_a
#print "B total is %d" % counter_b


if all(x < counter_a for x in (counter_b, counter_c, counter_d and counter_e)):
    print 'openness to experience'
elif all(x < counter_b for x in (counter_a, counter_c, counter_d and counter_e)):
    print 'conscientiousness'
elif all(x < counter_c for x in (counter_b, counter_a, counter_d and counter_e)):
    print 'extraversion'
elif all(x < counter_d for x in (counter_b, counter_c, counter_a and counter_e)):
    print 'agreeableness'
elif all(x < counter_e for x in (counter_b, counter_c, counter_d and counter_a)):
    print 'asshole'
else:
    print 'all round panda'
