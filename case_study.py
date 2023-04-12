
#wpierw liczymy ile wyniesie koszt mieszkania za 5 lat

import numpy as np

price = 120000
rate = 0.05
years = 5

future_price = price * (1 + rate) ** years

print("The apartment will cost", round(future_price, 2), "PLN in 5 years.")


import numpy as np

PV = 153862.4
r = 0.12
n = 12
t = 5

PMT = PV * (r / n) * (1 + r / n) ** (n*t) / ((1 + r / n) ** (n*t) - 1)
print("You need to put", round(PMT, 2), "PLN into the deposit each month to be able to afford the apartment in 5 years.")
