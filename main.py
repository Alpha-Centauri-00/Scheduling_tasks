import yaml
import schedule
import subprocess
from datetime import datetime
from schedule import every, repeat




End = "11:47:00"

with open("conf.yml","r") as f:
    confi = yaml.safe_load(f)

system_test = confi["tasks"]["system"]
smoke_test = confi["tasks"]["smoke"]
regression_test = confi["tasks"]["regression"]



@repeat(every(10).seconds)
def smoke_testing():
    subprocess.run(smoke_test)

@repeat(every(20).seconds)
def system_testing():
    subprocess.run(system_test)

@repeat(every(5).seconds)
def regression_testing():
    subprocess.run(regression_test)




while True:
    schedule.run_pending()
    
    Time = datetime.now().strftime("%H:%M:%S")
    if Time == End:
        break
