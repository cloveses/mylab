import xlrd
import random

def get_file_datas(filename,row_deal_function=None,grid_end=0,start_row=1):
    """start_row＝1 有一行标题行；gred_end=1 末尾行不导入"""
    """row_del_function 为每行的数据类型处理函数，不传则对数据类型不作处理 """
    wb = xlrd.open_workbook(filename)
    ws = wb.sheets()[0]
    nrows = ws.nrows
    datas = []
    for i in range(start_row,nrows-grid_end):
        row = ws.row_values(i)
        # print(row)
        if row_deal_function:
            row = row_deal_function(row)
        datas.append(row)
    return datas

def row_data_clean(row):
    row = [str(r) for r in row]
    row[0] = int(float(row[0]))
    row[1] = int(float(row[1]))
    for i in range(4, 14):
        row[i] = ord(row[i]) - 64
    return row
datas = get_file_datas('副本测试数据.xlsx', row_data_clean)
# for data in datas:
#     print(data)

staff = {}
for data in datas:
    staff[data[0]] = data
# staff = {'id':[], }
# results = [['总人数',{'乘车点1人数':0, },['staffid', ]], [], ]
results = [[0, {},[]] for i in range(17) ]

valid_roads = list(range(10, 18))
print('valid_roads:', valid_roads, '\n')
limit_num = 80

for i in range(10):
    if len(staff) == 0:
        break

    wishes = []
    for staffid, staff_data in staff.items():
        wishes.append((staffid, staff_data[i+4]))
    print('wishes:', wishes, '\n')
    free_wishes = [w for w in wishes if w[-1] <= 9]
    limit_wishes = [w for w in wishes if w[-1] > 9]
    print('free_wishes', free_wishes, '\n')

    for free_road in free_wishes:
        staffid = free_road[0]
        staff_road = free_road[-1]-1
        peoples = staff[staffid][1]
        results[staff_road][0] += peoples
        results[staff_road][2].append(staffid)
        if staff[staffid][2] == '是':
            station = staff[staffid][3]
            if station in results[staff_road][1]:
                results[staff_road][1][station] += peoples
            else:
                results[staff_road][1][station] = peoples
        del staff[staffid]

    random.shuffle(limit_wishes)
    print('limit_wishes', limit_wishes, '\n')
    for limit_road in limit_wishes:
        staffid = limit_road[0]
        peoples = staff[staffid][1]
        staff_road = limit_road[-1]

        if staff_road in valid_roads:
            # print('...........')
            staff_road -= 1
            peoples = staff[staffid][1]
            if results[staff_road][0] + peoples > 80:
                continue
            else:
                results[staff_road][0] += peoples
                results[staff_road][2].append(staffid)
                if results[staff_road][0] >= 80:
                    valid_roads.remove(limit_road[-1])
                if staff[staffid][2] == '是':
                    station = staff[staffid][3]
                    if station in results[staff_road][1]:
                        results[staff_road][1][station] += peoples
                    else:
                        results[staff_road][1][station] = peoples
                del staff[staffid]

print(len(staff))
for index, i in enumerate(results):
    print(index+1, i[:2])

