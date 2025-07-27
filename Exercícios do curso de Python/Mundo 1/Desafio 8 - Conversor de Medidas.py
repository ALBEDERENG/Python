n = float(input("Uma distância em metros: "))
print ("A medida de {}m corresponde a".format(n))
nkm = n / 1000
nhm = n / 100
ndam = n / 10
ndm = int(n*10)
ncm = int(n*100)
nmm = int(n*1000)
print ("{}km".format(nkm))
print ("{}hm".format(nhm))
print ("{}dam".format(ndam))
print ("{}cm".format(ncm))
print ("{}mm".format(nmm))
