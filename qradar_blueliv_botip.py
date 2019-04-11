import logging
from sdk.blueliv_api import BluelivAPI
import requests
import json
import urllib3
urllib3.disable_warnings()

qradar_auth_key = ""
qradar_ref_set = ""
qradar_server = ""
QRadar_POST_url = "https://" + qradar_server + "/api/reference_data/sets/bulk_load/" + qradar_ref_set
QRadar_headers = {'SEC': '', 'Content-Type': 'application/json', 'Version': '9.0', 'Accept':'application/json'}
Qradar_cert = 'qradar.pem'

LOG_FILE = 'blueliv.log'
logging.basicConfig(filename=LOG_FILE)
logger = logging.getLogger('main')

proxy = None

"""
proxy = {'http': 'x.x.x.x:80',
         'https': 'x.x.x.x:80'}
"""
api = BluelivAPI(base_url='', token='', log_level=logging.INFO, proxy=proxy)

# Get last full bot ips
response = api.bot_ips.recent('full')

ip_list = []
counter = 0
for i in response.items:
    ip_list.append(response.items[counter]['ip'])
    counter += 1

json.dumps(ip_list)

print(ip_list)

p = requests.post(QRadar_POST_url, headers=QRadar_headers, json=ip_list, verify=Qradar_cert)
p.raise_for_status() #Raise exception on HTTP errors
