import random
import pandas as pd
import os

############# CHANGE THESE #############

# paste path for spreadsheet here (right-click on file, hit "option" and then select "copy 'file' as pathname")
df = pd.DataFrame("") 

# type the name of the spreadsheet column that contains winners in the quotation marks below
colwinners = "" 

# type the number of winners here
numwinners = 3 

# can change the file name where your winner info is saved
file = 'winners.txt'


############# DONT CHANGE THESE ###############

winners = df.sample(n = numwinners) 
lines = winners[[colwinners]]
loc = os.path.join(os.getcwd(), file)

with open(loc,'w') as outfile:
    lines.to_string(outfile)

## WHERE TO FIND THE FILE WITH WINNER ADDRESSES
print(loc)