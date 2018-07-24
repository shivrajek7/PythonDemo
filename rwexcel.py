from rwfile import fileoperation
import xlrd as read
import xlwt as write


class exceloperation:
    filePath = 'C:\\Users\shivraj\Desktop\\test.xls'
    listOfLines=[]
    readExcelDataList=[]

    def getdatafromfile(self):
        d = fileoperation()
        list1 = d.fileread()
        exceloperation.listOfLines=list1
     #   fh=fileoperation()
      #  exceloperation.listofLines=fh.fileread()
       # return exceloperation.listofLines


    def writetoexcel(self):
        d = fileoperation()
        list1 = d.fileread()
        workBook = write.Workbook()
        userInfoSheet = workBook.add_sheet('UserInfo')
        count = 0
        cols = []
        for item in list1:
            for words in item.split(','):
                cols.append(words)

        for num in range(list1.__len__()):
            row = userInfoSheet.row(num)
            for item in range(3):
                row.write(item, cols.__getitem__(count))
                count += 1

        workBook.save(exceloperation.filePath)



    def readfromexcel(self):
        workbook = read.open_workbook(exceloperation.filePath)
        userinfosheet = workbook.sheet_by_name("UserInfo")

        for rindex in range(0, userinfosheet.nrows):
            for cindex in range(0, userinfosheet.ncols):
                exceloperation.readExcelDataList.append(userinfosheet.cell(rindex, cindex).value)
        print(exceloperation.readExcelDataList)
        return exceloperation.readExcelDataList
        

if __name__ == '__main__':
    k=exceloperation()
    k.writetoexcel()
    k.readfromexcel()





