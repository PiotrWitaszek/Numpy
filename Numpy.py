import numpy as np
import numpy_financial as npf

print("Zadanie 1")
rate = 0.05
nper = 5
pmt = 0
pv = 120000
price = npf.fv(rate, nper, pmt, -pv)
print(f'Orientacyjna cena mieszkania za 5 lat to: {npf.fv(rate, nper, pmt, -pv):,.2f} PLN')
# czy robić w ten sposób czy tworzyć jakiej def fv(rate, nper, pmt, pv, when='end')?

rate = 0.12
nper = 60
pv = 0
fv = 153153.79
print(npf.pmt(0.12/12,nper,-fv))