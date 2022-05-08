#DOSYA İSLEMLERİ
#r=okuma
#w=yazma
#a=ekleme yapma
#r+ =hem okuma hem yazma 

ths=open("tahsilat_dosyasi.txt","w")
ths.write("Otuken Pazarlama: 150.000tl \nTuran Nakliyat: 200.000tl \nBozkurt Muhasebe:30.000tl")
ths.close() #kapatmayı unutma diskte yer kaplamasın
#w kipini kullanırken dikkat et. örnegin bu dosyayı w kipi ile açıp içine bir şeyler yazdıktan sonra tekrar w kipi ile açmaya çalışırsan önceki dosyayı sorgusuz sualsiz silip yerine yeni bir dosya açacaktır. bu yüzden w kipini mutlaka dikkatli kullannn!

with open("tahsilat_dosyasi.txt") as ths: #bizim kapatmamıza gerek kalmadan dosyayı kendisi kapatacak
    print(ths.read()) #hepsini gösteriyor
    print(ths.readline()) #satır satır gösteriyor
    print(ths.readlines())# liste halinde okuyor yani bilgileri aralarına virgül koyarak gösteriyor

    ths.seek(0) #tekrar okurken seek ile en başa dönüyor (0.bayta)

# w metodu ile yalnızca karakter dizileri yazılabilir, liste tipinde veri yazılamaz
# writelines metodu liste tipinde veri yazma imkanı verir
# insert ile ortalarda bir yerlerde veri ekleme yapabilmemizi saglar