import re
from kmp import KMPSearch

print("\n")
print("\n")

root_file=input("Nama Dokumen Pertama :")
print("\n")
plagiarised_file=input("Nama Dokumen Kedua :")
  
Text = open(root_file,"r")
text = Text.read()

print("\n")

pattern_file = open(plagiarised_file,"r").read()
sentences = re.split(r'[\.\?!\r\n]', pattern_file)
counter_matched = 0
counter_total = 0
p=0

for pattern in sentences:
  pattern = pattern.strip()

  if len(pattern) > 0:
    counter_total +=1
    counter_matched += KMPSearch(pattern, text,p)
          
print ("Match percentage = %s%%" % (counter_matched*100/counter_total))
print("\n")

if(counter_matched*100/counter_total) >= 70 :
  print ("Dari Input dokumen awal terplagiat. %s%% Dari perbandingan Dua Dokumen %s." % ((counter_matched*100/counter_total), root_file))  
    
print("\n")
print("\n")
