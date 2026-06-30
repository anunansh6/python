#सेट क्या होता है?

# एक ऐसे थैले की कल्पना कीजिए जिसमें आप सामान डालते हैं, लेकिन अगर आप उसमें कुछ ऐसा डालने की कोशिश करते हैं जो पहले से ही उसमें मौजूद है,
# इसे पूरी तरह से अनदेखा कर दिया जाता है। साथ ही, आइटम किसी विशेष क्रम में नहीं रहते हैं। यह एक पायथन सेट है।

# अव्यवस्थित: इनमें कोई इंडेक्स मान नहीं होते और ये स्लाइसिंग का समर्थन नहीं करते।
# परिवर्तनीय: सेट बन जाने के बाद आप उसमें तत्व जोड़ या हटा सकते हैं।
# अद्वितीय तत्व: एक सेट में प्रत्येक तत्व अद्वितीय होना चाहिए। डुप्लिकेट तत्व स्वतः ही हटा दिए जाते हैं।
# विषम: सेट में विभिन्न डेटा प्रकारों के तत्व हो सकते हैं, लेकिन सभी तत्व हैश करने योग्य होने चाहिए।
# (उदाहरण के लिए, संख्याएँ, स्ट्रिंग, टपल, लेकिन सूचियाँ या शब्दकोश नहीं)।

# # empty set
# x = set()
# print(f"x: type: {type(x)}")

# set from a list 
# x = [1, 2, 3, 2, 4, 1, 5]
# x = set(x)
# print(f"Set from list (duplicates removed): {my_set}") 

# X = set((1, 3, 4, 5, 1, 4))
# print(X)

# curly braces
# X = {"apple", "banana", "patao", "anil", 1, 3, 4, 5, 1}
# print(f"fruits: {X}") 
# x = {"x", "t", "a", "A", "X", "T"}
# print(x)

# mixed data types 
# X = {1, "hello", (1, 2), 3.14, (1, 2)} 
# print(x)

# x = {1, 2, 3}
# print(x)

# x.add(4)
# print(x)

# x.add(2) 
# print(2: {x}") 

# x.update([1, 2, 3, 4, 5, 6])
# print(f"{x}") 

# x.update("abcdefg") 
# print(f"{x}") 

# x.update({7, 8}) 
# print(f"x({7, 8}))


# x = {10, 20, 30, 40, 50}
# print(f"Original set: {x}")

# x.remove(30)
# print(f"{x}")

# x.discard(50)
# print(f"(20): {x}") 

# pop 

# a = x.pop()
# print(x)
# print(a)

# X = x.pop()
# print(f"a:x: {x}")

# x.clear()
# print(f"x: {x}") 

# a = {1, 2, 3}
# b = a.copy()
# b.add(23)
# print(a)
# print(b)

# x= {10, 20, 30, 40, 50}

# # Membership
# print(f"Is 3 in my_set? {3 in my_set}")    
# print(f"Is 6 not in my_set? {6 not in my_set}") 

x = {1, 2, 3, 4}
y= {3, 4, 5, 6}

# # Union
# a = a | b
# print(f" (set_a | set_b): {union_set}")
# print(f" (set_a.union(set_b)): {set_a.union(set_b)}")

# Intersection:
# x = set_b & set_a
# print(f" (set_a & set_b): {x}") 
# print(f" (set_a.intersection(set_b)): {set_a.intersection(set_b)}")

# Difference 
# difference_ab = set_a - set_b
# print(f"Difference (set_a - set_b): {difference_ab}") 
# print(f"Difference (set_a.difference(set_b)): {set_a.difference(set_b)}")

# Difference 
# difference_ba = set_b - set_a
# print(f"Difference (set_b - set_a): {difference_ba}") 

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = {4, 5, 6}

# Is set1 a subset of set2?
# print(f"Is {a} subset of {b}? {set1.issubset(set2)}") 
# print(f"Is {a} <= {b}? {set1 <= set2}") 

# Is set2 a superset of set1?
# print(f"Is {set2} superset of {set1}? {set2.issuperset(set1)}") 
# print(f"Is {set2} >= {set1}? {set2 >= set1}") 

# Are set1 and set3 disjoint? 
# print(f"Are {set1} and {set3} disjoint? {set1.isdisjoint(set3)}") 

# # Are set1 and set2 disjoint?
# print(f"Are {set1} and {set2} disjoint? {set1.isdisjoint(set2)}") 


# Create a frozenset
# In frozenset You Can not add, update, remove, pop, discard

# x = frozenset([1, 2, 3])
# y = frozenset([1, 2, 3])
# print(x)
