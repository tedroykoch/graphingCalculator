GRAPHING CALCULATOR (written at age 14) 

I originally built this graphing calculator on Trinket.io, which has since shut down. Trinket ran Python a little differently than a standard terminal and had a white background, so I recommend running it in a terminal with a white background (otherwise some of the graph's text won't be visible). 

How to run: 

python3 graphing_calculator.py 

Then type an equation when prompted, for example: 

y = 0.5x^2 - 8 
y = {x} - 3 (curly braces mean absolute value) 
y = 2(x+1) 

Known issues: a few edge cases, like y = x^0.5 or y = x^-1, crash in standard Python because negative roots and dividing by zero behave differently there than they did on Trinket.