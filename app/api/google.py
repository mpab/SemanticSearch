
from googlesearch import search 

# to search 
query = "semantic distance"
  
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 

