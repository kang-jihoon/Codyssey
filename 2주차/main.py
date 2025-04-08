def read_log_file(file_path):
    try:
        with open(file_path,'r', encoding='utf-8') as file:
            return[tuple(line.strip().split(',',1))for line in file if ',' in line]
    except (FileNotFoundError, IOError):
        print('파일 읽기 오류'); return[]

def save_as_json(logs, output_path):
    try:
        with open(output_path,'w',encoding='utf-8') as file:
            file.write('{\n'+',\n'.join(f'   "{i}": {{"timestamp": "{t}", "message": "{m}"}}' for i, (t, m) in enumerate(logs)) + '\n}')
    except IOError:
        print('파일 저장 오류')

def search_logs_file(logs, keyword):
    return [log for log in logs if keyword in log[1]]

if __name__=='__main__':
    logs = read_log_file('mission_computer_main.log')

    if logs:
        logs.sort(reverse=True, key=lambda x:x[0])
        save_as_json(logs, 'mission_computer_main.json')

        print('JSON 저장 완료\n', logs)
        
        results = search_logs_file(logs, input('찾고 싶은 특정문자를 입력하세요: '))
        print('검색 결과:', results if results else '찾고자 하는 특정문자가 없습니다.')
