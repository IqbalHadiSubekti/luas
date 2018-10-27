class Segitiga():
	def __init__(self,setengah,alas,tinggi):
		self.setengah = setengah
		self.alas = alas
		self.tinggi = tinggi

luas = Segitiga(1/2,40,80)
print(luas.setengah*luas.alas*luas.tinggi)