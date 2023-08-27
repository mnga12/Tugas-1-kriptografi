
#Kelompok 1 Kriptografi MA4151

#Jihan Navitri

#Sulthan Bimo Rizqullah

#Ibrahim Naufal Mangaraja

#library yang dipakai
from collections import Counter
import re
import numpy as np

# mengimport dokumen
with open("Docs letter counter.txt") as f:
    for line in f:
        line = line.lower() # mengubah huruf kapital menjadi huruf kecil

    line = re.sub("[^A-Za-z]","",line) # menghapus karakter selain alfabet
    c = Counter()
    # iterasi menghitung frekuensi tiap huruf
    for line in line:
        c += Counter(line)

#mengubah dictionary menjadi array 2x26
new_lis = list(c.items())
con_arr = np.array(new_lis)

# menghitung persentase munculnya tiap huruf
sum = 0
for i in range(26):
    sum += (int(con_arr[i][1])) # menghitung banyak semua huruf
for i in range(26):
    print(str(con_arr[i][0]) +': '+ str(int(con_arr[i][1])/sum*100))
