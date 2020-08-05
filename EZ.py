# OpenOPS - XtremIO, Dell EMC XtremIO Monitor
# XtremIO: X1
# XMS Version: 6.3.1 build 5_hotfix_1
# Programe: Python 3.8
# Stage: prototype
# Author: QD888
# Tested: 5th Aug. 2020

# Import libraries
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib
from urllib.parse import urlencode
from urllib.parse import quote


# Set up endpoint and authentication credentials
endpoint = 'https://IP address'
username = 'username'
password = 'password'
auth = HTTPBasicAuth(username, password)

# Get API address
api = '/api/json/v2/types/'
url = endpoint + api

# For GET requests
response = requests.get(url, auth=auth, verify=False)
payload = json.loads(response.text)

# Example: Disk information
api = '/api/json/v2/types/ssds'
url = endpoint + api
resDisk = requests.get(url, auth=auth, verify=False)
plDisk = json.loads(resDisk.text)

# Example: Performance information
api = '/api/json/v2/types/performance?entity=Target&prop=avg__rd_iops'
url = endpoint + api
resPerf = requests.get(url, auth=auth, verify=False)
plPerf = json.loads(resPerf.text)
