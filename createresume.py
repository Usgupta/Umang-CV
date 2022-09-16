import shutil
import datetime

print("start")

yr = datetime.datetime.now().year
original = r'main.pdf'

target = r'UMANG GUPTA RESUME ' + str(yr)

shutil.copyfile(original, target)

print("end")
