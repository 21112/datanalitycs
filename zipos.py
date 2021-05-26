import glob
import re


swords = ['<bi8>Put cartridge at: MODULE[', 'Got cartridge from: MODULE[', '@identify OK', 'get l', 'put t', 'get m','put m',' stall ']

h =[]

def stream_lines(file_name):
    with open(f"{file_name}", 'r') as f:
        r = f.readlines()
        return r
sn_nummer= []  
bib_id_kartuschen = []
set_sn= set(bib_id_kartuschen)
mo = None
files = [f for f in glob.iglob('DeanStreet/*.log')]
for i in files:
    g = stream_lines(i)
    for i in range(len(g)):
        # if '<bi8>Put cartridge at: MODULE[' in g[i]:
        #     r = re.search("\[\d{1,5}\]", g[i])
        #     mod = str(r[0]).lstrip("[").rstrip("]")
        #     print("Put cartridge at:"+mod)
        # if 'Got cartridge from: MODULE[' in g[i]:
        #     r = re.search("\[\d{1,2}\]", g[i])
        #     mod = str(r[0]).lstrip("[").rstrip("]")
        #     print("Got cartridge from:" + mod)
            
        if '@identify OK' in g[i]:
            r = re.search("\d{20,27}",g[i])
            try:
                bib_id_kartuschen.append(str(r[0].lstrip(' ').rstrip('\n')))
                # print(r[0])
            except TypeError:
                pass
        # if 'get l' in g[i]:
            
        #     h.append(g[i])

            # print(g[i])
        # if 'put t' in g[i]:
        #     print(g[i])
        if ' get m' in g[i]:
            gm = re.search('get\sm\d{1,2}\s',g[i])
            mo = gm[0]
            
            if ' 0405' in g[i]:

                r = re.search("\s\d{20,27}", g[i])
                nn = r[0].lstrip(' ')
                try:
                    if nn not in bib_id_kartuschen:
                        bib_id_kartuschen.append(str(r[0].strip('\n')))
                        
                    else:
                        pass
                except TypeError:
                    pass
        if 'put m' in g[i]:
            pm = re.search('put\sm\d{1,2}\s',g[i])
            mo = pm[0]
            print(pm[0])
            

        #     pass
        # if ' stall ' in g[i]:
        #     print(g[i-3],g[i-1],'*********************************************************' + g[i])
        

        # if '<bi8>Failure happened, Failure Information:' in g[i]:
        #     t = re.search('(\d{1,2}\/\d{1,2}\/\d{4}\s\d{1,2}:\d{1,2}:\d{1,2})',g[i-1])
        #     rp = t[0].split('/')
        #     stall_time = str(rp[1])+'/'+str(rp[0])+'/'+str(rp[2])
        #     failed_command = g[i+1].lstrip('FailedCommand: ').rstrip('\n')
        #     failure_reason = g[i+2].lstrip('FailureReason: ').rstrip('\n')
        #     gripper_state = g[i+3].lstrip('GripperState: ').rstrip('\n')
        #     if failed_command == 'RECOVER_TO_SAFE_GANTRY_POSITION':
        #         mo = 'Gantry'
        #     print('STALL TIME:'+stall_time+'\n'+'FailedCommand:'+failed_command+'\n'+ 'FailureReason:'+failure_reason+'\n'+'GripperState:'+gripper_state)
        #     print(mo,'\n')
        # if 'has encountered' in g[i]:
        #     rf = re.findall('module\s.+\shas|encountered\s.+]',g[i])
        #     mod = rf[0].strip("module ").strip(" has").strip('[').strip(']')
        #     print('Modul:'+mod)
        #     st = rf[1].strip('encountered ').strip('[').strip(']')
        #     print('Stall:'+ st)
        #     for n in range(1,5):
        #         if 'SN' in g[i+n]:
        #             r = re.search("\d+",g[i+n])
        #             sn = r[0]
        #             print('Kartuschen SN:'+ str(sn), '\n')
        #             if sn:
        #                 sn_nummer.append(sn)

            
  
print(len(bib_id_kartuschen))
print(len(set_sn))                      

            # for l in sn_nummer:
                
            #     for n in set_sn:
            #         if l in n:
            #             print(n)
