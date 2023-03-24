# GetIP CLI

Utility to get geodata by IP or to get your public IP.

# Installation:

## Installation for Windows:

Download `getip.exe`, put it in any directory and specify the path to this directory in PATH.

or

Use the installation method described below for Linux, with a slight adjustment of the installation command:

***Note: to use this method, you must have python on your system.***

You must have the setuptools package installed.

```
pip install setuptools
```

Open the terminal in the utilities folder (where it is located setup.py ) and enter the command:

```
python setup.py install
```


## Instalation for Linux:

You must have the `setuptools` package installed.

```
pip install setuptools
```

Open the terminal in the utilities folder (where it is located setup.py ) and enter the command:

```
sudo python3 setup.py install
```

# Using:

You can use the utility without installation by running it as a simple python-script or install it and use it as a CLI-utility directly from the terminal.

## Get data of your current public IP:
### **CLI**:
```
getip
```
or
### **Python-script**:
```
python getip.py
```

## Get data of other IP:
### **CLI:**
```
getip -i IP
```
or
### **Python-script**:
```
python getip.py -i IP
```


## Example output:

```
Ip..................: 0.0.0.0
Success.............: True
Type................: IPv4
Continent...........: Europe
Continent Code......: EU
Country.............: Germany
Country Code........: DE
Region..............: Hesse
Region Code.........: HE
City................: Frankfurt
Latitude............: 0.0
Longitude...........: 0.0
Is Eu...............: True
Postal..............: 00000
Calling Code........: 49
Capital.............: Berlin
Borders.............: AT,BE,CH,CZ,DK,FR,LU,NL,PL
Flag................: https://cdn.ipwhois.io/flags/de.svg
Connection..........: {'asn': 52000, 'org': 'FINE GROUP SERVERS SOLUTIONS LLC', 'isp': 'MIRholding B.V.', 'domain': 'finegroupservers.com'}
Timezone............: {'id': 'Europe/Berlin', 'abbr': 'CET', 'is_dst': False, 'offset': 3600, 'utc': '+01:00', 'current_time': '2023-03-23T20:17:56+01:00'}
```