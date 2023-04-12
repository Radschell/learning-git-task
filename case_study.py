
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

import numpy as np
import matplotlib.pyplot as plt

# Set up variables for deposit calculation
PMT = 1736
r = 0.12
n = 12
t = 5

# Calculate deposit values over time
months = np.arange(0, 61, 1)
deposit_values = np.zeros(len(months))
deposit_values[0] = 120

for i in range(1, len(months)):
    deposit_values[i] = deposit_values[i-1] * (1 + r/n) + PMT

# Calculate apartment value over time
apartment_value = 120000 * (1.05)**(months/12)


plt.plot(months, deposit_values/1000, label='Deposit Value')
plt.plot(months, apartment_value/1000, label='Apartment Value')

plt.xlabel('Months')
plt.ylabel('Value (in thousands of PLN)')
plt.title('Deposit and Apartment Values Over Time')
plt.legend()

# Show the plot
plt.show()