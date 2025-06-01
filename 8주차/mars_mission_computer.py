import random
import time
import platform
import os
import psutil

class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illumunance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }

    def set_env(self):
        datas = self.env_values
        datas['mars_base_internal_temperature'] = random.randint(18,30)
        datas['mars_base_external_temperature'] = random.randint(0,21)
        datas['mars_base_internal_humidity'] = random.randint(50,60)
        datas['mars_base_external_illumunance'] = random.randint(500,715)
        datas['mars_base_internal_co2'] = random.randint(2,10)/100
        datas['mars_base_internal_oxygen'] = random.randint(4,7)
    
    def get_env(self):
        os.makedirs('1/1.6', exist_ok=True)
        with open('1/1.6/environment.log', 'w') as f:
            f.write(str(self.env_values))
        return self.env_values

class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illumunance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen':0.0
        }
        self.history = {key: [] for key in self.env_values}
        self.ds = DummySensor()


    def get_sensor_data(self):
        start_time = time.time()
        try:
            while True:
                self.update_env_values()
                self.print_env_values()

                elapsed = int(time.time() - start_time)
                if elapsed > 0 and elapsed % 300 == 0:
                    self.print_average()

                time.sleep(5)
        except KeyboardInterrupt:
            print("System stopped....")
    
    def update_env_values(self):
        self.ds.set_env()
        current = self.ds.get_env()

        for key in self.env_values:
            value = current[key]
            if value is not None:
                self.env_values[key] = value
                self.history[key].append(value)
                if len(self.history[key]) > 60:
                    self.history[key].pop(0)

    def print_env_values(self):
        print("{")
        for key in self.env_values:
            print(f'    "{key}": {round(self.env_values[key], 3)}')
        print("}")

    def print_average(self):
        print("\n=== Average ===")
        for key in self.history:
            values = self.history[key]
            if values:
                total = 0.0
                for v in values:
                    total += v
                avg = total / len(values)
                print(f"{key}: {round(avg, 3)}")
        print("==========================\n")
    
    def get_mission_computer_info(self):
        try:
            os_name = platform.system()
            os_version = platform.version()
            cpu_type = platform.processor()
            cpu_cores = os.cpu_count()
            mem_bytes = psutil.virtual_memory().total
            mem_gb = round(mem_bytes / (1024 ** 3), 2)

            print('{')
            print(f'    "os": "{os_name}",')
            print(f'    "os version": "{os_version}",')
            print(f'    "cpu type": "{cpu_type}",')
            print(f'    "cpu cores": "{cpu_cores}",')
            print(f'    "memory size(gb)": "{mem_gb}",')
            print('}')
        
        except Exception as e:
            print(f'시스템 정보를 가져오는 중 오류 발생: {e}')

    def get_mission_computer_load(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            mem_usage = psutil.virtual_memory().percent

            print('{')
            print(f'    "cpu usage(%)": {cpu_usage}')
            print(f'    "memory usage(%)": {mem_usage}')
            print('}')

        except Exception as e:
            print(f'시스템 부하 정보를 가져오는 중 오류 발생: {e}')


RunComputer = MissionComputer()

RunComputer.get_mission_computer_info()
RunComputer.get_mission_computer_load()
