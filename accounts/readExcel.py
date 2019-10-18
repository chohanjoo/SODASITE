import openpyxl

 
def readDataToExcel():
    # 엑셀파일 열기
    wb = openpyxl.load_workbook('accounts/soda.xlsx') # 배포시 경로에 맞게 설정해줘야한다.
    
    # 현재 Active Sheet 얻기
    ws = wb.active
    # ws = wb.get_sheet_by_name("Sheet1")
    
    data = []
    for r in ws.rows:
        name = r[0].value
        studentNumber = r[1].value
        email = r[2].value

        info = {}
        info['name'] = name
        info['studentNumber'] = studentNumber
        info['email'] = email

        data.append(info)
    
    
    wb.close()

    return data
