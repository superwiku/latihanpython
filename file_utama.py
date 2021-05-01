import paket1.file_satu
print("file utama __name__ di set ke {}".format(__name__))
def fungsi1():
    print ('fungsi 1 dieksekusi')
def fungsi2():
    print ('fungsi 2 dieksekusi')

if __name__ == '__main__':
    fungsi1()
else:
    fungsi2()