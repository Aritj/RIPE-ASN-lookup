# RIPE-CC-prefix-lookup
This project identifies all ASNs for any given country code (cc) and determines the associated IP prefixes, checking which are advertised. Initially inspired by an interest in the ASNs and IP prefixes for the Faroe Islands (FO), this tool uses RIPE NCC data to provide insights into IP address allocations and advertisement status.


## Generating the example files

### Faroe Islands
```bash
> python3 lookup.py fo
```
Generates an output file called fo_asn_data_{timestamp}.json:
```json
{"15389": {"name": "FAROESE-TELECOM-AS - P/F Telefonverkid", "upstream_bgp_asn": [1299, 3292], "downstream_bgp_asn": [206928, 25152], "announced_prefixes": {"ipv4_prefixes": ["193.34.104.0/22", "185.74.208.0/22", "198.137.136.0/22", "212.55.32.0/19", "88.85.32.0/19", "81.18.224.0/20", "178.19.192.0/20", "217.172.80.0/20"], "ipv6_prefixes": ["2a02:e90::/32"]}, "not_announced_prefixes": {"ipv4_prefixes": [], "ipv6_prefixes": ["2a02:e94::/30", "2a02:e92::/31", "2a02:e91::/32"]}}, "20963": {"name": "NEMAFAROE - P/F 20.11.19", "upstream_bgp_asn": [12969], "downstream_bgp_asn": [200664, 206928, 209175], "announced_prefixes": {"ipv4_prefixes": ["46.227.112.0/21", "81.25.176.0/20", "185.88.228.0/22", "80.77.128.0/20"], "ipv6_prefixes": []}, "not_announced_prefixes": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "200664": {"name": "PF-FTNET - P/F Net", "upstream_bgp_asn": [20963], "downstream_bgp_asn": [], "announced_prefixes": {"ipv4_prefixes": [], "ipv6_prefixes": []}, "not_announced_prefixes": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "206928": {"name": "PF-ELEKTRON - P/F Elektron", "upstream_bgp_asn": [15389, 20963, 46844], "downstream_bgp_asn": [], "announced_prefixes": {"ipv4_prefixes": ["185.171.172.0/22"], "ipv6_prefixes": []}, "not_announced_prefixes": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "209175": {"name": "KRINGVARP_FOROYA - Kringvarp Foroya", "upstream_bgp_asn": [20963], "downstream_bgp_asn": [], "announced_prefixes": {"ipv4_prefixes": ["195.80.36.0/22"], "ipv6_prefixes": []}, "not_announced_prefixes": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "210417": {"name": "NET2 - P/F Net", "upstream_bgp_asn": [], "downstream_bgp_asn": [], "announced_prefixes": {"ipv4_prefixes": [], "ipv6_prefixes": []}, "not_announced_prefixes": {"ipv4_prefixes": [], "ipv6_prefixes": []}}}
```
We can also control the JSON formatting (indentation level):
```bash
> python3 lookup.py fo -i 4
```
Resulting in a file with the following output:
<details>
  <summary>View output</summary>
    
  ```json
{
    "15389": {
        "name": "FAROESE-TELECOM-AS - P/F Telefonverkid",
        "upstream_bgp_asn": [
            1299,
            3292
        ],
        "downstream_bgp_asn": [
            206928,
            25152
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "193.34.104.0/22",
                "185.74.208.0/22",
                "198.137.136.0/22",
                "212.55.32.0/19",
                "88.85.32.0/19",
                "81.18.224.0/20",
                "178.19.192.0/20",
                "217.172.80.0/20"
            ],
            "ipv6_prefixes": [
                "2a02:e90::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a02:e94::/30",
                "2a02:e92::/31",
                "2a02:e91::/32"
            ]
        }
    },
    "20963": {
        "name": "NEMAFAROE - P/F 20.11.19",
        "upstream_bgp_asn": [
            12969
        ],
        "downstream_bgp_asn": [
            200664,
            206928,
            209175
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "46.227.112.0/21",
                "81.25.176.0/20",
                "185.88.228.0/22",
                "80.77.128.0/20"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "200664": {
        "name": "PF-FTNET - P/F Net",
        "upstream_bgp_asn": [
            20963
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206928": {
        "name": "PF-ELEKTRON - P/F Elektron",
        "upstream_bgp_asn": [
            15389,
            20963,
            46844
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.171.172.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "209175": {
        "name": "KRINGVARP_FOROYA - Kringvarp Foroya",
        "upstream_bgp_asn": [
            20963
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "195.80.36.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "210417": {
        "name": "NET2 - P/F Net",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    }
}
  ```
</details>

### Iceland
For countries with a large amount of ASNs it is recommended to use multiple threads to speed up the process (-t 20).
```bash
> python3 lookup.py is -i 4 -t 20
```
Generates an output file called is_asn_data_{timestamp}.json with the following contents:
<details>
  <summary>View output</summary>
    
