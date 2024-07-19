# RIPE-ASN-lookup
This project identifies all ASNs for any given country code (cc) and determines the associated IP prefixes, checking which are advertised. Initially inspired by an interest in the ASNs and IP prefixes for the Faroe Islands (FO), this tool uses RIPE NCC data to provide insights into IP address allocations and advertisement status.


## Generating the example files

### Faroe Islands
```bash
> python3 lookup.py fo
```
Generates a file with the following contents:
```json
{"15389": {"name": "FAROESE-TELECOM-AS - P/F Telefonverkid", "announced": {"ipv4_prefixes": ["81.18.224.0/20", "217.172.80.0/20", "178.19.192.0/20", "88.85.32.0/19", "212.55.32.0/19", "193.34.104.0/22", "185.74.208.0/22", "198.137.136.0/22"], "ipv6_prefixes": ["2a02:e90::/32"]}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": ["2a02:e90::/29"]}}, "20963": {"name": "NEMAFAROE - P/F 20.11.19", "announced": {"ipv4_prefixes": ["81.25.176.0/20", "80.77.128.0/20", "46.227.112.0/21", "185.88.228.0/22"], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "200664": {"name": "PF-FTNET - P/F Net", "announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "206928": {"name": "PF-ELEKTRON - P/F Elektron", "announced": {"ipv4_prefixes": ["185.171.172.0/22"], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "209175": {"name": "KRINGVARP_FOROYA - Kringvarp Foroya", "announced": {"ipv4_prefixes": ["195.80.36.0/22"], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "210417": {"name": "NET2 - P/F Net", "announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}}
```
We can also control the JSON formatting (indentation level):
```bash
> python3 lookup.py fo 4
```
Resulting in a file with the following output:
```json
{
    "15389": {
        "name": "FAROESE-TELECOM-AS - P/F Telefonverkid",
        "announced": {
            "ipv4_prefixes": [
                "81.18.224.0/20",
                "217.172.80.0/20",
                "178.19.192.0/20",
                "88.85.32.0/19",
                "212.55.32.0/19",
                "193.34.104.0/22",
                "185.74.208.0/22",
                "198.137.136.0/22"
            ],
            "ipv6_prefixes": [
                "2a02:e90::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a02:e90::/29"
            ]
        }
    },
    "20963": {
        "name": "NEMAFAROE - P/F 20.11.19",
        "announced": {
            "ipv4_prefixes": [
                "81.25.176.0/20",
                "80.77.128.0/20",
                "46.227.112.0/21",
                "185.88.228.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "200664": {
        "name": "PF-FTNET - P/F Net",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206928": {
        "name": "PF-ELEKTRON - P/F Elektron",
        "announced": {
            "ipv4_prefixes": [
                "185.171.172.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "209175": {
        "name": "KRINGVARP_FOROYA - Kringvarp Foroya",
        "announced": {
            "ipv4_prefixes": [
                "195.80.36.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "210417": {
        "name": "NET2 - P/F Net",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    }
}
```


### Greenland
```bash
> python3 lookup.py gl 4
```
Returns an output file called gl_asn_data_{timestamp}.json with the following contents:
```json
{
    "8818": {
        "name": "Tusass A/S",
        "announced": {
            "ipv4_prefixes": [
                "128.0.70.0/24",
                "178.170.210.0/23",
                "88.83.24.0/21",
                "185.21.228.0/22",
                "178.170.147.0/24",
                "194.177.224.0/19",
                "37.230.216.0/22",
                "178.170.199.0/24",
                "46.16.16.0/21",
                "185.93.20.0/22",
                "37.230.164.0/22",
                "188.72.71.0/24",
                "185.18.188.0/22",
                "178.170.160.0/22",
                "185.57.160.0/22",
                "37.230.214.0/23",
                "46.243.151.0/24",
                "178.170.132.0/22",
                "185.157.200.0/22",
                "37.18.44.0/22",
                "178.170.216.0/24",
                "178.170.204.0/23",
                "178.170.212.0/22",
                "37.230.220.0/23",
                "88.83.0.0/19",
                "178.170.200.0/22"
            ],
            "ipv6_prefixes": [
                "2a00:1fa8::/32",
                "2a03:fdc0::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    }
}
```

