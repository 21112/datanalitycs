# import zipfile
# import os, os.path
# import sqlite3


# zip_file = './data/Filemail.com files 2021-5-12 ddwapsfodnhdnfg.zip'

# def get_zip(zip_file):
#     z = zipfile.ZipFile(zip_file, 'r')
#     z.extractall('./zipdir/')
#     z.close()

# def gz(path):
#     plu = []
#     g = [f for f in glob.iglob(f'{path}*.zip')]
#     for f in g:
#         get_zip(f'{path}+{f}')


# def get_logfiles():
#     for i in os.listdir('./zipdir'):
#         if i.endswith('.zip'):
#             get_zip(i)
#         elif i.endswith('.log'):
#             g =[f for f in glob.iglob('zipdir/*.log')]
#             for i in g:
#                 with open(f'{i}', 'r') as f:
#                         for line in f:
#                             h = re.search('GOT_CARTRIDGE', line)
#                             if h is not None:
#                                 print(h.group(1))

# zip_names=[]
# p = os.walk('./data')
# for d, r,f in p:
#     for i in f:
#         if i.endswith('.zip'):
#             if i not in zip_names:
#                 zip_names.append(i)
#                 get_zip(f'{d}/{i}')
#             else:
#                 continue