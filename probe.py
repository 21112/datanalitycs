
import glob
import re


def stream_lines(file_name):
    with open(f"{file_name}", 'r') as f:
        r = f.read()
        return r

files = [f for f in glob.iglob('DeanStreet/*.log')]

for i in files:
        g = stream_lines(i)
        f = re.findall("Cartridge at module \[\b\] has encountered \[\b\]", g)
        if f:
                print(f[0])
# for i in range(len(t)):
        
#     if '@identify OK' in t[i]:
#             print(t[i])
#     if 'Put cartridge at:' in t[i]:
#             print(t[i])
    
#     if 'Got cartridge from:' in t[i]:
#             print(t[i])


