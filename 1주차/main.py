print('Hello Mars\n')

f_p="/Users/gangjihun/Downloads/mission_computer_main.log"

try:
    with open(f_p, "r", encoding="utf-8") as file:
        lines = file.readlines()
except FileNotFoundError as e:
     print("error: ", e)
     with open("error_f.py", 'a') as error_f:
         error_f.write(str(e))
         error_f.write('\n')
else: 
     print("순차")
     for line in lines:
         print(line, end='')
         
     print("\n역순")
     for line in lines[::-1]:
         print(line, end='')