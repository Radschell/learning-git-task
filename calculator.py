import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

program_start = input("Wybierz rodzaj dzialania podajac liczbe 1,2,3, lub 4; 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie")

num1 = float(input("Podaj pierwsza liczbe:"))
num2 = float(input("Podaj druga liczbe:"))

if program_start == "1":
   zapytanie = input("czy chcesz dodac jeszcze jedna liczbe? (T/N)")
   if zapytanie == "N":
          result = num1 + num2
          logging.info(f"Dodaje {num1} oraz {num2}")
   else:
          num3 = float(input("Podaj trzecia liczbe:"))
          logging.info(f"Dodaje {num1} oraz {num2} oraz {num3}")
          result = num1 + num2 + num3
elif program_start == "2":
  logging.info(f"Odejmuje {num2} od {num1}")
  result = num1 - num2
elif program_start == "3":
  logging.info(f"Dziele {num1} przez {num2}")
  result = num1/num2
elif program_start == "4":
  logging.info(f"Mnoze {num1} razy {num2}")
  result = num1*num2
else:
  print("nieprawidlowa wartosc")

print(f"Twoj wynik to {result}")

#pytania: jak sprawic aby pokazywal sie komunikat o ineprawidlowej wartosci
#jak sprawic abym mogl dodawac wiecej niz jedna liczbe dodatkowo bez spaghetti code