class ValamilyenNev:
    v1 = "alma"

    def __init__(self, nev, kor): #semmi másra nem használható csak inicializálásra
        self.nev = nev
        self.kor = kor

    def osszead(self, a, b):
        return a + b


print(ValamilyenNev.v1)
obj1 = ValamilyenNev("Elek", 33 ) #példányosításkor meghívódik egy spec fgv, init fgv (konstruktor)
print(obj1.v1)
print(obj1.kor)
print(obj1.nev)
print(obj1.osszead(1, 2))

#állásinterjún
class Counter:
    def __init__(self, start=0):
        self.value = start

    def __call__(self, step=1): #mindig meghívódik, ezért ad hozzá plusz egyet
        self.value += step
        return self.value

c = Counter(10)
print(c())
print(c(6))
print(c.value)

def s1(a, b):
    return a + b

print(callable(s1))
print(s1.__call__(1, 2))

class Madar:
    def __init__(self, szine):
        self.szine = szine
        self._v1 = "alma" #protected
        self.__v2 = "citrom" #private

    def fn1(self):
        print(self._v1)
        print(self.__v2)

class Sas(Madar):
    def __init__(self, szine, hus_napi_mennyisege):
        super().__init__(szine)
        self.hus = hus_napi_mennyisege

    def fn2(self):
        print(self.szine)
        print(self._v1)
        #print(self.__v2)

sas1 = Sas("barna", 5)
print(sas1.szine)
print(sas1.hus)
print("-" * 15)
sas1.fn1()
print("-" * 15)
sas1.fn2()
print("-" * 15)
print("adat: ", sas1._v1) #ez nem jól működik.
#print(sas1.__v2)

