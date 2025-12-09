dic1 = {"kulcs1": "Noiser", "kulcs2": "Noisericious"}
print(dic1)
print(dic1["kulcs1"])
print(dic1["kulcs2"])

dic2 = {"key1": "Noiser1", "key2": [12, 23, 34], "key3": ["alma", "banán", "eper"]}
print(dic2)
print(dic2["key3"][1].upper())
print(dic2["key3"][1])

dic3 = {"key1": "alma", "key2": {"alkey1": {"alalkey1": "citrom"}} }
print(dic3)
print(dic3["key1"])
print(dic3["key2"])
print(dic3["key2"]["alkey1"]["alalkey1"])
print(dic2.keys())
print(dic2.values())
print(dic2.items())
print(dic2.get("key1"))

dic4 = {}
dic4.update(dic2)
print(dic4)
dic4.update(dic3)
print(dic4)
dic2.clear()
print(dic2)
print(dic2.get("key2", "Ez a kulcs nem szerepel szotárban"))
