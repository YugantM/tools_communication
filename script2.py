# receiver

import json,os
import pandas as pd

data = os.popen("python3 script1.py")

#print()
print(pd.read_json(data.read(),orient='index'))