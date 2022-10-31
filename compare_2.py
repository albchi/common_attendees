from fuzzywuzzy import fuzz

lfn = []
lln = []
lshow = []


# 1. open and process show.csv -> l[]
filename = 'show.csv'

with open(filename) as f:
   s = f.readline() # burn 1st line
   while True:
      s = f.readline() # burn 1st line
      if not s:
         break # EOF
      sfn = s.split(",")[0]
      lfn.append(sfn)
      sln = s.split(",")[1]
      lln.append(sln)
      lshow.append(sfn+" "+sln)


print(" some stats about " + filename)
print(" fn count is : " + str(len(lfn)) )
print(" ln count is : " + str(len(lln)) )
print(" lshow count is : " + str(len(lshow)) )

# find the index value by looking up the element value in a list
#print(" Cara's index is : " + str(lfn.index('Cara')))

# interate throught the list 
#print("first names are : ")
#for tmp in lfn:
#   print(str(lfn.index(tmp)) + " " + tmp)


# 2. open and process booth.csv -> lbooth

lbooth = []
with open("booth.csv") as f2:
   s2 = f2.readline()
   while True:
      if not s2:
         break #out of while
      s2 = f2.readline()
      s2n = s2.split(',')[0] 
      lbooth.append(s2n)

# debug
#print("the imported booth contact list is:")
#for tmp in lbooth:
#   print(tmp)



# 3. brute force sweep for each in lshow, sweep lbooth 
l_show_booth = []

for tmp_show in lshow:
   if tmp_show in lbooth:
      l_show_booth.append(tmp_show)

print(" Brute force : these people " + str(len(l_show_booth)) + " went to the show and booth")
with open("show_booth.txt", "w") as f:
   for tmp in l_show_booth:
      print(tmp)
      f.write(tmp + ", ")

#break # CANNOT BREAK out of main
# exit() # works!

# 4. let's use fuzzywuzzy

#l_show_booth_fuzzy = [] 
def use_fuzzy(per):
   l_show_booth_fuzzy = [] # ha if declared here, can't see in global
   for tmp_show in lshow:
      for tmp_booth in lbooth:
         if (fuzz.partial_ratio(tmp_show, tmp_booth) > per):
            l_show_booth_fuzzy.append(tmp_show)

   print(" Fuzzy : these people " + str(len(l_show_booth_fuzzy)) + " went to the show and booth, per fuzzy " + str(per))
   for tmp in l_show_booth_fuzzy:
      print(tmp)


#try_table = (50, 75, 90, 95, 100) # set!
try_table = [50, 75, 90, 95, 100]
for tmp in try_table:
   use_fuzzy(tmp)


