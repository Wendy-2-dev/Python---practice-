#Trade journal with winning rate summary for forex market 
win = 0
loss = 0
total_trades = 0
win_rate = 0
total_win_pips = 0
total_loss_pips = 0
average_won_pips = 0
average_lost_pips = 0
net_pips = 0

while True:
    journaling = str(input("are you journaling? yes or done?:"))
    if journaling != "yes":
        break
        
    trade_pair = str(input("enter your trade pair:"))
    result = str(input("did you won or loss:"))
    if result == "win":
        pip_won = float(input("enter no. of pips won:"))
        win += 1
        total_win_pips +=pip_won
    elif result == "loss":
        pip_lost = float(input("enter the no. of pips lost:"))
        loss += 1
        total_loss_pips +=pip_lost
          
    total_trades += 1
    
net_pips = total_win_pips - total_loss_pips


win_rate = round((win/total_trades) * 100,2) if total_trades > 0 else 0


# use conditional expression where necessary 
average_won_pips = total_win_pips/win if win > 0 else 0
average_lost_pips = total_loss_pips/loss if loss > 0 else 0
    
print ("\n")   
print("-----WINNING SUMMARY-----ENTRIES----")
print(f"{'Total No. of trades:':<24}{total_trades:>05.2f}")
print(f"{'Win rate in percent:':<24}{win_rate:05.2f}%")
print(f"{'Average pips won:':<24}{average_won_pips:05.2f}")
print(f"{'Average pips lost:':<24}{average_lost_pips:05.2f}")
print(f"{'Net pips for the trades:':<24}{net_pips:05.2f}")
