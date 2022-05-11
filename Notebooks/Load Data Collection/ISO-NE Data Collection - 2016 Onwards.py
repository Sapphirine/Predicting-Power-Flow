from pyiso.base import BaseClient
from pyiso import LOGGER
from pyiso import client_factory
import os
from os import environ
import pandas as pd
import time
import calendar

os.environ["ISONE_USERNAME"] = "rr3417@columbia.edu"
os.environ["ISONE_PASSWORD"] = "4ryhj281"

isone = client_factory('ISONE', timeout_seconds=60)

for year in range(2022,2024):
    for month in range(1,5):
        last_date = calendar.monthrange(year, month)[1]
        data = isone.get_load(latest=False, start_at=f'{month}/01/{year}', end_at=f'{month}/{last_date}/{year}')
        temp_df = pd.DataFrame(data)
        temp_df.to_csv(f"{year}-{month:02d}.csv", index=False)
        print(f"{year}-{month:02d} done")
        #print(temp_df)
    
print("Done")