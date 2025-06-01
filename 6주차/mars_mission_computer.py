import random
import os

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

ds = DummySensor()
ds.set_env()
print(ds.get_env())