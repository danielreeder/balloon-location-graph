import aprslib
import csv

def callback(packet):
    if (packet.get('from') == 'KK7MXV-11' or packet.get('from') == 'KO4TL-11'):
        sign = packet.get('from')
        keys = list(packet.keys())
        with open(sign + '.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writerow(packet)
            print(packet)
AIS = aprslib.IS(callsign="KK7MXV-11", passwd="-1")
AIS.connect()
# by default `raw` is False, then each line is ran through aprslib.parse()
AIS.consumer(callback)