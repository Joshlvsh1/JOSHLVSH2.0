import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("BLAST OFF")

print("how many seconds to count down int:")
seconds = input()
while not seconds.isdigit():
    print("Nahhhh bro not that")
    seconds = input()
seconds = int(seconds)
countdown(seconds)