```json
{
    "35834": {
        "name": "CCP - CCP ehf.",
        "upstream_bgp_asn": [
            12552,
            1299,
            132337,
            13335,
            137409,
            15802,
            15830,
            20764,
            25091,
            29075,
            31042,
            328832,
            34549,
            34927,
            35280,
            37100,
            39351,
            41327,
            4455,
            44735,
            48362,
            50304,
            5713,
            60171,
            62275,
            6424,
            6461,
            6939,
            7195,
            7575,
            8896,
            8932,
            9002,
            9044,
            9304,
            9498
        ],
        "downstream_bgp_asn": [
            12779,
            12969,
            13237,
            14630,
            14840,
            18106,
            1828,
            198150,
            207841,
            212483,
            213241,
            24482,
            25160,
            271253,
            28792,
            31742,
            34177,
            34288,
            35266,
            35598,
            36236,
            37721,
            39122,
            396998,
            41047,
            42473,
            48070,
            49544,
            50300,
            51185,
            52320,
            5405,
            57406,
            59605,
            62167,
            6233,
            6894
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "87.237.34.0/23",
                "87.237.34.0/24",
                "87.237.32.0/24",
                "87.237.39.0/24",
                "87.237.32.0/23",
                "87.237.38.0/24",
                "87.237.33.0/24",
                "87.237.38.0/23",
                "87.237.36.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "87.237.37.0/24"
            ],
            "ipv6_prefixes": []
        }
    },
    "34678": {
        "name": "TOLVUN-AS - Eignafelag Tolvunar ehf",
        "upstream_bgp_asn": [
            25509
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "85.116.64.0/19",
                "85.116.65.0/24",
                "85.116.64.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "39472": {
        "name": "ARION-BANKI-AS - Arion Banki hf",
        "upstream_bgp_asn": [
            12969,
            13335,
            30818,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "88.151.48.0/22",
                "88.151.48.0/21",
                "88.151.52.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "31236": {
        "name": "RVK-AS - Reykjavik City Hall",
        "upstream_bgp_asn": [
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "82.112.94.0/24",
                "82.112.64.0/19",
                "82.112.85.0/24",
                "82.112.90.0/24",
                "160.20.214.0/23",
                "94.198.48.0/23",
                "82.112.93.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "21268": {
        "name": "VODAFONE_ICELAND - Ljosleidarinn ehf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "42888": {
        "name": "MANNVIT-AS - Mannvit hf",
        "upstream_bgp_asn": [
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "195.130.193.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "31410": {
        "name": "CORE-GLOBAL-AS - Nova hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "25509": {
        "name": "VORTEX-AS - Hringidan ehf / Vortex Inc",
        "upstream_bgp_asn": [
            1239,
            1267,
            12779,
            132337,
            137409,
            15802,
            15830,
            15958,
            174,
            1764,
            1836,
            200780,
            20485,
            20562,
            20764,
            24961,
            2603,
            28716,
            29075,
            29208,
            31025,
            3214,
            328832,
            33891,
            34019,
            34549,
            34927,
            35280,
            35710,
            37100,
            37468,
            39351,
            41327,
            4455,
            47734,
            48362,
            48858,
            50304,
            50629,
            5398,
            5713,
            60171,
            6057,
            6424,
            6939,
            7195,
            8447,
            8758,
            8896,
            8932,
            9498
        ],
        "downstream_bgp_asn": [
            34678,
            12969,
            13237,
            142271,
            14630,
            14840,
            15547,
            15605,
            17639,
            18106,
            1828,
            198150,
            198385,
            199524,
            199938,
            200612,
            205112,
            206356,
            207841,
            208431,
            20932,
            210937,
            212483,
            213151,
            213241,
            21412,
            23106,
            24482,
            25091,
            25160,
            25220,
            263152,
            271253,
            28792,
            28917,
            29140,
            31027,
            31510,
            3170,
            31742,
            3212,
            34177,
            34288,
            34872,
            35266,
            35360,
            35598,
            36236,
            37721,
            39122,
            396998,
            41047,
            42473,
            42541,
            45489,
            47147,
            47692,
            48070,
            48919,
            49544,
            49605,
            50300,
            51184,
            51185,
            52320,
            5405,
            553,
            559,
            56987,
            57406,
            57695,
            58057,
            59605,
            62167,
            6233,
            64475,
            8283,
            8298,
            8888,
            34678
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "213.190.96.0/19"
            ],
            "ipv6_prefixes": [
                "2a00:5380::/29"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "24743": {
        "name": "SNERPA-NET - Snerpa ehf",
        "upstream_bgp_asn": [
            1239,
            12969,
            174,
            2603
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "193.109.16.0/20",
                "193.109.25.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "1850": {
        "name": "ISNIC - Internet a Islandi hf",
        "upstream_bgp_asn": [
            2603,
            44735,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.93.156.0/22",
                "193.4.58.0/23"
            ],
            "ipv6_prefixes": [
                "2001:67c:6c::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "31441": {
        "name": "GR-AS - Ljosleidarinn ehf",
        "upstream_bgp_asn": [
            12969
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "83.173.0.0/18"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "15474": {
        "name": "RHNET - Rannsokna- og haskolanet Islands hf.",
        "upstream_bgp_asn": [
            2603
        ],
        "downstream_bgp_asn": [
            25244,
            29348,
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "130.208.0.0/16",
                "160.210.0.0/16"
            ],
            "ipv6_prefixes": [
                "2a00:c88::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "39418": {
        "name": "UMSJA - Origo hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "39532": {
        "name": "LANDSBANKI-AS - Landsbankinn hf",
        "upstream_bgp_asn": [
            12969,
            13335,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "89.104.128.0/19"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "43892": {
        "name": "BASIS-AS - Sensa ehf",
        "upstream_bgp_asn": [
            44735,
            6677
        ],
        "downstream_bgp_asn": [
            201849
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.62.60.0/22",
                "185.67.180.0/22",
                "185.130.12.0/22",
                "79.171.96.0/21"
            ],
            "ipv6_prefixes": [
                "2a06:d700::/29",
                "2a02:3c8::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "43571": {
        "name": "NOVAIS-AS - Nova hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "25244": {
        "name": "DECODE-AS - deCode genetics Ltd.",
        "upstream_bgp_asn": [
            15474,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "212.126.248.0/21",
                "212.126.224.0/19",
                "212.126.240.0/21"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "44515": {
        "name": "IS-ADVANIA - Advania Island ehf",
        "upstream_bgp_asn": [
            30818
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "212.30.229.0/24",
                "82.221.162.0/24",
                "193.181.194.0/24",
                "82.221.88.0/22",
                "82.221.22.0/24",
                "82.221.84.0/24",
                "82.221.161.0/24",
                "82.221.80.0/21",
                "82.221.0.0/17",
                "212.30.242.0/24",
                "82.221.0.0/21",
                "82.221.28.0/24",
                "82.221.81.0/24",
                "82.221.80.0/24",
                "82.221.92.0/22",
                "212.30.224.0/19"
            ],
            "ipv6_prefixes": [
                "2a02:f48:2100::/40",
                "2a02:f48::/40"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "82.221.32.0/19",
                "82.221.8.0/21",
                "82.221.24.0/22",
                "82.221.30.0/23",
                "82.221.29.0/24",
                "82.221.16.0/22",
                "82.221.20.0/23",
                "82.221.23.0/24",
                "82.221.96.0/19",
                "82.221.64.0/20",
                "82.221.82.0/23",
                "82.221.86.0/23",
                "82.221.85.0/24",
                "82.221.192.0/18",
                "82.221.128.0/19",
                "82.221.176.0/20",
                "82.221.168.0/21",
                "82.221.164.0/22",
                "82.221.160.0/24",
                "82.221.163.0/24"
            ],
            "ipv6_prefixes": [
                "2a02:f4c::/30",
                "2a02:f4a::/31",
                "2a02:f49::/32",
                "2a02:f48:8000::/33",
                "2a02:f48:4000::/34",
                "2a02:f48:1000::/36",
                "2a02:f48:800::/37",
                "2a02:f48:400::/38",
                "2a02:f48:200::/39",
                "2a02:f48:100::/40",
                "2a02:f48:3000::/36",
                "2a02:f48:2800::/37",
                "2a02:f48:2400::/38",
                "2a02:f48:2200::/39",
                "2a02:f48:2000::/40"
            ]
        }
    },
    "44275": {
        "name": "OPINKERFI2024 - Opin Kerfi hf",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.169.190.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "47828": {
        "name": "VALITOR-AS - Valitor hf",
        "upstream_bgp_asn": [
            12969,
            13335,
            6677
        ],
        "downstream_bgp_asn": [
            204588
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "91.199.134.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "44925": {
        "name": "THE-1984-AS - 1984 ehf",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "195.246.231.0/24",
                "185.112.144.0/22",
                "195.246.230.0/24",
                "89.147.108.0/22",
                "93.95.224.0/21",
                "93.95.225.0/24",
                "93.95.231.128/25",
                "93.95.227.0/24",
                "93.95.228.0/24",
                "93.95.230.0/24",
                "93.95.229.0/24",
                "89.147.109.0/24",
                "89.147.108.0/24",
                "185.112.145.0/24",
                "185.112.146.0/24",
                "185.112.144.0/24",
                "89.147.110.0/24",
                "185.112.147.0/24",
                "89.147.111.0/24",
                "195.246.230.0/23"
            ],
            "ipv6_prefixes": [
                "2a00:5ee0:2000::/35",
                "2a00:5ee0:2000::/36",
                "2a00:5ee0::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "48685": {
        "name": "OK-AS - Opin Kerfi hf",
        "upstream_bgp_asn": [
            2603,
            56704,
            6677
        ],
        "downstream_bgp_asn": [
            198815,
            206010,
            211589,
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "94.142.152.0/21",
                "185.119.124.0/22",
                "176.10.32.0/21",
                "176.57.224.0/20",
                "94.250.244.0/23",
                "185.118.32.0/22",
                "185.25.252.0/22"
            ],
            "ipv6_prefixes": [
                "2a06:a100::/29",
                "2a03:5cc0::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "48568": {
        "name": "IS-HINET - Haskoli Islands",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "51829": {
        "name": "KUKL-AS - Nova hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "47545": {
        "name": "VST-RAF-AS - Verkis hf",
        "upstream_bgp_asn": [
            44735,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "91.208.22.0/24"
            ],
            "ipv6_prefixes": [
                "2001:67c:2114::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "50613": {
        "name": "THORDC-AS - Advania Island ehf",
        "upstream_bgp_asn": [
            30818
        ],
        "downstream_bgp_asn": [
            200651
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "82.221.113.0/24",
                "82.221.96.0/19",
                "82.221.111.0/24",
                "82.221.105.0/24",
                "82.221.139.0/24",
                "82.221.128.0/24",
                "82.221.128.0/19",
                "82.221.131.0/24",
                "37.235.49.0/24",
                "82.221.143.0/24",
                "82.221.130.0/24",
                "82.221.136.0/24",
                "82.221.104.0/24",
                "151.236.24.0/24",
                "82.221.141.0/24",
                "82.221.129.0/24",
                "193.107.84.0/22",
                "82.221.100.0/23",
                "192.71.218.0/24"
            ],
            "ipv6_prefixes": [
                "2a03:f80:354::/48",
                "2a02:f48:2000::/40"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "51896": {
        "name": "HRINGDU-AS - Hringdu ehf",
        "upstream_bgp_asn": [
            2603,
            6677
        ],
        "downstream_bgp_asn": [
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "31.209.152.0/21",
                "46.22.96.0/24",
                "46.22.96.0/20",
                "185.191.232.0/22",
                "89.17.128.0/19",
                "31.209.136.0/21",
                "31.209.144.0/21"
            ],
            "ipv6_prefixes": [
                "2a00:5000::/29"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "57508": {
        "name": "AS-ALZA-IS - Alza ehf",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "91.220.110.0/24",
                "185.221.232.0/22"
            ],
            "ipv6_prefixes": [
                "2001:67c:2aac::/48",
                "2a0c:7000::/29"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "51296": {
        "name": "MEDIAN-IS - Handpoint ehf",
        "upstream_bgp_asn": [
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "91.216.255.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "44735": {
        "name": "SIP-ASN - Nova hf",
        "upstream_bgp_asn": [
            1103,
            12552,
            1267,
            1299,
            132337,
            137409,
            15576,
            15802,
            15830,
            15958,
            20562,
            20764,
            24961,
            25091,
            2603,
            29075,
            2914,
            31042,
            31133,
            3216,
            328832,
            3356,
            33891,
            34019,
            34549,
            3462,
            34927,
            35280,
            37100,
            37468,
            39351,
            41327,
            43727,
            4455,
            47147,
            47160,
            48362,
            48858,
            50304,
            50629,
            50673,
            5713,
            57304,
            60171,
            6057,
            62275,
            6424,
            6461,
            6777,
            6939,
            7195,
            8447,
            8758,
            8896,
            8932,
            9002,
            9044,
            9498
        ],
        "downstream_bgp_asn": [
            13335,
            1850,
            197403,
            198020,
            200432,
            200868,
            202030,
            205514,
            206669,
            206804,
            207137,
            209045,
            209214,
            210080,
            210747,
            212771,
            212926,
            29689,
            30286,
            35834,
            39832,
            43525,
            43892,
            44275,
            44644,
            44925,
            47545,
            47556,
            57508,
            59396,
            60259,
            60550,
            60690,
            64703,
            65205,
            65323,
            1140,
            12637,
            12779,
            12859,
            12969,
            13237,
            14630,
            14840,
            14907,
            15435,
            15547,
            15605,
            17639,
            18106,
            1828,
            198150,
            199524,
            199938,
            207841,
            20932,
            212483,
            213241,
            23106,
            24482,
            25160,
            25220,
            263152,
            271253,
            28792,
            29140,
            31027,
            31122,
            3170,
            31742,
            3214,
            3333,
            3399,
            34177,
            34288,
            35266,
            35598,
            36236,
            37721,
            39122,
            396998,
            41047,
            42473,
            42541,
            45489,
            48070,
            48919,
            49544,
            49605,
            50300,
            50763,
            51184,
            51185,
            51873,
            52320,
            5405,
            559,
            56987,
            57406,
            59605,
            62167,
            6233,
            6894,
            8283,
            8888,
            917
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "213.181.96.0/20",
                "46.182.184.0/21",
                "185.40.120.0/22",
                "149.126.80.0/21",
                "185.152.116.0/22",
                "178.19.48.0/20",
                "91.220.138.0/24",
                "153.92.128.0/19",
                "78.40.248.0/21",
                "185.152.119.0/24",
                "213.181.112.0/20",
                "157.97.0.0/19",
                "213.181.96.0/19",
                "185.111.36.0/22",
                "78.40.250.0/24"
            ],
            "ipv6_prefixes": [
                "2a01:6f00::/29",
                "2a00:9280::/32",
                "2a13:2440:b0::/48",
                "2a01:8280::/32",
                "2a01:8280:dc00::/40"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "44644": {
        "name": "ARVAKUR-NET - Arvakur hf",
        "upstream_bgp_asn": [
            44735,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "92.43.192.0/21"
            ],
            "ipv6_prefixes": [
                "2a01:9460::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "56704": {
        "name": "FARICE-AS - Farice ehf",
        "upstream_bgp_asn": [
            1103,
            1239,
            12552,
            1267,
            13030,
            13194,
            132337,
            137409,
            15576,
            15802,
            15830,
            15958,
            174,
            20562,
            20764,
            2119,
            24961,
            25091,
            25369,
            29075,
            29208,
            31042,
            31133,
            3214,
            3216,
            328832,
            33891,
            34019,
            34549,
            3462,
            34927,
            35280,
            37100,
            37468,
            39351,
            41327,
            4455,
            47147,
            47160,
            48362,
            48858,
            50304,
            50629,
            50673,
            5713,
            60171,
            6057,
            62275,
            6424,
            6453,
            6461,
            6777,
            6939,
            7195,
            8218,
            8447,
            8758,
            8896,
            8932,
            9002,
            9044,
            9498
        ],
        "downstream_bgp_asn": [
            205436,
            206804,
            207137,
            48685,
            1140,
            12637,
            12779,
            12859,
            12969,
            13237,
            14630,
            14840,
            14907,
            15435,
            15547,
            15605,
            17639,
            18106,
            1828,
            198150,
            199524,
            199938,
            207841,
            20932,
            212483,
            213241,
            23106,
            24482,
            25160,
            25220,
            263152,
            271253,
            28792,
            29140,
            31027,
            31122,
            3170,
            31742,
            3333,
            3399,
            34177,
            34288,
            35266,
            35598,
            36236,
            37721,
            39122,
            396998,
            41047,
            42473,
            42541,
            45489,
            48070,
            48919,
            49544,
            49605,
            50300,
            50763,
            51088,
            51184,
            51185,
            51873,
            52320,
            5405,
            559,
            56987,
            57406,
            59605,
            62167,
            6233,
            8283,
            8455,
            8888
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "139.28.147.0/24",
                "185.217.58.0/24",
                "185.159.158.0/24",
                "185.154.116.0/22",
                "185.252.165.0/24",
                "31.15.112.0/21"
            ],
            "ipv6_prefixes": [
                "2a03:eb80::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "59396": {
        "name": "TRS - Tolvu- og Rafeindapjonusta Sudurlands ehf",
        "upstream_bgp_asn": [
            44735,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "37.205.32.0/21",
                "37.205.32.0/24",
                "185.112.204.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "57729": {
        "name": "KOPAVOGUR-AS - Kopavogsbaer",
        "upstream_bgp_asn": [
            12969
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "194.31.61.0/24",
                "193.4.142.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "60259": {
        "name": "SIMAFELAGID-ASN - Nova hf",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [
            62199
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "62199": {
        "name": "VERNEGLOBAL-IS - Verne Global hf.",
        "upstream_bgp_asn": [
            60259
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.45.76.0/22"
            ],
            "ipv6_prefixes": [
                "2a01:49a0::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "197973": {
        "name": "SKRA-NET - Registers Iceland",
        "upstream_bgp_asn": [
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "128.140.232.0/21"
            ],
            "ipv6_prefixes": [
                "2a02:6b80::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "60690": {
        "name": "OPEX-ASN - Opin Kerfi hf",
        "upstream_bgp_asn": [
            2603,
            44735
        ],
        "downstream_bgp_asn": [
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "93.95.72.0/21",
                "185.27.36.0/22",
                "185.219.148.0/22",
                "178.248.16.0/21",
                "185.109.100.0/22",
                "185.67.84.0/22",
                "185.123.196.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "59788": {
        "name": "NORTHLAYER-AS1 - Northlayer ehf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "200651": {
        "name": "FLOKINET - FlokiNET ehf",
        "upstream_bgp_asn": [
            12552,
            3223,
            50613,
            50673
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "81.180.202.0/23",
                "185.246.189.0/24",
                "37.156.68.0/24",
                "185.100.86.0/24",
                "185.10.68.0/24",
                "185.165.170.0/24",
                "185.247.224.0/24",
                "185.100.87.0/24",
                "185.165.169.0/24",
                "185.165.171.0/24",
                "185.246.188.0/24",
                "185.146.233.0/24",
                "37.228.128.0/24",
                "185.247.225.0/24",
                "185.247.226.0/24",
                "185.146.232.0/24",
                "37.228.129.0/24",
                "185.100.84.0/23",
                "185.165.168.0/24"
            ],
            "ipv6_prefixes": [
                "2a06:1700:3::/48",
                "2a06:1700:4::/48",
                "2a06:1700:100::/48",
                "2a06:1700:2::/48",
                "2a06:1700:1::/48",
                "2a06:1700::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "185.146.234.0/23",
                "185.247.227.0/24",
                "185.246.190.0/23"
            ],
            "ipv6_prefixes": [
                "2a06:1704::/30",
                "2a06:1702::/31",
                "2a06:1701::/32",
                "2a06:1700:8000::/33",
                "2a06:1700:4000::/34",
                "2a06:1700:2000::/35",
                "2a06:1700:1000::/36",
                "2a06:1700:800::/37",
                "2a06:1700:400::/38",
                "2a06:1700:200::/39",
                "2a06:1700:180::/41",
                "2a06:1700:140::/42",
                "2a06:1700:120::/43",
                "2a06:1700:110::/44",
                "2a06:1700:108::/45",
                "2a06:1700:104::/46",
                "2a06:1700:102::/47",
                "2a06:1700:101::/48",
                "2a06:1700:80::/41",
                "2a06:1700:40::/42",
                "2a06:1700:20::/43",
                "2a06:1700:10::/44",
                "2a06:1700:8::/45",
                "2a06:1700:6::/47",
                "2a06:1700:5::/48"
            ]
        }
    },
    "198707": {
        "name": "CLOUDOMATE-AS - Alfred Hall",
        "upstream_bgp_asn": [
            44103
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2001:67c:c88::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "199844": {
        "name": "RARIK - RARIK ohf.",
        "upstream_bgp_asn": [
            12969,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.44.240.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "60300": {
        "name": "VODAFONE_ICELAND - Syn hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "200868": {
        "name": "KAPALVAEDING - Kapalvaeding ehf.",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.86.220.0/22",
                "213.181.126.0/23"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "57759": {
        "name": "KORTA-AS - Rapyd Europe hf.",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "201849": {
        "name": "SENSA-AS - Sensa ehf",
        "upstream_bgp_asn": [
            43892
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a06:d700:4444::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "30818": {
        "name": "IS-ADVANIA-TRANSIT - Advania Island ehf",
        "upstream_bgp_asn": [
            1299,
            2603,
            286,
            3223,
            3257
        ],
        "downstream_bgp_asn": [
            202030,
            203322,
            204926,
            206842,
            211734,
            3257,
            39472,
            44515,
            50613,
            6677,
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "82.221.170.0/24",
                "82.221.164.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "201696": {
        "name": "ALTHINGI-AS - Althingi Islendinga",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "197403": {
        "name": "ISLANDSBANKI-AS1 - Islandsbanki hf",
        "upstream_bgp_asn": [
            12969,
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "46.28.157.0/24",
                "46.28.152.0/21"
            ],
            "ipv6_prefixes": [
                "2a00:7840::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "29348": {
        "name": "FSNET-AS - Icelandic Ministry of Education",
        "upstream_bgp_asn": [
            15474
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "82.148.64.0/19"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "201885": {
        "name": "RU-AS - Haskolinn i Reykjavik ehf.",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "198815": {
        "name": "RUV-AS - Rikisutvarpid Ohf",
        "upstream_bgp_asn": [
            12969,
            48685
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "37.152.64.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "37.152.68.0/22"
            ],
            "ipv6_prefixes": []
        }
    },
    "202247": {
        "name": "NETBERG - Netpandan ehf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "51019": {
        "name": "BNUYYNET - Kjartan Hrafnkelsson",
        "upstream_bgp_asn": [
            15353,
            16509,
            205794,
            25091,
            3214,
            34549,
            34927,
            398447,
            6939,
            8298,
            835
        ],
        "downstream_bgp_asn": [
            207598,
            57450,
            140731,
            140984,
            204508,
            209718,
            210937,
            211380,
            213151,
            34854,
            34872,
            39351,
            41047,
            41666,
            42541,
            5405,
            56662,
            60326,
            6233,
            7721,
            8888,
            924
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a05:dfc1:ff02::/48",
                "2a05:dfc1:ff00::/48",
                "2a05:dfc1:ffea::/48",
                "2001:67c:bdc::/48",
                "2a14:14c1:100::/48",
                "2a07:54c4:175c::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "202030": {
        "name": "ICELANDAIR-AS - Icelandair ehf",
        "upstream_bgp_asn": [
            2603,
            30818,
            44735,
            6677
        ],
        "downstream_bgp_asn": [
            64708,
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.56.14.0/24",
                "185.56.15.0/24",
                "185.56.13.0/24",
                "185.56.12.0/22",
                "185.56.12.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203322": {
        "name": "EIMSKIP-AS - Eimskip Island ehf",
        "upstream_bgp_asn": [
            30818
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.138.172.0/22",
                "185.138.172.0/23",
                "185.138.174.0/23"
            ],
            "ipv6_prefixes": [
                "2a07:fc0::/29"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203590": {
        "name": "SENSA-AS - Sensa ehf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203566": {
        "name": "MILAHF-AS2 - Mila hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203715": {
        "name": "ISA - Isavia ohf",
        "upstream_bgp_asn": [
            12969,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.126.60.0/23",
                "185.126.62.0/23"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "29689": {
        "name": "ORIGO-AS - Origo hf",
        "upstream_bgp_asn": [
            13335,
            2603,
            44735,
            6677
        ],
        "downstream_bgp_asn": [
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "80.248.16.0/20",
                "217.28.176.0/20",
                "87.121.23.0/24",
                "185.30.184.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "203176": {
        "name": "RB - Reiknistofa bankanna hf.",
        "upstream_bgp_asn": [
            12969,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "193.4.166.0/24",
                "194.144.249.112/28",
                "193.4.97.232/29",
                "194.144.249.96/28",
                "185.29.198.0/24",
                "185.29.196.0/22",
                "217.151.180.0/28",
                "193.4.113.32/27"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "204588": {
        "name": "PROTEGION - Rapyd Europe hf.",
        "upstream_bgp_asn": [
            13335,
            47828
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.240.42.0/24",
                "185.240.41.0/24",
                "185.240.43.0/24",
                "185.240.40.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "202868": {
        "name": "TSC - Nova hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "205436": {
        "name": "ASWINTERMUTE - Wintermute Technologies EHF",
        "upstream_bgp_asn": [
            12357,
            12969,
            49282,
            56704
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "147.28.18.0/24",
                "147.28.16.0/23",
                "147.28.22.0/24",
                "185.156.23.0/24",
                "147.28.17.0/24",
                "185.156.20.0/24",
                "147.28.16.0/24",
                "185.156.21.0/24",
                "185.156.20.0/23",
                "147.28.18.0/23",
                "185.156.22.0/24",
                "147.28.19.0/24",
                "147.28.23.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "147.28.24.0/21",
                "147.28.20.0/23"
            ],
            "ipv6_prefixes": []
        }
    },
    "200432": {
        "name": "BORGUN - Teya Iceland hf",
        "upstream_bgp_asn": [
            12703,
            36351,
            44735,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.107.62.0/24",
                "185.107.61.0/24",
                "185.107.63.0/24",
                "185.107.60.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206010": {
        "name": "RFS - Umbra Service Center Management",
        "upstream_bgp_asn": [
            48685,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.198.144.0/22"
            ],
            "ipv6_prefixes": [
                "2a0a:89c0::/29"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206440": {
        "name": "NETPANDAN - Netpandan ehf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "204926": {
        "name": "IS-GUNNAR - Gunnar Gudvardarson",
        "upstream_bgp_asn": [
            30818,
            6939
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2001:678:58c::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206669": {
        "name": "GAGNAVEITAN - Gagnaveitan ehf.",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.179.78.0/24",
                "185.179.79.0/24",
                "185.179.77.0/24",
                "185.179.76.0/24",
                "185.179.76.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206743": {
        "name": "SECURITASICELAND - Securitas hf.",
        "upstream_bgp_asn": [
            12969
        ],
        "downstream_bgp_asn": [
            64627
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.177.134.0/24",
                "185.177.132.0/23",
                "185.177.135.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "6677": {
        "name": "ICENET-AS1 - Mila hf",
        "upstream_bgp_asn": [
            1103,
            1239,
            12552,
            1267,
            12779,
            1299,
            13030,
            132337,
            137409,
            15802,
            15830,
            15958,
            174,
            20562,
            20764,
            2119,
            24961,
            25091,
            30818,
            30900,
            31500,
            3216,
            328832,
            3303,
            33891,
            34019,
            34549,
            34927,
            35280,
            37100,
            37468,
            39351,
            41327,
            42708,
            43727,
            4455,
            47147,
            47160,
            48362,
            50629,
            50673,
            5713,
            60171,
            6057,
            6424,
            6461,
            6777,
            6939,
            7195,
            8218,
            8220,
            8447,
            8758,
            8896,
            8932,
            9002,
            9009,
            9044,
            9304,
            9498
        ],
        "downstream_bgp_asn": [
            1850,
            197973,
            199844,
            200432,
            202030,
            203176,
            203715,
            206010,
            210747,
            216293,
            25244,
            29689,
            31236,
            39472,
            39532,
            39832,
            42888,
            43892,
            44477,
            44644,
            47545,
            47828,
            48685,
            51296,
            51896,
            57043,
            59396,
            1140,
            12350,
            12637,
            12859,
            12969,
            13237,
            14630,
            14840,
            14907,
            15435,
            15547,
            15605,
            17639,
            18106,
            1828,
            198150,
            199524,
            199938,
            207841,
            20932,
            212483,
            213241,
            23106,
            24482,
            25160,
            25220,
            263152,
            271253,
            28792,
            29140,
            31027,
            31122,
            3170,
            31742,
            3214,
            3333,
            3399,
            34177,
            34288,
            35266,
            35598,
            36236,
            37721,
            39122,
            396998,
            41047,
            41095,
            42473,
            42541,
            45489,
            48070,
            48919,
            49544,
            49605,
            50300,
            50304,
            50763,
            51088,
            51184,
            51185,
            51873,
            52320,
            5405,
            559,
            56987,
            57406,
            59605,
            62167,
            6233,
            6667,
            6894,
            8283,
            8455,
            8607,
            8888,
            917,
            1850,
            197973,
            199844,
            200432,
            202030,
            203176,
            203715,
            206010,
            210747,
            216293,
            25244,
            29689,
            31236,
            39472,
            39532,
            39832,
            42888,
            43892,
            44477,
            44644,
            47545,
            47828,
            48685,
            51296,
            51896,
            57043,
            59396
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "157.157.0.0/16",
                "31.209.192.0/18",
                "192.147.34.0/24",
                "213.167.150.0/24",
                "212.30.212.0/24",
                "213.167.128.0/19",
                "185.44.204.0/24",
                "157.157.2.0/24",
                "157.157.4.0/24",
                "194.105.224.0/19",
                "194.105.224.0/24",
                "212.30.192.0/19",
                "85.220.0.0/17"
            ],
            "ipv6_prefixes": [
                "2a13:9900::/32",
                "2001:1a98::/29"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "206842": {
        "name": "TACTICA - Tactica ehf",
        "upstream_bgp_asn": [
            30818
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.174.176.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "207295": {
        "name": "AS-THORIX-RS - Northlayer ehf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "207598": {
        "name": "LSG-AS - Leifur Steinn Gunnarsson",
        "upstream_bgp_asn": [
            51019
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a07:54c4:73d1::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "210747": {
        "name": "IHOTELS - BERJAYA HOTELS ICELAND hf",
        "upstream_bgp_asn": [
            44735,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "193.243.188.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "211757": {
        "name": "PANASCAIS - Panascais ehf.",
        "upstream_bgp_asn": [
            20473
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "31.43.173.0/24",
                "31.43.172.0/24"
            ],
            "ipv6_prefixes": [
                "2a10:9840:2::/48",
                "2a10:9840:1::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "209933": {
        "name": "DANDRI - David Andri Jakobsson",
        "upstream_bgp_asn": [
            34927,
            39249,
            6939,
            8772
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2001:678:888::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "210080": {
        "name": "TOLVUTHJONUSTAN - Tolvuthjonustan ehf.",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.221.176.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "209214": {
        "name": "IS-NETHEIMUR - Netheimur ehf.",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.248.120.0/22"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "211589": {
        "name": "RUV-CDN - Rikisutvarpid Ohf",
        "upstream_bgp_asn": [
            48685
        ],
        "downstream_bgp_asn": [
            12969
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "37.152.71.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "212926": {
        "name": "HARPA-AS - Harpa Concert Hall and Conference Centre ohf",
        "upstream_bgp_asn": [
            12969,
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "88.135.70.0/24"
            ],
            "ipv6_prefixes": [
                "2a07:e8c0::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "208548": {
        "name": "KJARNET-0 - Kjartan Hrafnkelsson",
        "upstream_bgp_asn": [
            400587,
            50224,
            52041
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a07:54c4:a60::/44",
                "2a07:54c2:1c00::/38",
                "2a07:54c4:13f0::/44"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "211815": {
        "name": "LANDSVIRKJUN-AS - Landsvirkjun",
        "upstream_bgp_asn": [
            12969
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.236.130.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "211734": {
        "name": "IS-VEGAGERDIN - Vegagerdin",
        "upstream_bgp_asn": [
            30818
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.147.136.0/22",
                "185.147.136.0/24",
                "185.147.137.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "213239": {
        "name": "NORTHLAYER-AS2 - Northlayer ehf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "212771": {
        "name": "NETVOKTUN - Netvoktun ehf",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.43.30.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "213364": {
        "name": "IS-STEINN-6 - STEINN ORVAR BJARNARSON",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "215793": {
        "name": "SIMINN - Siminn hf. (Iceland Telecom)",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "215608": {
        "name": "SAMGONGUSTOFA - Samgongustofa",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "216017": {
        "name": "OKH-2 - Opin Kerfi hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "216260": {
        "name": "TSICELAND - Tech tolvu- og rekstrarla ehf.",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "214718": {
        "name": "WISE - Thekking - Tristan hf",
        "upstream_bgp_asn": [],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "216293": {
        "name": "TS - TechSupport ehf",
        "upstream_bgp_asn": [
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "212.46.60.0/24"
            ],
            "ipv6_prefixes": [
                "2a13:d9c0::/29"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "215823": {
        "name": "FOSSHALS-LAN - Spaugur ehf.",
        "upstream_bgp_asn": [
            209533,
            52025
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a07:54c4::/44"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    },
    "12969": {
        "name": "VODAFONE_ICELAND - Ljosleidarinn ehf",
        "upstream_bgp_asn": [
            1103,
            12552,
            1267,
            1273,
            12779,
            13194,
            132337,
            137409,
            15576,
            15802,
            15830,
            15958,
            1764,
            20562,
            20764,
            24961,
            25091,
            2603,
            29075,
            31042,
            31133,
            3214,
            3216,
            328832,
            33891,
            34019,
            34549,
            3462,
            34927,
            35280,
            37100,
            37468,
            39351,
            41327,
            43727,
            4455,
            47147,
            47160,
            48200,
            48362,
            48858,
            50304,
            50629,
            50673,
            5713,
            57304,
            60171,
            6057,
            62275,
            6424,
            6461,
            6777,
            6939,
            7195,
            8447,
            8758,
            8896,
            8932,
            9002,
            9044,
            9498
        ],
        "downstream_bgp_asn": [
            197403,
            198815,
            199844,
            203176,
            203715,
            205436,
            206743,
            20963,
            211815,
            212926,
            24743,
            31441,
            39472,
            39532,
            47828,
            57729,
            1140,
            12637,
            12859,
            13237,
            14630,
            14840,
            14907,
            15435,
            15547,
            15605,
            17639,
            18106,
            1828,
            198150,
            199524,
            199938,
            207841,
            20932,
            212483,
            213241,
            23106,
            24482,
            25160,
            25220,
            263152,
            271253,
            28792,
            29140,
            31027,
            31122,
            3170,
            31742,
            3333,
            3399,
            34177,
            34288,
            35266,
            35598,
            36236,
            37721,
            39122,
            396998,
            41047,
            42473,
            42541,
            45489,
            48070,
            48919,
            49544,
            49605,
            50300,
            50763,
            51088,
            51184,
            51185,
            51873,
            52320,
            5405,
            559,
            56987,
            57406,
            59605,
            62167,
            6233,
            6894,
            8283,
            8888,
            917,
            10310,
            1031,
            10474,
            11019,
            1101,
            11179,
            11260,
            1126,
            112,
            1140,
            1200,
            1213,
            12200,
            12329,
            12355,
            12390,
            12399,
            12400,
            12414,
            1241,
            12440,
            12488,
            1248,
            12491,
            12496,
            12576,
            12578,
            12637,
            12693,
            12695,
            12703,
            12713,
            12731,
            12759,
            12850,
            12859,
            12874,
            12876,
            12883,
            12888,
            12902,
            13002,
            13009,
            13037,
            13101,
            13122,
            13150,
            131958,
            13208,
            13213,
            132203,
            13237,
            13249,
            13280,
            13285,
            132876,
            13335,
            13414,
            135391,
            136106,
            136907,
            13768,
            138322,
            138915,
            13896,
            139057,
            139341,
            139628,
            13984,
            140443,
            14061,
            14127,
            14537,
            14593,
            14630,
            14907,
            15133,
            15169,
            15435,
            15447,
            15474,
            1547,
            15502,
            15510,
            15547,
            15605,
            15606,
            15654,
            15695,
            15703,
            15766,
            15806,
            15895,
            15943,
            15966,
            15967,
            16082,
            16097,
            16164,
            16171,
            16247,
            16265,
            16276,
            16298,
            16353,
            16509,
            16552,
            16637,
            1680,
            17088,
            17557,
            17639,
            18001,
            18059,
            18106,
            1820,
            18283,
            1828,
            1921,
            19551,
            196752,
            19679,
            196844,
            196881,
            196954,
            197000,
            19711,
            197156,
            197403,
            197440,
            197692,
            197727,
            197731,
            197790,
            197898,
            197981,
            198046,
            198089,
            198440,
            198554,
            198736,
            198781,
            198792,
            198815,
            198930,
            198967,
            199181,
            199335,
            199452,
            199468,
            199481,
            199483,
            199524,
            199599,
            199659,
            199713,
            199716,
            199775,
            199844,
            199938,
            199939,
            199995,
            200020,
            200023,
            200052,
            200070,
            200197,
            200478,
            200562,
            200565,
            200596,
            200612,
            200781,
            201119,
            201126,
            201261,
            201277,
            201290,
            201401,
            201791,
            201838,
            201877,
            2018,
            202020,
            202030,
            202053,
            202282,
            202425,
            20253,
            202596,
            202932,
            202954,
            203101,
            203176,
            20326,
            203372,
            203421,
            203536,
            203568,
            203582,
            203715,
            203724,
            203754,
            203851,
            203936,
            204264,
            204536,
            204558,
            204598,
            20473,
            204805,
            20495,
            204995,
            20504,
            205389,
            205436,
            20546,
            205479,
            20559,
            205668,
            205689,
            205771,
            205892,
            205943,
            205975,
            206067,
            206264,
            206347,
            206446,
            20647,
            206483,
            206530,
            206626,
            206663,
            206735,
            206743,
            20681,
            206934,
            206999,
            207044,
            207063,
            207083,
            20712,
            207176,
            207375,
            207594,
            20766,
            20773,
            207790,
            207841,
            207934,
            207995,
            20799,
            208034,
            20804,
            208189,
            20847,
            20857,
            20860,
            208621,
            208802,
            208844,
            20886,
            209045,
            20915,
            209181,
            209326,
            20932,
            20940,
            20963,
            20969,
            209768,
            210062,
            210083,
            21013,
            210627,
            210874,
            210893,
            21099,
            211029,
            2110,
            211307,
            211393,
            211589,
            211597,
            211713,
            211815,
            211826,
            212027,
            212109,
            21221,
            212232,
            212263,
            212312,
            212477,
            21263,
            212655,
            21267,
            2128,
            212926,
            213050,
            213052,
            213054,
            213094,
            213241,
            213373,
            21409,
            21472,
            21574,
            216071,
            21859,
            22356,
            22697,
            22822,
            23028,
            23106,
            23344,
            23576,
            23764,
            23889,
            23944,
            23947,
            24429,
            24482,
            24586,
            24594,
            24730,
            24743,
            2484,
            24875,
            24904,
            24916,
            24940,
            25133,
            25151,
            25152,
            25160,
            25220,
            25369,
            25376,
            25428,
            25441,
            25455,
            25460,
            25509,
            25521,
            25818,
            2611,
            262589,
            262725,
            263528,
            2635,
            26415,
            26464,
            265038,
            267613,
            2686,
            270814,
            28008,
            2818,
            28283,
            2852,
            2854,
            28725,
            28788,
            28792,
            28917,
            29006,
            29017,
            29049,
            2906,
            29119,
            29140,
            29141,
            29208,
            29263,
            29314,
            293,
            29419,
            29452,
            29467,
            29505,
            29527,
            29606,
            29611,
            29632,
            29668,
            29689,
            29802,
            29838,
            30058,
            30081,
            30103,
            30740,
            30818,
            30827,
            30844,
            30900,
            30925,
            31019,
            31084,
            31122,
            31319,
            31424,
            31441,
            31449,
            31472,
            31477,
            31500,
            31515,
            31529,
            31631,
            31638,
            31673,
            31708,
            3170,
            31727,
            31742,
            31898,
            3213,
            3223,
            32590,
            327814,
            32787,
            328366,
            328748,
            32934,
            33182,
            3326,
            3327,
            3333,
            33353,
            33763,
            33920,
            33986,
            3399,
            34066,
            34087,
            34119,
            34141,
            34177,
            34224,
            34245,
            34270,
            34288,
            34428,
            34442,
            34655,
            34746,
            34756,
            34772,
            34863,
            34953,
            34968,
            35000,
            35180,
            35228,
            35266,
            35297,
            35313,
            35320,
            35399,
            35432,
            35437,
            35551,
            35574,
            35575,
            35598,
            35709,
            35729,
            35753,
            35793,
            35826,
            35834,
            36182,
            36236,
            36351,
            36692,
            36864,
            36868,
            36874,
            36916,
            36944,
            36994,
            37054,
            37119,
            37282,
            3741,
            37613,
            37678,
            37680,
            37721,
            38040,
            3856,
            38623,
            38719,
            38758,
            38880,
            38915,
            38983,
            39063,
            39090,
            39093,
            39120,
            39122,
            39175,
            39180,
            39202,
            39208,
            3920,
            39233,
            39319,
            39356,
            39386,
            39449,
            39472,
            39498,
            39521,
            39532,
            39537,
            395505,
            39572,
            39591,
            396356,
            39637,
            39647,
            39686,
            396986,
            396998,
            39704,
            39737,
            39832,
            39839,
            398465,
            39878,
            39923,
            4004,
            40401,
            40627,
            40850,
            40999,
            41000,
            41041,
            41073,
            41090,
            41107,
            41230,
            41313,
            41354,
            41405,
            41495,
            41529,
            41552,
            41692,
            41811,
            41820,
            41887,
            41913,
            41960,
            42090,
            42093,
            42184,
            42295,
            42310,
            42344,
            42366,
            42385,
            42473,
            42541,
            42567,
            42611,
            42649,
            42689,
            42707,
            42755,
            42831,
            42841,
            42861,
            42947,
            42,
            43013,
            43142,
            43190,
            43192,
            43256,
            43350,
            43366,
            43406,
            43414,
            43519,
            43566,
            43599,
            43641,
            43668,
            43872,
            43942,
            43984,
            43996,
            44034,
            44123,
            44212,
            44314,
            44356,
            44384,
            44592,
            44608,
            44684,
            44735,
            44788,
            44858,
            44901,
            44965,
            45014,
            45102,
            45430,
            45437,
            45474,
            45489,
            45701,
            45758,
            45899,
            46244,
            4637,
            46489,
            4651,
            4657,
            46844,
            47172,
            47447,
            47480,
            4761,
            47631,
            47638,
            47674,
            47680,
            47720,
            4775,
            47828,
            47836,
            4788,
            47942,
            47957,
            47973,
            47998,
            47999,
            4800,
            48070,
            48101,
            48237,
            48266,
            48284,
            48294,
            48305,
            48314,
            48519,
            48635,
            48685,
            48688,
            48825,
            48919,
            48945,
            49033,
            49121,
            49127,
            49158,
            49375,
            49415,
            49425,
            49463,
            49544,
            49567,
            49572,
            49600,
            49605,
            49627,
            49653,
            49685,
            49800,
            49820,
            49823,
            49870,
            49981,
            50023,
            50072,
            50083,
            50245,
            50263,
            50266,
            50272,
            50295,
            50300,
            50309,
            50316,
            50326,
            50340,
            50384,
            50489,
            50522,
            50581,
            50763,
            50812,
            50823,
            50858,
            50889,
            50923,
            51043,
            51050,
            51055,
            51088,
            51167,
            51184,
            51185,
            51265,
            51276,
            51409,
            51468,
            51553,
            51561,
            51752,
            51809,
            51823,
            51873,
            51896,
            51945,
            52075,
            52320,
            52551,
            53062,
            53180,
            53334,
            5390,
            5394,
            5404,
            5405,
            54113,
            5416,
            54309,
            5459,
            5466,
            54825,
            5482,
            54994,
            5500,
            5503,
            55219,
            5524,
            55256,
            55329,
            55685,
            55818,
            5583,
            559,
            5606,
            5631,
            56329,
            56382,
            56410,
            56474,
            56478,
            56595,
            56630,
            56654,
            56655,
            56665,
            56704,
            56767,
            56911,
            56987,
            56990,
            57043,
            57112,
            57154,
            57169,
            57344,
            57356,
            57463,
            57508,
            57575,
            57653,
            57729,
            57793,
            57811,
            57976,
            58007,
            58138,
            58226,
            58272,
            58273,
            58291,
            58453,
            58511,
            58807,
            59110,
            59395,
            59439,
            59455,
            59545,
            59605,
            59624,
            59659,
            59692,
            59711,
            59778,
            59811,
            59865,
            59908,
            59933,
            60022,
            60064,
            60277,
            60294,
            60350,
            60377,
            60439,
            60476,
            60486,
            60610,
            60670,
            60672,
            60690,
            60793,
            60800,
            60822,
            60868,
            61124,
            61135,
            61157,
            61194,
            61215,
            61231,
            61323,
            61349,
            61599,
            61955,
            62041,
            62044,
            6204,
            6206,
            62105,
            62163,
            62167,
            62217,
            62227,
            62240,
            6233,
            62663,
            62713,
            62715,
            62856,
            62902,
            62955,
            63113,
            63399,
            63927,
            63949,
            64049,
            64289,
            64522,
            64528,
            64532,
            64538,
            64539,
            64560,
            64568,
            64581,
            64666,
            64701,
            64702,
            65000,
            6507,
            65106,
            65202,
            65500,
            65532,
            65534,
            6661,
            6663,
            6677,
            6681,
            6717,
            6768,
            6775,
            6834,
            6866,
            714,
            7342,
            7522,
            7642,
            7979,
            8038,
            8075,
            8262,
            8282,
            8283,
            8301,
            8304,
            8309,
            8315,
            8365,
            8368,
            8399,
            8400,
            8422,
            8426,
            8452,
            8462,
            8468,
            8473,
            8487,
            8529,
            8530,
            8544,
            8551,
            8560,
            8587,
            8632,
            8637,
            8647,
            8674,
            8680,
            8681,
            8683,
            8732,
            8752,
            8757,
            8763,
            8764,
            8767,
            8821,
            8839,
            8859,
            8866,
            8881,
            8888,
            8918,
            8953,
            9009,
            9031,
            9036,
            9050,
            9116,
            9119,
            9123,
            9136,
            9145,
            9150,
            9153,
            9264,
            9299,
            9304,
            9354,
            9381,
            9583,
            9605,
            983,
            9902
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "193.4.4.0/24",
                "213.176.131.0/24",
                "185.21.16.0/23",
                "217.171.208.0/20",
                "5.23.80.0/20",
                "193.4.5.0/24",
                "193.4.56.0/23",
                "81.15.0.0/17",
                "194.144.0.0/16",
                "217.9.128.0/20",
                "89.160.128.0/17",
                "213.213.128.0/19",
                "185.21.16.0/22",
                "193.4.60.0/22",
                "185.21.18.0/23",
                "213.176.128.0/19",
                "46.239.192.0/19",
                "62.145.128.0/19",
                "88.149.0.0/17",
                "5.23.64.0/20",
                "193.4.48.0/21",
                "213.220.64.0/18",
                "193.4.64.0/18",
                "217.151.160.0/19",
                "185.177.132.0/22",
                "46.239.192.0/18",
                "5.23.64.0/19",
                "193.4.0.0/19",
                "193.4.128.0/17",
                "185.24.0.0/23",
                "46.239.224.0/19",
                "185.24.0.0/22"
            ],
            "ipv6_prefixes": [
                "2a02:48::/32",
                "2a00:4d60::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "217.151.176.0/20",
                "217.151.160.0/20"
            ],
            "ipv6_prefixes": [
                "2a02:4c::/30",
                "2a02:4a::/31",
                "2a02:49::/32"
            ]
        }
    }
}
```
</details>
