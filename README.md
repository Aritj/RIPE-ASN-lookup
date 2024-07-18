# RIPE-ASN-lookup
This project identifies all ASNs for any given country code (cc) and determines the associated IP prefixes, checking which are advertised. Initially inspired by an interest in the ASNs and IP prefixes for the Faroe Islands (FO), this tool uses RIPE NCC data to provide insights into IP address allocations and advertisement status.


## Generating the example files
This project includes two example .json files, which have been generated as follows:

```
(base) aritj@Aris-MBP Projects copy % python3 lookup.py fo
ASN data written to fo_asn_data_20240718_231802.json
(base) aritj@Aris-MBP Projects copy % python3 lookup.py fo 4
ASN data written to fo_asn_data_20240718_231810.json
```