### Iceland
```bash
> python3 lookup.py is 4
```
Returns an output file called is_asn_data_{timestamp}.json with the following contents:
```json
{
    "1850": {
        "name": "ISNIC - Internet a Islandi hf",
        "announced": {
            "ipv4_prefixes": [
                "185.93.156.0/22",
                "193.4.58.0/23"
            ],
            "ipv6_prefixes": [
                "2001:67c:6c::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "6677": {
        "name": "ICENET-AS1 - Mila hf",
        "announced": {
            "ipv4_prefixes": [
                "212.30.192.0/19",
                "185.44.204.0/24",
                "157.157.2.0/24",
                "213.167.128.0/19",
                "213.167.150.0/24",
                "157.157.4.0/24",
                "194.105.224.0/24",
                "212.30.212.0/24",
                "157.157.0.0/16",
                "85.220.0.0/17",
                "192.147.34.0/24",
                "194.105.224.0/19",
                "31.209.192.0/18"
            ],
            "ipv6_prefixes": [
                "2001:1a98::/29",
                "2a13:9900::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "12969": {
        "name": "VODAFONE_ICELAND - Ljosleidarinn ehf",
        "announced": {
            "ipv4_prefixes": [
                "193.4.4.0/24",
                "213.176.131.0/24",
                "213.176.128.0/19",
                "185.21.18.0/23",
                "193.4.5.0/24",
                "217.9.128.0/20",
                "89.160.128.0/17",
                "185.24.0.0/23",
                "193.4.0.0/19",
                "193.4.60.0/22",
                "5.23.64.0/20",
                "194.144.0.0/16",
                "62.145.128.0/19",
                "213.213.128.0/19",
                "193.4.64.0/18",
                "185.24.0.0/22",
                "46.239.224.0/19",
                "81.15.0.0/17",
                "46.239.192.0/18",
                "217.151.160.0/19",
                "213.220.64.0/18",
                "193.4.48.0/21",
                "5.23.80.0/20",
                "185.177.132.0/22",
                "193.4.56.0/23",
                "185.21.16.0/23",
                "193.4.128.0/17",
                "46.239.192.0/19",
                "217.171.208.0/20",
                "5.23.64.0/19",
                "185.21.16.0/22",
                "88.149.0.0/17"
            ],
            "ipv6_prefixes": [
                "2a00:4d60::/32",
                "2a02:48::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [
                "217.151.176.0/20",
                "217.151.160.0/20"
            ],
            "ipv6_prefixes": [
                "2a02:48::/29"
            ]
        }
    },
    "15474": {
        "name": "RHNET - Rannsokna- og haskolanet Islands hf.",
        "announced": {
            "ipv4_prefixes": [
                "160.210.0.0/16",
                "130.208.0.0/16"
            ],
            "ipv6_prefixes": [
                "2a00:c88::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "21268": {
        "name": "VODAFONE_ICELAND - Ljosleidarinn ehf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "24743": {
        "name": "SNERPA-NET - Snerpa ehf",
        "announced": {
            "ipv4_prefixes": [
                "193.109.25.0/24",
                "193.109.16.0/20"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "25244": {
        "name": "DECODE-AS - deCode genetics Ltd.",
        "announced": {
            "ipv4_prefixes": [
                "212.126.248.0/21",
                "212.126.240.0/21",
                "212.126.224.0/19"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "25509": {
        "name": "VORTEX-AS - Hringidan ehf / Vortex Inc",
        "announced": {
            "ipv4_prefixes": [
                "213.190.96.0/19"
            ],
            "ipv6_prefixes": [
                "2a00:5380::/29"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "29348": {
        "name": "FSNET-AS - Icelandic Ministry of Education",
        "announced": {
            "ipv4_prefixes": [
                "82.148.64.0/19"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "29689": {
        "name": "ORIGO-AS - Origo hf",
        "announced": {
            "ipv4_prefixes": [
                "87.121.23.0/24",
                "185.30.184.0/22",
                "217.28.176.0/20",
                "80.248.16.0/20"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "30818": {
        "name": "IS-ADVANIA-TRANSIT - Advania Island ehf",
        "announced": {
            "ipv4_prefixes": [
                "82.221.170.0/24",
                "82.221.164.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "31236": {
        "name": "RVK-AS - Reykjavik City Hall",
        "announced": {
            "ipv4_prefixes": [
                "82.112.93.0/24",
                "82.112.85.0/24",
                "82.112.64.0/19",
                "94.198.48.0/23",
                "160.20.214.0/23",
                "82.112.94.0/24",
                "82.112.90.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "31410": {
        "name": "CORE-GLOBAL-AS - Nova hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "31441": {
        "name": "GR-AS - Ljosleidarinn ehf",
        "announced": {
            "ipv4_prefixes": [
                "83.173.0.0/18"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "34678": {
        "name": "TOLVUN-AS - Eignafelag Tolvunar ehf",
        "announced": {
            "ipv4_prefixes": [
                "85.116.65.0/24",
                "85.116.64.0/24",
                "85.116.64.0/19"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "35834": {
        "name": "CCP - CCP ehf.",
        "announced": {
            "ipv4_prefixes": [
                "87.237.34.0/23",
                "87.237.32.0/24",
                "87.237.36.0/24",
                "87.237.38.0/23",
                "87.237.34.0/24",
                "87.237.39.0/24",
                "87.237.32.0/23",
                "87.237.38.0/24",
                "87.237.33.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [
                "87.237.32.0/21"
            ],
            "ipv6_prefixes": []
        }
    },
    "39418": {
        "name": "UMSJA - Origo hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "39472": {
        "name": "ARION-BANKI-AS - Arion Banki hf",
        "announced": {
            "ipv4_prefixes": [
                "88.151.52.0/22",
                "88.151.48.0/22",
                "88.151.48.0/21"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "39532": {
        "name": "LANDSBANKI-AS - Landsbankinn hf",
        "announced": {
            "ipv4_prefixes": [
                "89.104.128.0/19"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "42888": {
        "name": "MANNVIT-AS - Mannvit hf",
        "announced": {
            "ipv4_prefixes": [
                "195.130.193.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "43571": {
        "name": "NOVAIS-AS - Nova hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "43892": {
        "name": "BASIS-AS - Sensa ehf",
        "announced": {
            "ipv4_prefixes": [
                "185.130.12.0/22",
                "79.171.96.0/21",
                "185.62.60.0/22",
                "185.67.180.0/22"
            ],
            "ipv6_prefixes": [
                "2a06:d700::/29",
                "2a02:3c8::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "44275": {
        "name": "OPINKERFI2024 - Opin Kerfi hf",
        "announced": {
            "ipv4_prefixes": [
                "185.169.190.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "44515": {
        "name": "IS-ADVANIA - Advania Island ehf",
        "announced": {
            "ipv4_prefixes": [
                "82.221.80.0/24",
                "82.221.22.0/24",
                "82.221.161.0/24",
                "82.221.88.0/22",
                "212.30.224.0/19",
                "82.221.92.0/22",
                "212.30.229.0/24",
                "82.221.0.0/21",
                "82.221.81.0/24",
                "82.221.80.0/21",
                "82.221.84.0/24",
                "212.30.242.0/24",
                "82.221.28.0/24",
                "82.221.162.0/24",
                "82.221.0.0/17",
                "193.181.194.0/24"
            ],
            "ipv6_prefixes": [
                "2a02:f48::/40",
                "2a02:f48:2100::/40"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [
                "82.221.0.0/16"
            ],
            "ipv6_prefixes": [
                "2a02:f48::/29"
            ]
        }
    },
    "44644": {
        "name": "ARVAKUR-NET - Arvakur hf",
        "announced": {
            "ipv4_prefixes": [
                "92.43.192.0/21"
            ],
            "ipv6_prefixes": [
                "2a01:9460::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "44735": {
        "name": "SIP-ASN - Nova hf",
        "announced": {
            "ipv4_prefixes": [
                "153.92.128.0/19",
                "78.40.248.0/21",
                "185.152.119.0/24",
                "213.181.96.0/20",
                "91.220.138.0/24",
                "46.182.184.0/21",
                "185.111.36.0/22",
                "149.126.80.0/21",
                "213.181.96.0/19",
                "185.152.116.0/22",
                "185.40.120.0/22",
                "178.19.48.0/20",
                "213.181.112.0/20",
                "157.97.0.0/19",
                "78.40.250.0/24"
            ],
            "ipv6_prefixes": [
                "2a00:9280::/32",
                "2a01:6f00::/29",
                "2a13:2440:b0::/48",
                "2a01:8280::/32",
                "2a01:8280:dc00::/40"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "44925": {
        "name": "THE-1984-AS - 1984 ehf",
        "announced": {
            "ipv4_prefixes": [
                "93.95.224.0/21",
                "185.112.144.0/22",
                "195.246.230.0/24",
                "195.246.231.0/24",
                "89.147.108.0/22",
                "93.95.225.0/24",
                "93.95.231.128/25",
                "93.95.227.0/24",
                "93.95.228.0/24",
                "93.95.230.0/24",
                "93.95.229.0/24"
            ],
            "ipv6_prefixes": [
                "2a00:5ee0::/32",
                "2a00:5ee0:2000::/36",
                "2a00:5ee0:2000::/35"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [
                "195.246.230.0/23"
            ],
            "ipv6_prefixes": []
        }
    },
    "47545": {
        "name": "VST-RAF-AS - Verkis hf",
        "announced": {
            "ipv4_prefixes": [
                "91.208.22.0/24"
            ],
            "ipv6_prefixes": [
                "2001:67c:2114::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "47828": {
        "name": "VALITOR-AS - Valitor hf",
        "announced": {
            "ipv4_prefixes": [
                "91.199.134.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "48568": {
        "name": "IS-HINET - Haskoli Islands",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "48685": {
        "name": "OK-AS - Opin Kerfi hf",
        "announced": {
            "ipv4_prefixes": [
                "176.57.224.0/20",
                "185.118.32.0/22",
                "185.25.252.0/22",
                "94.250.244.0/23",
                "185.119.124.0/22",
                "94.142.152.0/21",
                "176.10.32.0/21"
            ],
            "ipv6_prefixes": [
                "2a03:5cc0::/32",
                "2a06:a100::/29"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "50613": {
        "name": "THORDC-AS - Advania Island ehf",
        "announced": {
            "ipv4_prefixes": [
                "82.221.111.0/24",
                "82.221.105.0/24",
                "192.71.218.0/24",
                "82.221.128.0/24",
                "82.221.129.0/24",
                "82.221.136.0/24",
                "82.221.128.0/19",
                "82.221.100.0/23",
                "82.221.96.0/19",
                "151.236.24.0/24",
                "82.221.143.0/24",
                "82.221.141.0/24",
                "82.221.104.0/24",
                "82.221.113.0/24",
                "82.221.139.0/24",
                "37.235.49.0/24",
                "193.107.84.0/22",
                "82.221.131.0/24",
                "82.221.130.0/24"
            ],
            "ipv6_prefixes": [
                "2a03:f80:354::/48",
                "2a02:f48:2000::/40"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "51019": {
        "name": "BNUYYNET - Kjartan Hrafnkelsson",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a05:dfc1:ff00::/48",
                "2a05:dfc1:ffea::/48",
                "2a14:14c1:100::/48",
                "2a07:54c4:175c::/48",
                "2a05:dfc1:ff02::/48",
                "2001:67c:bdc::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "51296": {
        "name": "MEDIAN-IS - Handpoint ehf",
        "announced": {
            "ipv4_prefixes": [
                "91.216.255.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "51829": {
        "name": "KUKL-AS - Nova hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "51896": {
        "name": "HRINGDU-AS - Hringdu ehf",
        "announced": {
            "ipv4_prefixes": [
                "185.191.232.0/22",
                "89.17.128.0/19",
                "31.209.152.0/21",
                "31.209.144.0/21",
                "31.209.136.0/21",
                "46.22.96.0/24",
                "46.22.96.0/20"
            ],
            "ipv6_prefixes": [
                "2a00:5000::/29"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [
                "31.209.144.0/20"
            ],
            "ipv6_prefixes": []
        }
    },
    "56704": {
        "name": "FARICE-AS - Farice ehf",
        "announced": {
            "ipv4_prefixes": [
                "31.15.112.0/21",
                "185.159.158.0/24",
                "185.154.116.0/22",
                "185.252.165.0/24",
                "139.28.147.0/24",
                "185.217.58.0/24"
            ],
            "ipv6_prefixes": [
                "2a03:eb80::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "57508": {
        "name": "AS-ALZA-IS - Alza ehf",
        "announced": {
            "ipv4_prefixes": [
                "185.221.232.0/22",
                "91.220.110.0/24"
            ],
            "ipv6_prefixes": [
                "2a0c:7000::/29",
                "2001:67c:2aac::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "57729": {
        "name": "KOPAVOGUR-AS - Kopavogsbaer",
        "announced": {
            "ipv4_prefixes": [
                "193.4.142.0/24",
                "194.31.61.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "57759": {
        "name": "KORTA-AS - Rapyd Europe hf.",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "59396": {
        "name": "TRS - Tolvu- og Rafeindapjonusta Sudurlands ehf",
        "announced": {
            "ipv4_prefixes": [
                "37.205.32.0/24",
                "37.205.32.0/21",
                "185.112.204.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "59788": {
        "name": "NORTHLAYER-AS1 - Northlayer ehf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "60259": {
        "name": "SIMAFELAGID-ASN - Nova hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "60300": {
        "name": "VODAFONE_ICELAND - Syn hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "60690": {
        "name": "OPEX-ASN - Opin Kerfi hf",
        "announced": {
            "ipv4_prefixes": [
                "185.67.84.0/22",
                "178.248.16.0/21",
                "185.27.36.0/22",
                "185.219.148.0/22",
                "185.123.196.0/22",
                "185.109.100.0/22",
                "93.95.72.0/21"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "62199": {
        "name": "VERNEGLOBAL-IS - Verne Global hf.",
        "announced": {
            "ipv4_prefixes": [
                "185.45.76.0/22"
            ],
            "ipv6_prefixes": [
                "2a01:49a0::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "197403": {
        "name": "ISLANDSBANKI-AS1 - Islandsbanki hf",
        "announced": {
            "ipv4_prefixes": [
                "46.28.157.0/24",
                "46.28.152.0/21"
            ],
            "ipv6_prefixes": [
                "2a00:7840::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "197973": {
        "name": "SKRA-NET - Registers Iceland",
        "announced": {
            "ipv4_prefixes": [
                "128.140.232.0/21"
            ],
            "ipv6_prefixes": [
                "2a02:6b80::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "198707": {
        "name": "CLOUDOMATE-AS - Alfred Hall",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2001:67c:c88::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "198815": {
        "name": "RUV-AS - Rikisutvarpid Ohf",
        "announced": {
            "ipv4_prefixes": [
                "37.152.64.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [
                "37.152.64.0/21"
            ],
            "ipv6_prefixes": []
        }
    },
    "199844": {
        "name": "RARIK - RARIK ohf.",
        "announced": {
            "ipv4_prefixes": [
                "185.44.240.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "200432": {
        "name": "BORGUN - Teya Iceland hf",
        "announced": {
            "ipv4_prefixes": [
                "185.107.62.0/24",
                "185.107.60.0/24",
                "185.107.63.0/24",
                "185.107.61.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [
                "185.107.60.0/22"
            ],
            "ipv6_prefixes": []
        }
    },
    "200651": {
        "name": "FLOKINET - FlokiNET ehf",
        "announced": {
            "ipv4_prefixes": [
                "37.156.68.0/24",
                "185.247.226.0/24",
                "185.100.86.0/24",
                "185.165.168.0/24",
                "81.180.202.0/23",
                "185.165.170.0/24",
                "37.228.128.0/24",
                "185.165.169.0/24",
                "185.100.87.0/24",
                "185.10.68.0/24",
                "185.247.225.0/24",
                "185.146.232.0/24",
                "37.228.129.0/24",
                "185.246.189.0/24",
                "185.165.171.0/24",
                "185.246.188.0/24",
                "185.247.224.0/24",
                "185.100.84.0/23",
                "185.146.233.0/24"
            ],
            "ipv6_prefixes": [
                "2a06:1700:2::/48",
                "2a06:1700::/48",
                "2a06:1700:4::/48",
                "2a06:1700:100::/48",
                "2a06:1700:3::/48",
                "2a06:1700:1::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [
                "185.247.224.0/22",
                "185.100.84.0/22",
                "185.165.168.0/22",
                "185.246.188.0/22",
                "185.146.232.0/22"
            ],
            "ipv6_prefixes": [
                "2a06:1700::/29"
            ]
        }
    },
    "200868": {
        "name": "KAPALVAEDING - Kapalvaeding ehf.",
        "announced": {
            "ipv4_prefixes": [
                "185.86.220.0/22",
                "213.181.126.0/23"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "201696": {
        "name": "ALTHINGI-AS - Althingi Islendinga",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "201849": {
        "name": "SENSA-AS - Sensa ehf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a06:d700:4444::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "201885": {
        "name": "RU-AS - Haskolinn i Reykjavik ehf.",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "202030": {
        "name": "ICELANDAIR-AS - Icelandair ehf",
        "announced": {
            "ipv4_prefixes": [
                "185.56.12.0/22",
                "185.56.13.0/24",
                "185.56.14.0/24",
                "185.56.15.0/24",
                "185.56.12.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "202247": {
        "name": "NETBERG - Netpandan ehf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "202868": {
        "name": "TSC - Nova hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203176": {
        "name": "RB - Reiknistofa bankanna hf.",
        "announced": {
            "ipv4_prefixes": [
                "193.4.113.32/27",
                "193.4.166.0/24",
                "194.144.249.112/28",
                "194.144.249.96/28",
                "185.29.198.0/24",
                "185.29.196.0/22",
                "193.4.97.232/29",
                "217.151.180.0/28"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203322": {
        "name": "EIMSKIP-AS - Eimskip Island ehf",
        "announced": {
            "ipv4_prefixes": [
                "185.138.174.0/23",
                "185.138.172.0/23",
                "185.138.172.0/22"
            ],
            "ipv6_prefixes": [
                "2a07:fc0::/29"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203566": {
        "name": "MILAHF-AS2 - Mila hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203590": {
        "name": "SENSA-AS - Sensa ehf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203715": {
        "name": "ISA - Isavia ohf",
        "announced": {
            "ipv4_prefixes": [
                "185.126.60.0/23",
                "185.126.62.0/23"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [
                "185.126.60.0/22"
            ],
            "ipv6_prefixes": []
        }
    },
    "204588": {
        "name": "PROTEGION - Rapyd Europe hf.",
        "announced": {
            "ipv4_prefixes": [
                "185.240.40.0/24",
                "185.240.43.0/24",
                "185.240.41.0/24",
                "185.240.42.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [
                "185.240.40.0/22"
            ],
            "ipv6_prefixes": []
        }
    },
    "204926": {
        "name": "IS-GUNNAR - Gunnar Gudvardarson",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2001:678:58c::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "205436": {
        "name": "ASWINTERMUTE - Wintermute Technologies EHF",
        "announced": {
            "ipv4_prefixes": [
                "185.156.22.0/24",
                "147.28.16.0/24",
                "147.28.18.0/24",
                "147.28.17.0/24",
                "185.156.21.0/24",
                "147.28.19.0/24",
                "147.28.16.0/23",
                "185.156.23.0/24",
                "185.156.20.0/23",
                "185.156.20.0/24",
                "147.28.18.0/23",
                "147.28.22.0/24",
                "147.28.23.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [
                "147.28.16.0/20",
                "185.156.20.0/22"
            ],
            "ipv6_prefixes": []
        }
    },
    "206010": {
        "name": "RFS - Umbra Service Center Management",
        "announced": {
            "ipv4_prefixes": [
                "185.198.144.0/22"
            ],
            "ipv6_prefixes": [
                "2a0a:89c0::/29"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206440": {
        "name": "NETPANDAN - Netpandan ehf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206669": {
        "name": "GAGNAVEITAN - Gagnaveitan ehf.",
        "announced": {
            "ipv4_prefixes": [
                "185.179.79.0/24",
                "185.179.76.0/22",
                "185.179.76.0/24",
                "185.179.78.0/24",
                "185.179.77.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206743": {
        "name": "SECURITASICELAND - Securitas hf.",
        "announced": {
            "ipv4_prefixes": [
                "185.177.132.0/23",
                "185.177.134.0/24",
                "185.177.135.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206842": {
        "name": "TACTICA - Tactica ehf",
        "announced": {
            "ipv4_prefixes": [
                "185.174.176.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "207295": {
        "name": "AS-THORIX-RS - Northlayer ehf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "207598": {
        "name": "LSG-AS - Leifur Steinn Gunnarsson",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a07:54c4:73d1::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "208548": {
        "name": "KJARNET-0 - Kjartan Hrafnkelsson",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a07:54c4:13f0::/44",
                "2a07:54c4:a60::/44",
                "2a07:54c2:1c00::/38"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "209214": {
        "name": "IS-NETHEIMUR - Netheimur ehf.",
        "announced": {
            "ipv4_prefixes": [
                "185.248.120.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "209933": {
        "name": "DANDRI - David Andri Jakobsson",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2001:678:888::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "210080": {
        "name": "TOLVUTHJONUSTAN - Tolvuthjonustan ehf.",
        "announced": {
            "ipv4_prefixes": [
                "185.221.176.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "210747": {
        "name": "IHOTELS - BERJAYA HOTELS ICELAND hf",
        "announced": {
            "ipv4_prefixes": [
                "193.243.188.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "211589": {
        "name": "RUV-CDN - Rikisutvarpid Ohf",
        "announced": {
            "ipv4_prefixes": [
                "37.152.71.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "211734": {
        "name": "IS-VEGAGERDIN - Vegagerdin",
        "announced": {
            "ipv4_prefixes": [
                "185.147.137.0/24",
                "185.147.136.0/22",
                "185.147.136.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "211757": {
        "name": "PANASCAIS - Panascais ehf.",
        "announced": {
            "ipv4_prefixes": [
                "31.43.173.0/24",
                "31.43.172.0/24"
            ],
            "ipv6_prefixes": [
                "2a10:9840:2::/48",
                "2a10:9840:1::/48"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [
                "31.43.172.0/23"
            ],
            "ipv6_prefixes": []
        }
    },
    "211815": {
        "name": "LANDSVIRKJUN-AS - Landsvirkjun",
        "announced": {
            "ipv4_prefixes": [
                "185.236.130.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "212771": {
        "name": "NETVOKTUN - Netvoktun ehf",
        "announced": {
            "ipv4_prefixes": [
                "185.43.30.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "212926": {
        "name": "HARPA-AS - Harpa Concert Hall and Conference Centre ohf",
        "announced": {
            "ipv4_prefixes": [
                "88.135.70.0/24"
            ],
            "ipv6_prefixes": [
                "2a07:e8c0::/32"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "213239": {
        "name": "NORTHLAYER-AS2 - Northlayer ehf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "213364": {
        "name": "IS-STEINN-6 - STEINN ORVAR BJARNARSON",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "214718": {
        "name": "WISE - Thekking - Tristan hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "215608": {
        "name": "SAMGONGUSTOFA - Samgongustofa",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "215793": {
        "name": "SIMINN - Siminn hf. (Iceland Telecom)",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "215823": {
        "name": "FOSSHALS-LAN - Spaugur ehf.",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a07:54c4::/44"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "216017": {
        "name": "OKH-2 - Opin Kerfi hf",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "216260": {
        "name": "TSICELAND - Tech tolvu- og rekstrarla ehf.",
        "announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "216293": {
        "name": "TS - TechSupport ehf",
        "announced": {
            "ipv4_prefixes": [
                "212.46.60.0/24"
            ],
            "ipv6_prefixes": [
                "2a13:d9c0::/29"
            ]
        },
        "not_announced": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    }
}
```
