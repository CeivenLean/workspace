from openpyxl import load_workbook


wb = load_workbook('/Users/xxxl/VSProjects/workspace/02excel/test.xlsx')
sheet = wb.active
for cells in sheet.iter_cols(): 
    # print(cells)
    for cell2 in cells: 
        if cell2.value is not None: 
            # print(cell2.value)
            # print(type(cell2.value))
            info2 = str(cell2.value).find('str2\'')
            if info2 == 0: 
                print(cell2.row,cell2.column)
                print(cell2.data_type)
                
