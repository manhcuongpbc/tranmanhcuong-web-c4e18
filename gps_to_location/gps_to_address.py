import sys
import googlemaps
from datetime import datetime
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
gmaps = googlemaps.Client(key=sys.argv[1])
output = open('out.txt', 'w', encoding='utf-8')
with open(sys.argv[2],'r') as input_file:
    for line in input_file:
        if line[:-1]:
            fields = line[:-1].split(",")
            reverse_geocode_result = gmaps.reverse_geocode((float(fields[0]),float(fields[1])))

            address = reverse_geocode_result[0]["formatted_address"]
            # print(address,end="\t",file = output)
            parts = address.split(",")
            print(parts[-2][1:],file = output)
            # print(parts[-3][1:] + " " +parts[-2][1:],file = output)
            # print()
        else:
            print("", file = output)
# AIzaSyA02GezIomcFpjlYXTZh5xlS_ErP222sR8