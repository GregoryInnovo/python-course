
def convert(current_type, usd_value):
    user_pesos = float(input("How much " + current_type + " you have? "))
    result_usd = user_pesos / usd_value
    result_usd = round(result_usd, 2)
    result_usd = str(result_usd)
    print("You have $" +result_usd + " usd!")

menu = """
Welcome to convert currency 💲

1 - COP
2 - ARG
3 - MEX

Choose an option: """

option = int(input(menu))

if option == 1:
    convert("COP", 4032.67)
elif option == 2:
    convert("ARG", 65)
elif option == 3:
    convert("MEX", 24)
else:
    print("Please select an exist option ")



# user_usd = float(input("How much USD you have? "))

# result_cop = user_usd * usd_value
# result_cop = round(result_cop, 2)
# result_cop = str(result_cop)
# print("You have $" +result_cop + " cop!")
