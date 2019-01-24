import openpyxl

 
def readDataToExcel():
    # 엑셀파일 열기
    wb = openpyxl.load_workbook('accounts/soda.xlsx')
    
    # 현재 Active Sheet 얻기
    ws = wb.active
    # ws = wb.get_sheet_by_name("Sheet1")
    
    data = []
    # 국영수 점수를 읽기
    for r in ws.rows:
        name = r[0].value
        studentNumber = r[1].value
        phoneNumber = r[2].value

        info = {}
        info['name'] = name
        info['studentNumber'] = studentNumber
        info['phoneNumber'] = phoneNumber

        data.append(info)
        print(name, studentNumber, phoneNumber)
    
    print(data)
    
    wb.close()

    return data
