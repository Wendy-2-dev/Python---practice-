print("=" * 40)
print("CANDLESTICK CLASSIFIER")
print("=" * 40)
print()

# classifying a candlestick
def candlestick_classifier(open_price,close_price,highest_price,lowest_price, candlestick_color):
    body_top = max(open_price, close_price)
    body_bottom = min(open_price, close_price)
    margin = abs(body_top - body_bottom)
    upper_wick = abs(highest_price - body_top)
    lower_wick = abs(lowest_price - body_bottom)
    
    if margin <= (2*upper_wick) and margin <= (2*lower_wick):
        print("{:<25}""{:>25}". format
        	("long-legged indecision:","show market is indecisive"))
        
    if body_bottom == body_top and lower_wick > 0 and upper_wick == 0:
     print("{:<25}""{:>25}".format("Dragonfly bullish:", "Signal possible market reversal upwards"))
        

    if body_bottom == body_top and upper_wick > 0 and lower_wick == 0:
         print("{:<25}""{:>25}".format("Gravestone bearish:", "Signals possible market reversal downwards"))
        
    if body_bottom == lowest_price and body_top == highest_price and body_bottom == body_top:
        print("{:<25}""{:>25}". format ("four- price doji:","Signals extreme indecision"))
        
    if body_bottom == lowest_price and body_top == highest_price and close_price > open_price:
        print("{:<25}""{:>25}". format ("Bullish Marubozu:","Strong buying conviction, almost no wick."))
        
    elif body_bottom == lowest_price and body_top == highest_price and close_price < open_price:
        print("{:<25}""{:>25}". format ("Bearish Marubozu","Strong selling conviction, almost no wick."))
        
    elif candlestick_color == "red" and lower_wick >= body_bottom:
        print("{:<25}""{:>25}". format ("Bearish candlestick:"," Sellers were in control."))
    
    elif candlestick_color == "blue" and upper_wick > body_top:
        print("{:<25}""{:>25}". format ("Bullish candlestick","Buyers were in control."))
               
# Giving prices tied to a candlestick
while True:
    open_price = float(input("enter opening price:"))
    highest_price = float(input("enter the price of the highest wick:"))
    lowest_price = float(input("enter price of the lowest wick;"))
    close_price = float(input("enter the Lowest price:"))
    candlestick_color = str(input("enter the color:red or blue:"))
    classification = str(input("enter 'yes' or 'done':"))
    if classification == 'done':
        break
    else:
            candlestick_classifier(open_price, close_price, highest_price, lowest_price, candlestick_color)

            	
            





    
    