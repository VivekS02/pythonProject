import openpyxl

book = openpyxl.load_workbook("C:\\Users\\Vivek\\OneDrive\\Desktop\\pythondata.xlsx")
sheet = book.active

cell = sheet.cell(row=2,column=4)
print(cell.value)