import openpyxl

path = "C:/Users/Dell/Desktop/serene.xlsx"
workbook = openpyxl.load_workbook(path)
sheeet = workbook.active

for row in range(1, 6):
    for col in range(1, 4):
        sheeet.cell(row=row, column=col).value = "weclome"
workbook.save(path)