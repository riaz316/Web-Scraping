import openpyxl

# load workbook and sheet
wb = openpyxl.load_workbook("authentic.xlsx")
sheet = wb.active

# G477


for i in range(237, 500):
    cell = 'G' + str(i)
    print(cell)
    # Load data
    detail = sheet[cell].value
    # remove english character
    corrected = ""
    wordList = []
    for word in detail.split():
        if (not word[0] == 'g') or (not word[1] == 'a'):
            corrected += " " + word
    sheet[cell] = corrected

print(corrected)

wb.save('authentic.xlsx')
