
file_path="/Users/gangjihun/python/mission_computer_main.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print(f"파일'{file_path}'을 찾을 수 없습니다.")
except PermissionError:
    print(f"'{file_path}'의 접근권한이 없습니다.")
except IsADirectoryError :
    print(f"디렉터리가 아닌 파일경로를 입력하세요.")
except TimeoutError:
    print(f"타임아웃 오류 발생")
except Exception as e:
    print(f"오류 발생 : {e}")
