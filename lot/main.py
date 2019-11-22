import random
staff = {'id':[], }
# results = [['总人数',{'乘车点1人数':0, },['staffid', ]], [], ]
results = [[0, {},[]], [], ]

valid_roads = list(range(10, 17))
limit_num = 80

for i in range(10):
    wishes = []
    for staffid, road in staff.items():
        wishes.append((staffid, road))
    free_wishes = [w for w in wishes if w[-1] <= 9]
    limit_wishes = [w for w in wishes if w[-1] > 9]
    for free_road in free_wishes:
        staffid = free_road[0]
        peoples = staff[staffid][1]
        results[i][0] += peoples
        if staff[staffid][2] == '是':
            station = staff[staffid][1]
            if station in results[i][1]:
                results[i][1][station] += peoples
            else:
                results[i][1][station] = peoples
        del staff[staffid]

    random.shuffle(limit_wishes)
    for limit_road in limit_wishes:
        staffid = limit_road[0]
        peoples = staff[staffid][1]
        if limit_road in valid_roads:
            peoples = staff[staffid][1]
            if results[i][0] + peoples > 80:
                continue
            else:
                results[i][0] += peoples
                if results[i][0] >= 80:
                    del valid_roads[i]
                if staff[staffid][2] == '是':
                    station = staff[staffid][1]
                    if station in results[i][1]:
                        results[i][1][station] += peoples
                    else:
                        results[i][1][station] = peoples
                del staff[staffid]

print(len(staff))



        

    

