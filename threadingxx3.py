import threading
import time
def fungsi(nm):
    print("\nThread {} : mulai".format(nm))
    time.sleep(3)
    print("\nThread {} : selesai".format(nm))


if __name__ == '__main__':
    for index in range(4):
        x=threading.Thread(target=fungsi,args=(index,))  
        x.start()      
        print('\ntungguuuu....')

    