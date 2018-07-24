
class fileoperation:

    filename = 'C:/Users/shivraj/Desktop/raj.txt'
    def __init__(self):
        pass
    def fileread(self):
        fh = open(fileoperation.filename,'r')
        listfromfile=fh.readlines()
        print(listfromfile)
        return listfromfile
        fh.close()

    def filewrite(self,listtofile):
        fh = open(fileoperation.filename, 'w')
        lines_of_text = listtofile
        for item in lines_of_text:
            l=4
            for i in item:
                fh.write(i)
                if l>=3:
                    fh.write(',')
                    l-=1
            fh.write('\n')

        fh.close()

def main():
    d=fileoperation()
    listtofile=[['admin','admin123','success'],['admin', 'NA','psw cant be empty'],['NA','admin123','Username cant be empty'],['admin123','admin123','invalid username or psw']]
    d.filewrite(listtofile)
    d.fileread()
if __name__ == '__main__':
    main()