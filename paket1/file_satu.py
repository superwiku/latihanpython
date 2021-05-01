import paket2.file_dua
print("file satu __name__ di set ke {}".format(__name__))
def fungsi3():
    print('fungsi 3 dieksekusi')
def fungsi4():
    print('fungsi 4 dieksekusi')

if __name__ == '__main__':
    fungsi3()
else:
    fungsi4()