import requests
import re
import pandas as pd

chrName = input('Enter Character Name : ').title()
x = requests.get(f'https://rickandmortyapi.com/api/character/?name={chrName}')


details = x.json()['results']
INFO = []
for i in details:
    eps = ''.join(i['episode'])
    epsNo = re.findall('\d+',eps)
    
    INFO.append((i['location']['name'], epsNo))


title = f'Chracter : {chrName}'.center(150)
lenofstar = 70
print('\n\n')
print('#'*lenofstar)
print(f'Chracter : {chrName}'.center(50))
print('#'*lenofstar)
print('LOCATION'.ljust(50)+'EPISODE'.rjust(10))

for loc, ep in INFO:
    print('.'*lenofstar)
    for i in ep:
        print(f'{loc.ljust(50)}{i.rjust(10)}')  
print('#'*lenofstar)

df = pd.DataFrame(INFO)
df.rename(columns={0:'LOCATION', 1:'EPISODE'}, inplace=True)

df.to_excel(f'./{chrName}.xlsx', index = False)