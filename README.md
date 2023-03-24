# GetIP CLI

Utility to get geodata by IP or to get your public IP.

# Installation:

## Installation for Windows:

Download `getip.exe`, put it in any directory and specify the path to this directory in PATH.

## Instalation for Linux:

You must have the `setuptools` package installed.

```
pip3 install setuptools
```

Open the terminal in the utilities folder (where it is located setup.py ) and enter the command:

```
sudo python3 setup.py install
```

# Using:

## Get data of your current public IP:

If `getip.exe` in the PATH on Windows:
```
getip
```

## Get data of other IP:

```
getip -i IP-address
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