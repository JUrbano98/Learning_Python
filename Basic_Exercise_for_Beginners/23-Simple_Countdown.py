'''
Write a code to create a simple countdown timer of 5 seconds using a while
loop. Once the timer finishes (when the remaining time reaches zero),
print a “Time’s up!” message.
'''


import time


def final_countdown(secs):
    for i in range(secs):
        print("Time remaining: ", secs - i, "seconds.")
        time.sleep(1)
    print("Time's up!")


final_countdown(5)
