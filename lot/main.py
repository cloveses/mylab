staff = {'id':[], }
results = [['总人数',{'乘车点1人数':0, },['staffid', ]], [], ]

for i in range(10):
    wishes = []
    for staffid, road in staff.items():
        wishes.append((staffid, road))
    free_roads = [w for w in wishes if w[-1] <= 9]
    for free_road in free_roads:
        
