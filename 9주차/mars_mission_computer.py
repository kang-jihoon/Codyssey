import threading
import multiprocessing
import time
import random
import sys

class MissionComputer:
    def get_mission_computer_info(self):
        while True:
            print('[INFO]', 'CPU: 3.2GHz, RAM: 16GB, OS: MarsOS 1.0')
            time.sleep(20)

    def get_mission_computer_load(self):
        while True:
            cpu_load = random.randint(1, 100)
            memory_usage = random.randint(1, 100)
            print('[LOAD]', f'CPU Load: {cpu_load}%, Memory Usage: {memory_usage}%')
            time.sleep(20)

    def get_sensor_data(self):
        while True:
            temperature = random.uniform(-80.0, 20.0)
            radiation = random.uniform(0.1, 5.0)
            print('[SENSOR]', f'Temperature: {temperature:.2f}C, Radiation: {radiation:.2f}mSv')
            time.sleep(5)

run_computer = MissionComputer()

threads = [
    threading.Thread(target=run_computer.get_mission_computer_info, name='computer_info', daemon=True),
    threading.Thread(target=run_computer.get_mission_computer_load, name='computer_load', daemon=True),
    threading.Thread(target=run_computer.get_sensor_data, name='sensor_data', daemon=True),
]
for t in threads:
    t.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('멀티 쓰레드 모니터링 종료')

runComputer1 = MissionComputer()
runComputer2 = MissionComputer()
runComputer3 = MissionComputer()
processes = [
    multiprocessing.Process(target=runComputer1.get_mission_computer_info, name='computer_info'),
    multiprocessing.Process(target=runComputer2.get_mission_computer_load, name='computer_load'),
    multiprocessing.Process(target=runComputer3.get_sensor_data, name='sensor_data'),
]
for p in processes:
    p.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    for p in processes:
        p.terminate()
    print('멀티 프로세스 모니터링 종료')

