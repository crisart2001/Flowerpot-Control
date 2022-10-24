#Para caja G
#Captura de datos
import statistics
from statistics import mean
import time
import requests
import json


url = "http://201.207.53.225:3031/api/biocarbon/"
valores=['','','']

baja_humedad=15.00
alta_humedad=20.00
sleep_time=900 #15 minutos