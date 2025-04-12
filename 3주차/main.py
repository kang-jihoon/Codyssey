# 파일 경로 설정
file_path = "./Mars_Base_Inventory_List.csv"
csv_out_path = "./Mars_Base_Inventory_Danger.csv"
binary_out_path = "./Mars_base_Inventory_List.bin"

try:
    # 파일 열기
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Mars_Base_Inventory_List.csv 파일 내용 출력
    print("\n=============  Mars_Base_Inventory_List.csv 파일 내용  =============")
    for line in lines:
        print(line, end='')

    # 헤더 확인
    header = lines[0].strip().split(",")
    expected_header = ["Substance", "Weight (g/cm³)", "Specific Gravity", "Strength", "Flammability"]
    if header != expected_header:
        print("Error: 로그 파일 형식이 다릅니다.")
        exit()

    # 데이터 리스트 저장
    log_list = []
    for line in lines[1:]:  # 헤더 제외
        parts = line.strip().split(",", 4)
        if len(parts) == 5:
            Substance = parts[0].strip()
            Weight = parts[1].strip()
            Specific_Gravity = parts[2].strip()
            Strength = parts[3].strip()

            try:
                Flammability = float(parts[4].strip())  # 인화성 (실수형 변환)
                log_list.append((Substance, Weight, Specific_Gravity, Strength, Flammability))
            except ValueError:
                print(f"변환 오류: {parts} - 인화성 값이 실수가 아닙니다.")
except FileNotFoundError:
    print("파일을 찾지 못하였습니다.")
try:
    # 파일 열기
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # 인화성 기준 내림차순 정렬
    log_list.sort(key=lambda x: x[4], reverse=True)

    # 인화성 지수 0.7 이상인 경우에 출력
    print("\n=============  인화성 지수 0.7 이상 목록  ============")
    danger_list = [log for log in log_list if log[4] >= 0.7]
    for log in danger_list:
        print(log)

    # 인화성 지수 0.7 이상 목록 csv 파일로 저장
    with open(csv_out_path, "wt", encoding="utf-8") as file:
        file.write(",".join(header) + "\n")  # 헤더 추가
        for log in danger_list:
            file.write(",".join(map(str, log)) + "\n")

    print(f"\n인화성 지수 0.7 이상 데이터를 csv 파일 : {csv_out_path}에 저장")
except FileNotFoundError:
    print("파일을 찾지 못하였습니다.")
except IsADirectoryError:
    print("Error: 지정된 경로가 디렉터리입니다.")
try:
    # 파일 열기
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # 이진 파일로 저장 (정렬된 전체 log_list 기준)
    with open(binary_out_path, "wb") as file:
        for log in log_list:
            line = ",".join(map(str, log)) + "\n"
            file.write(line.encode("utf-8"))  # 문자열을 바이트로 변환하고 저장

    print(f"인화성 순 정렬 데이터를 이진 파일 : {binary_out_path}에 저장")

    # 이진 파일 다시 읽어 출력
    print("\n============  이진 파일에서 읽은 데이터  ============")
    with open(binary_out_path, "rb") as file:
        binary_content = file.readlines()
        for line in binary_content:
            print(line.decode("utf-8").strip())  # 바이트를 문자열로 변환 후 출력
except FileNotFoundError:
    print("파일을 찾지 못하였습니다.")
except PermissionError:
    print("Error: 파일을 열 권한이 없습니다.")