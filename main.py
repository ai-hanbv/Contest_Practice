names = ['김현도', '허도용', '박인석', '이동완', '손진영', '이지 향', '한승민', '카 림바예프', '김영현', '이인국', '박찬종', '김민중', '이종 현', '김정현', '류 재철', '김동훈', ' 신희경', '이상우', '최민국', '손정길', '박동준', '최인규', '김범근', '이호인']
data = []
def add_people(name, department, vacation):
    r_d = {
        "name" : name,
        "department" : department,
        "vacation" : vacation
    }
    data.append(r_d)

def update_people(*kwargs):
    '''
    Update name = 1, department = 2, vacation = 3
    '''
    