import xlrd

def get_initial_dat():
    data = xlrd.open_workbook('fixture.xlsx')
    table = data.sheets()[0]


    collect = {}
    key = ''
    value = ''

    for i in range(table.nrows):
        if i % 3 == 0:
            key = table.row_values(i)[0]
            collect[key] = []
            if len(table.row_values(i)) >= 2:
                collect[key] = [v for v in table.row_values(i)[1:] if v]
        else:
            if table.row_values(i)[0]:
                collect[key].extend(table.row_values(i))

    return collect
