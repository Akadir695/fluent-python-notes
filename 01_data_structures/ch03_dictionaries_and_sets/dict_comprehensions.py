# A dictcomp  builds instance by taking key:value pairs from iterable 
# exampe: 3-1 dict comprehensions 
dial_code = [
  (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (7, "Russia"),
    (1, "United States"),
]
# country_dial = {}
# for code, country in dial_code:
#   country_dial[country] = code 
country_dial = {country: code for code, country in dial_code}
print(country_dial)
# {'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62, 'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}
low_codes ={code: country.upper()
 for country, code in sorted(country_dial.items())
 if code < 70 
 }
print(low_codes)
