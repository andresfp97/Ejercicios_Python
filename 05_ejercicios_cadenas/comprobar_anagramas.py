# Counter -->  analiza si todos los caracteres de las cadenas conincidan en 
# el numero total de ellos 
from collections import Counter
def is_anagram(s1, s2):
 return Counter(s1) == Counter(s2)
 
print("listen is an anagram of silent -> {}".format(is_anagram("listen", "silent")))