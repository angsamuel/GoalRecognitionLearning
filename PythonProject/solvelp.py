import os
print " "
os.system("glpsol --cpxlp znoShadow.lp -o znoShadow.out")
print " "
os.system("glpsol --cpxlp zwithShadow.lp -o zwithShadow.out")
print " "
os.system("glpsol --cpxlp zmem.lp -o zmem.out")