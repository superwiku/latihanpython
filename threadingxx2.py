import threading
import time
def fungsi_satu(nm):
    print("Thread {} : mulai\n".format(nm))
    time.sleep(5)
    print("Thread {} : selesai\n".format(nm))
def fungsi_dua(nm2):
    print("Thread {} : mulai\n".format(nm2))
    time.sleep(4)
    print("Thread {} : selesai\n".format(nm2))
def fungsi_tiga(nm3):
    print("Thread {} : mulai\n".format(nm3))
    time.sleep(3)
    print("Thread {} : selesai\n".format(nm3))

if __name__ == '__main__':
    print('thread belum ada\n')
    x=threading.Thread(target=fungsi_satu,args=('aku',))    
    y=threading.Thread(target=fungsi_dua,args=('kamu',))
    z=threading.Thread(target=fungsi_tiga,args=('dia',))
    print('thread sudah ada tapi belum mulai\n')
    x.start()
    z.start()
    y.start()
    print('\n tungguuuu....')
