#전역변수 선언
#재질
material = ''
#지름
diameter = 0
#두께
thickness = 0
#면적
area = 0
#무게
weight = 0

#재질별 밀도
DENSITY = {
    '유리': 2.4,
    '알루미늄': 2.7,
    '탄소강': 7.85
}

#화성 중력 보정 개수
GRAVITY_RATIO = 0.38

def sphere_area(diameter, material = '유리', thickness = 1):
    global area, weight

    #반지름 계산(m --> cm)
    radius_cm = (diameter * 100) / 2

    #반구 표면적: 2 * 𝜋 * r²
    area_cm2 = 2 * 3.141592653589793 * radius_cm ** 2

    #부피 계산: 면적 * 두께
    volume_cm3 = area_cm2 * thickness

    #무게 계산: 부피 * 밀도
    weight_grams = volume_cm3 * DENSITY[material]

    #지구 무게 --> 화성 무게
    weight_kg = (weight_grams / 1000) * GRAVITY_RATIO

    #전역변수에 저장
    area = round(area_cm2, 3)
    weight = round(weight_kg, 3)
    
    #결과 출력
    print(f'재질 -> {material}, 지름 -> {round(diameter, 3)}, 두께 -> {round(thickness, 3)}, 면적 -> {area}, 무게 -> {weight} kg')

while True:
    print('\n돔 계산기 (종료하려면 e 입력)')

    #지름 입력
    while True:
        d = input('지름 입력(m):')
        if d.lower() == 'e':
            exit()
        try:
            diameter = float(d)
            if diameter <= 0:
                print('error: 지름은 0보다 커야 합니다.')
                continue
            break
        except ValueError:
            print('error: 지름은 숫자로 입력하세요.')

    #재질 입력
    while True:
        m = input('재질 입력(유리, 알루미늄, 탄소강, 기본값: 유리): ').strip()
        if m.lower() == 'e':
            exit()
        if m.strip() == '':
            material = '유리'
            break
        elif m in DENSITY:
            material = m
            break
        else:
            print('error: 유리, 알루미늄, 탄소강 중 다시 선택하세요.')

    #두께 입력
    while True:
        t = input('두께 입력(cm, 기본값: 1): ')
        if t.lower() == 'e':
            exit()
        if t.strip() == '':
            thickness = 1
            break
        try:
            thickness = float(t)
            break
        except ValueError:
            print('error: 두께를 숫자로 입력하세요.')

    sphere_area(diameter, material, thickness)