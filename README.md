# RIPE-CC-prefix-lookup
This project identifies all ASNs for any given country code (cc) and determines the associated IP prefixes, checking which are advertised. Initially inspired by an interest in the ASNs and IP prefixes for the Faroe Islands (FO), this tool uses RIPE NCC data to provide insights into IP address allocations and advertisement status.


## Generating the example files

### Faroe Islands
```bash
> python3 lookup.py fo
```
Generates an output file called fo_asn_data_{timestamp}.json:
```json
{"15389": {"name": "FAROESE-TELECOM-AS - P/F Telefonverkid", "announced": {"ipv4_prefixes": ["81.18.224.0/20", "217.172.80.0/20", "178.19.192.0/20", "88.85.32.0/19", "212.55.32.0/19", "193.34.104.0/22", "185.74.208.0/22", "198.137.136.0/22"], "ipv6_prefixes": ["2a02:e90::/32"]}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": ["2a02:e90::/29"]}}, "20963": {"name": "NEMAFAROE - P/F 20.11.19", "announced": {"ipv4_prefixes": ["81.25.176.0/20", "80.77.128.0/20", "46.227.112.0/21", "185.88.228.0/22"], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "200664": {"name": "PF-FTNET - P/F Net", "announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "206928": {"name": "PF-ELEKTRON - P/F Elektron", "announced": {"ipv4_prefixes": ["185.171.172.0/22"], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "209175": {"name": "KRINGVARP_FOROYA - Kringvarp Foroya", "announced": {"ipv4_prefixes": ["195.80.36.0/22"], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}, "210417": {"name": "NET2 - P/F Net", "announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}, "not_announced": {"ipv4_prefixes": [], "ipv6_prefixes": []}}}
```
We can also control the JSON formatting (indentation level):
```bash
> python3 lookup.py fo 4
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
                "81.18.224.0/20",
                "198.137.136.0/22",
                "185.74.208.0/22",
                "88.85.32.0/19",
                "178.19.192.0/20",
                "193.34.104.0/22",
                "212.55.32.0/19",
                "217.172.80.0/20"
            ],
            "ipv6_prefixes": [
                "2a02:e90::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2a02:e90::/29"
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
                "185.88.228.0/22",
                "81.25.176.0/20",
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


### Greenland
```bash
> python3 lookup.py gl 4
```
Generates an output file called gl_asn_data_{timestamp}.json with the following contents:
<details>
  <summary>View output</summary>
    
  ```json
{
    "8818": {
        "name": "Tusass A/S",
        "upstream_bgp_asn": [
            3356
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
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
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": []
        }
    }
}
  ```
</details>

### Iceland
```bash
> python3 lookup.py is 4
```
Generates an output file called is_asn_data_{timestamp}.json with the following contents:
<details>
  <summary>View output</summary>
    
```json
{
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
                "193.4.58.0/23",
                "185.93.156.0/22"
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
            24482,
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
            59396
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "157.157.2.0/24",
                "185.44.204.0/24",
                "212.30.212.0/24",
                "213.167.128.0/19",
                "157.157.4.0/24",
                "194.105.224.0/24",
                "157.157.0.0/16",
                "194.105.224.0/19",
                "85.220.0.0/17",
                "31.209.192.0/18",
                "213.167.150.0/24",
                "192.147.34.0/24",
                "212.30.192.0/19"
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
            24482,
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
            57729
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "213.176.128.0/19",
                "185.21.16.0/23",
                "217.151.160.0/19",
                "88.149.0.0/17",
                "185.21.18.0/23",
                "193.4.48.0/21",
                "5.23.64.0/20",
                "89.160.128.0/17",
                "193.4.60.0/22",
                "213.220.64.0/18",
                "46.239.192.0/19",
                "185.21.16.0/22",
                "5.23.64.0/19",
                "217.171.208.0/20",
                "185.24.0.0/23",
                "213.176.131.0/24",
                "193.4.4.0/24",
                "185.177.132.0/22",
                "213.213.128.0/19",
                "194.144.0.0/16",
                "46.239.192.0/18",
                "217.9.128.0/20",
                "193.4.56.0/23",
                "46.239.224.0/19",
                "185.24.0.0/22",
                "81.15.0.0/17",
                "193.4.0.0/19",
                "193.4.64.0/18",
                "5.23.80.0/20",
                "193.4.128.0/17",
                "62.145.128.0/19",
                "193.4.5.0/24"
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
                "2a02:48::/29"
            ]
        }
    },
    "15474": {
        "name": "RHNET - Rannsokna- og haskolanet Islands hf.",
        "upstream_bgp_asn": [
            2603
        ],
        "downstream_bgp_asn": [
            25244,
            29348
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
                "193.109.25.0/24",
                "193.109.16.0/20"
            ],
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
                "212.126.240.0/21",
                "212.126.224.0/19"
            ],
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
    "29689": {
        "name": "ORIGO-AS - Origo hf",
        "upstream_bgp_asn": [
            13335,
            2603,
            44735,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "80.248.16.0/20",
                "185.30.184.0/22",
                "87.121.23.0/24",
                "217.28.176.0/20"
            ],
            "ipv6_prefixes": []
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
            1299,
            202030,
            203322,
            204926,
            206842,
            211734,
            3257,
            39472,
            44515,
            50613,
            6677
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "82.221.164.0/24",
                "82.221.170.0/24"
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
                "82.112.64.0/19",
                "82.112.93.0/24",
                "82.112.94.0/24",
                "82.112.90.0/24",
                "94.198.48.0/23",
                "82.112.85.0/24",
                "160.20.214.0/23"
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
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "87.237.36.0/24",
                "87.237.39.0/24",
                "87.237.38.0/24",
                "87.237.33.0/24",
                "87.237.34.0/24",
                "87.237.38.0/23",
                "87.237.32.0/24",
                "87.237.34.0/23",
                "87.237.32.0/23"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "87.237.32.0/21"
            ],
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
                "88.151.52.0/22",
                "88.151.48.0/22",
                "88.151.48.0/21"
            ],
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
                "79.171.96.0/21",
                "185.62.60.0/22",
                "185.67.180.0/22",
                "185.130.12.0/22"
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
    "44515": {
        "name": "IS-ADVANIA - Advania Island ehf",
        "upstream_bgp_asn": [
            30818
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "82.221.88.0/22",
                "212.30.224.0/19",
                "82.221.80.0/21",
                "193.181.194.0/24",
                "82.221.80.0/24",
                "212.30.229.0/24",
                "212.30.242.0/24",
                "82.221.84.0/24",
                "82.221.28.0/24",
                "82.221.0.0/21",
                "82.221.92.0/22",
                "82.221.161.0/24",
                "82.221.81.0/24",
                "82.221.22.0/24",
                "82.221.0.0/17",
                "82.221.162.0/24"
            ],
            "ipv6_prefixes": [
                "2a02:f48::/40",
                "2a02:f48:2100::/40"
            ]
        },
        "not_announced_prefixes": {
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
            24482,
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
            65323
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.40.120.0/22",
                "185.152.116.0/22",
                "149.126.80.0/21",
                "153.92.128.0/19",
                "157.97.0.0/19",
                "91.220.138.0/24",
                "78.40.248.0/21",
                "213.181.96.0/20",
                "178.19.48.0/20",
                "213.181.112.0/20",
                "185.152.119.0/24",
                "213.181.96.0/19",
                "185.111.36.0/22",
                "46.182.184.0/21",
                "78.40.250.0/24"
            ],
            "ipv6_prefixes": [
                "2a00:9280::/32",
                "2a01:8280:dc00::/40",
                "2a13:2440:b0::/48",
                "2a01:8280::/32",
                "2a01:6f00::/29"
            ]
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
                "195.246.230.0/24",
                "89.147.108.0/22",
                "93.95.224.0/21",
                "195.246.231.0/24",
                "185.112.144.0/22",
                "93.95.225.0/24",
                "93.95.231.128/25",
                "93.95.227.0/24",
                "93.95.228.0/24",
                "93.95.230.0/24",
                "93.95.229.0/24",
                "89.147.109.0/24",
                "89.147.108.0/24",
                "185.112.144.0/24",
                "185.112.146.0/24",
                "89.147.110.0/24",
                "185.112.145.0/24",
                "185.112.147.0/24",
                "89.147.111.0/24"
            ],
            "ipv6_prefixes": [
                "2a00:5ee0:2000::/36",
                "2a00:5ee0:2000::/35",
                "2a00:5ee0::/32"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "195.246.230.0/23"
            ],
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
            211589
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "94.250.244.0/23",
                "185.118.32.0/22",
                "176.10.32.0/21",
                "185.25.252.0/22",
                "185.119.124.0/22",
                "94.142.152.0/21",
                "176.57.224.0/20"
            ],
            "ipv6_prefixes": [
                "2a03:5cc0::/32",
                "2a06:a100::/29"
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
                "82.221.131.0/24",
                "82.221.100.0/23",
                "82.221.96.0/19",
                "82.221.130.0/24",
                "82.221.104.0/24",
                "82.221.128.0/19",
                "82.221.129.0/24",
                "82.221.139.0/24",
                "82.221.141.0/24",
                "82.221.143.0/24",
                "37.235.49.0/24",
                "82.221.136.0/24",
                "82.221.105.0/24",
                "82.221.111.0/24",
                "82.221.128.0/24",
                "151.236.24.0/24",
                "192.71.218.0/24",
                "193.107.84.0/22",
                "82.221.113.0/24"
            ],
            "ipv6_prefixes": [
                "2a02:f48:2000::/40",
                "2a03:f80:354::/48"
            ]
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
            57450
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [],
            "ipv6_prefixes": [
                "2001:67c:bdc::/48",
                "2a14:14c1:100::/48",
                "2a05:dfc1:ffea::/48",
                "2a05:dfc1:ff02::/48",
                "2a07:54c4:175c::/48",
                "2a05:dfc1:ff00::/48"
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
    "51896": {
        "name": "HRINGDU-AS - Hringdu ehf",
        "upstream_bgp_asn": [
            2603,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.191.232.0/22",
                "31.209.152.0/21",
                "46.22.96.0/24",
                "46.22.96.0/20",
                "31.209.144.0/21",
                "89.17.128.0/19",
                "31.209.136.0/21"
            ],
            "ipv6_prefixes": [
                "2a00:5000::/29"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "31.209.144.0/20"
            ],
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
            48685
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.154.116.0/22",
                "31.15.112.0/21",
                "185.217.58.0/24",
                "139.28.147.0/24",
                "185.252.165.0/24",
                "185.159.158.0/24"
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
    "57508": {
        "name": "AS-ALZA-IS - Alza ehf",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "91.220.110.0/24",
                "185.221.232.0/22"
            ],
            "ipv6_prefixes": [
                "2a0c:7000::/29",
                "2001:67c:2aac::/48"
            ]
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
    "60690": {
        "name": "OPEX-ASN - Opin Kerfi hf",
        "upstream_bgp_asn": [
            2603,
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.67.84.0/22",
                "185.27.36.0/22",
                "185.109.100.0/22",
                "178.248.16.0/21",
                "93.95.72.0/21",
                "185.123.196.0/22",
                "185.219.148.0/22"
            ],
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
    "197403": {
        "name": "ISLANDSBANKI-AS1 - Islandsbanki hf",
        "upstream_bgp_asn": [
            12969,
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "46.28.152.0/21",
                "46.28.157.0/24"
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
                "37.152.64.0/21"
            ],
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
                "185.107.63.0/24",
                "185.107.61.0/24",
                "185.107.60.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "185.107.60.0/22"
            ],
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
                "185.100.84.0/23",
                "185.146.233.0/24",
                "185.165.170.0/24",
                "185.165.169.0/24",
                "185.100.87.0/24",
                "185.247.225.0/24",
                "81.180.202.0/23",
                "37.228.129.0/24",
                "185.165.168.0/24",
                "185.100.86.0/24",
                "185.247.224.0/24",
                "185.246.189.0/24",
                "185.146.232.0/24",
                "37.156.68.0/24",
                "185.165.171.0/24",
                "185.10.68.0/24",
                "185.246.188.0/24",
                "185.247.226.0/24",
                "37.228.128.0/24"
            ],
            "ipv6_prefixes": [
                "2a06:1700::/48",
                "2a06:1700:3::/48",
                "2a06:1700:2::/48",
                "2a06:1700:100::/48",
                "2a06:1700:4::/48",
                "2a06:1700:1::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "185.146.232.0/22",
                "185.100.84.0/22",
                "185.247.224.0/22",
                "185.246.188.0/22",
                "185.165.168.0/22"
            ],
            "ipv6_prefixes": [
                "2a06:1700::/29"
            ]
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
                "213.181.126.0/23",
                "185.86.220.0/22"
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
    "202030": {
        "name": "ICELANDAIR-AS - Icelandair ehf",
        "upstream_bgp_asn": [
            2603,
            30818,
            44735,
            6677
        ],
        "downstream_bgp_asn": [
            64708
        ],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.56.12.0/22",
                "185.56.14.0/24",
                "185.56.13.0/24",
                "185.56.15.0/24",
                "185.56.12.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [],
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
    "203176": {
        "name": "RB - Reiknistofa bankanna hf.",
        "upstream_bgp_asn": [
            12969,
            6677
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.29.196.0/22",
                "217.151.180.0/28",
                "194.144.249.96/28",
                "194.144.249.112/28",
                "185.29.198.0/24",
                "193.4.166.0/24",
                "193.4.97.232/29",
                "193.4.113.32/27"
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
            "ipv4_prefixes": [
                "185.126.60.0/22"
            ],
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
                "185.240.41.0/24",
                "185.240.40.0/24",
                "185.240.43.0/24",
                "185.240.42.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "185.240.40.0/22"
            ],
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
                "147.28.18.0/23",
                "147.28.22.0/24",
                "147.28.17.0/24",
                "185.156.20.0/24",
                "147.28.18.0/24",
                "185.156.22.0/24",
                "147.28.23.0/24",
                "185.156.23.0/24",
                "185.156.20.0/23",
                "147.28.16.0/24",
                "147.28.19.0/24",
                "147.28.16.0/23",
                "185.156.21.0/24"
            ],
            "ipv6_prefixes": []
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "185.156.20.0/22",
                "147.28.16.0/20"
            ],
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
    "206669": {
        "name": "GAGNAVEITAN - Gagnaveitan ehf.",
        "upstream_bgp_asn": [
            44735
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.179.76.0/22",
                "185.179.79.0/24",
                "185.179.78.0/24",
                "185.179.76.0/24",
                "185.179.77.0/24"
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
                "185.177.132.0/23",
                "185.177.135.0/24",
                "185.177.134.0/24"
            ],
            "ipv6_prefixes": []
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
                "2a07:54c2:1c00::/38",
                "2a07:54c4:a60::/44",
                "2a07:54c4:13f0::/44"
            ]
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
    "211589": {
        "name": "RUV-CDN - Rikisutvarpid Ohf",
        "upstream_bgp_asn": [
            48685
        ],
        "downstream_bgp_asn": [],
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
    "211734": {
        "name": "IS-VEGAGERDIN - Vegagerdin",
        "upstream_bgp_asn": [
            30818
        ],
        "downstream_bgp_asn": [],
        "announced_prefixes": {
            "ipv4_prefixes": [
                "185.147.136.0/24",
                "185.147.136.0/22",
                "185.147.137.0/24"
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
                "2a10:9840:1::/48",
                "2a10:9840:2::/48"
            ]
        },
        "not_announced_prefixes": {
            "ipv4_prefixes": [
                "31.43.172.0/23"
            ],
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
    }
}
```
</details>
