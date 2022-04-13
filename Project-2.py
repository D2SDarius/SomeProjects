import time
hmetor = 100.00
start_time = time. time()

while True:
    print("--- %s seconds ---" % (time.time() - start_time))
    hmetor -= 0.2
    print("Hmetor: " + str(hmetor))
    time.sleep(3)

