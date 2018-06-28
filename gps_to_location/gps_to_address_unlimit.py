import sys
from geopy.geocoders import ArcGIS
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
geolocator = ArcGIS()
fout = open(sys.argv[2],'w',  encoding = 'utf-8')
with open(sys.argv[1]) as fin:
    for line in fin:
        line = line.strip()
        location = geolocator.reverse(line)
#        location = geolocator.reverse("52.509669, 13.376294")
        fields = location.address.split(',')
        print(fields[-2].strip(), file =fout)
