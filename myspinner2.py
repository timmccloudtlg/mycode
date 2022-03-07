#!/usr/bin/env python3


from threading import Timer

def exit():
    print("Times UP!!!!!!!!!!")

input_time=int(input("Set time limit: "))
t = Timer(input_time, exit)
t.start()
prompt = "You have %d seconds to choose the correct answer.................\n" % input_time
answer = input(prompt)
t.cancel()
