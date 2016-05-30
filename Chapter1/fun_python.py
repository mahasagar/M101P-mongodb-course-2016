fruit = ['a','b','g','k','g','a']

def analyze_list(l):
   print l
   counts = {}
   for item in l:
      if item in counts: 
         counts[item] = counts[item] + 1
      else:
         counts[item] = 1
   return counts

counts = analyze_list(fruit)
print counts
