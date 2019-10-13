# pip install xlrd
import xlrd 

loc = ("./test.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

print(sheet.cell_value(0, 0))
print(sheet.nrows) 
print(sheet.ncols) 