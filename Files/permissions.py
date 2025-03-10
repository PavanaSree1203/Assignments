def read_from_index(f,i,n):
    with open(f,'rb')as fi:fi.seek(i);print(fi.read(n).decode('utf-8','ignore'))

read_from_index("my_file.txt",10,5)