# ip2country

Little python script to take in a file of IP addresses and return CSV output to stdout of:

* ip_address
* country(code)
* region/state
* city

This makes use of the excellent (and free) [ip2geotools](https://pypi.org/project/ip2geotools/) python library.

## Installation

* Create a new python3 virtual environment
* pip install -r requirements.txt

## Usage

```bash
python ip2country.py IP_ADDRESS_LIST_FILENAME
```

The `IP_ADDRESS_LIST_FILENAME` should just contain ipv4 addresses- one on each line

## Example output

```bash
$ echo "8.8.4.4" > test.txt

$ python ip2country.py test.txt
added 8.8.4.4
1 ip addresses added for lookup.
"8.8.4.4","US","California","Mountain View"
$ 
```
