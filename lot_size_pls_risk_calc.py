print("=" * 40)
print("LOT SIZE CALCULATOR")
print("=" * 40)
total_trade = 0
while True:
    take_trade = str(input("enter yes/no:"))
    if take_trade == "yes":
        capital = float(input("enter your account balance:"))
        risk_percent = float(input("enter the percentage of capital you are risking as a decimal:"))
        entry = float(input("enter your buying/selling price:"))
        stop_loss = float(input("enter your stopping sprice incase trade goes against you:"))
        pip_size = float(input("enter your pip size:"))
        contract = int(input("enter units:"))

        dollar_risk = capital * risk_percent

        stoploss_distance= abs((entry-stop_loss))/pip_size

        pip_value = round(dollar_risk/stoploss_distance,2)
    
        lot_size = round(dollar_risk/(stoploss_distance * contract * pip_size),2)
        total_trade += 1
        print("-------TRADE TICKETS-----------")
        print(f"{'Capital:':<15}{capital:>10.2f}")
        print(f"{'Risk %:':<15}{risk_percent:>10.2f}")
        print(f"{'stoploss_pips:':<15}{stoploss_distance:>10.2f}")
        print(f"{'Dollar risk:':<15}{dollar_risk:>10.2f}")
        print(f"{'pip value:':<15}{pip_value:> 10.2f}")
        print(f"{'Lot size:':<15}{lot_size:> 10.2f}")
    else:
        break

print(f"{'Total trade:':<15}{total_trade:10.2f}")

