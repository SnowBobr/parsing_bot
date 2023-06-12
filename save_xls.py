import xlsxwriter

def writer(parametr):
    book = xlsxwriter.Workbook(r"pars.xlsx")
    page = book.add_worksheet("product")

    row = 0
    column = 0

    page.set_column("A:A", 50)
    page.set_column("B:B", 300)
    page.set_column("C:C", 50)
    page.set_column("C:C", 100)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 1, item[2])
        page.write(row, column + 1, item[3])
        row += 1

    book.close()
