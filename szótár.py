dic1 = {"kulcs1": "érték1", "kulcs2": "érték2"}
print(dic1["kulcs1"])

dic2 = {"k1": 123, "k2": [12, 23, 34], "k3": ["alma", "banán", "eper"]}
print(dic2["k3"][0].upper())
dic2["k2"].append(55)
print(dic2)
dic3 = {"k1": "alma", "k2": {"ak1": {"aak1": "citrom"}} }
print(dic3["k2"]["ak1"]["aak1"])
print(dic2.keys())
print(dic2.values())
print(dic2.items())
print(dic2.get("k1"))
dic4 = {}
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
dic2.clear()
print(dic2)
print(dic2.get("k2", "Ez a kulcs nem szerepel szotárban"))