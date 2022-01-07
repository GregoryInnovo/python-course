user_cop = float(input("How much COP you have? "))
usd_value = 4032.67

result_usd = user_cop / usd_value
result_usd = round(result_usd, 2)
result_usd = str(result_usd)
print("You have $" +result_usd + " usd!")

user_usd = float(input("How much USD you have? "))

result_cop = user_usd * usd_value
result_cop = round(result_cop, 2)
result_cop = str(result_cop)
print("You have $" +result_cop + " cop!")