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

        # ---- AUTO PIPS ----
        if entry >= 100:
            pip_size = 0.1
            pair_type = "GOLD / INDICES"
        elif entry >= 10:
            pip_size = 0.01
            pair_type = "JPY PAIR"
        else:
            pip_size = 0.00010
            pair_type = "FOREX MAJOR"
        
        print(f"auto pip size detected: {pip_size} for {pair_type}")

        contract = int(input("enter units:"))
        leverage = float(input("enter your leverage as number eg 200 for 1:200:"))

        dollar_risk = capital * risk_percent
        stoploss_distance = abs((entry-stop_loss))/pip_size

        if stoploss_distance == 0:
            print("stoploss_distance is 0, check your entry and stop_loss")
            continue

        pip_value = round(dollar_risk/ stoploss_distance,2)
        lot_size = round(dollar_risk/ (stoploss_distance * contract * pip_size),2)

        # ---- MARGIN CHECK ----
        lot_value = lot_size * contract * entry
        margin_needed = lot_value / leverage
        free_margin = capital - margin_needed
        margin_percent = (margin_needed / capital) * 100 if capital != 0 else 0

        total_trade += 1
        print("-------TRADE TICKETS-----------")
        print(f"{'Capital:':<15}{capital:>10.2f}")
        print(f"{'Risk %:':<15}{risk_percent:>10.2f}")
        print(f"{'stoploss_pips:':<15}{stoploss_distance:>10.2f}")
        print(f"{'Dollar risk:':<15}{dollar_risk:>10.2f}")
        print(f"{'pip size auto:':<15}{pip_size:>10.5f}")
        print(f"{'pip value:':<15}{pip_value:>10.2f}")
        print(f"{'Lot size:':<15}{lot_size:>10.2f}")
        print(f"{'Lot value:':<15}{lot_value:>10.2f}")
        print(f"{'Margin needed:':<15}{margin_needed:>10.2f}")
        print(f"{'Free margin:':<15}{free_margin:>10.2f}")
        print(f"{'Margin %:':<15}{margin_percent:>9.2f}%")

        if margin_needed > capital:
            print("WARNING: margin_needed is more than your capital, trade will fail")
        elif margin_percent > 70:
            print("WARNING: margin is using more than 70% of your account, too risky")
        
        if stoploss_distance < 5:
            print("WARNING: stoploss_distance is less than 5 pips, too tight")

        if lot_size > 50:
            print("WARNING: lot_size is very big, check your stoploss")