import customtkinter as ctk
import requests

def program():
	try:
		window = ctk.CTk()
		window.title("Ekopro")
		window.minsize(500,600)
		window.geometry("500x600+500+40")
		window.maxsize(500,600)


		#Tema ayarları
		def tema_degistir():
			if tema_ayarla_var.get() == 0:
				ctk.set_appearance_mode("light")
				kur.configure(text_color="#0033FF")
				sonuc.configure(text_color="#0033FF")
			elif tema_ayarla_var.get() == 1:
				ctk.set_appearance_mode("dark")
				kur.configure(text_color="cyan")
				sonuc.configure(text_color="cyan")
		tema_ayarla_var = ctk.IntVar(value=0)
		tema_ayarla = ctk.CTkSwitch(
			window,
			text="Koyu Tema",
			onvalue=1,
			offvalue=0,
			variable=tema_ayarla_var,
			command=tema_degistir
			).place(x=1,y=1)

		def sec_def(chuice):
			global durum
			if chuice == "Dolar":
				kur.configure(text=f"1 Dolar {dolar} değerinde")
				durum = 1
			elif chuice == "Euro":
				kur.configure(text=f"1 Euro {euro} değerinde")
				durum = 2
			elif chuice == "Sterlin":
				kur.configure(text=f"1 Sterlin {sterlin} değerinde")
				durum = 3
			elif chuice == "Ruble":
				kur.configure(text=f"1 Ruble {ruble} değerinde")
				durum = 4

		sec = ctk.CTkComboBox(
			window,
			values=("Dolar","Euro","Sterlin","Ruble"),
			command=sec_def
			)
		sec.set("Seç")
		sec.pack(pady=8)

		#Dolar
		url = "https://api.exchangerate-api.com/v4/latest/USD"
		response = requests.get(url)
		data = response.json()
		dolar = data['rates']['TRY']

		#Euro
		url2 = "https://api.exchangerate-api.com/v4/latest/EUR"
		response2 = requests.get(url2)
		data2 = response2.json()
		euro = data2['rates']['TRY']

		#Sterlin
		url3 = "https://api.exchangerate-api.com/v4/latest/GBP"
		response3 = requests.get(url3)
		data3 = response3.json()
		sterlin = data3['rates']['TRY']

		#Ruble
		url4 = "https://api.exchangerate-api.com/v4/latest/RUB"
		response4 = requests.get(url4)
		data4 = response4.json()
		ruble = data4['rates']['TRY']



		kur = ctk.CTkLabel(
			window,
			text=f"Lütfen bir para birimi seçin",
			font=("italic",30),
			text_color = "#0033FF"
			)
		kur.pack(pady=50)

		kur_girdi = ctk.CTkEntry(
			window,
			placeholder_text = "Değer girin"
			)
		kur_girdi.pack(pady=40)

		def kur_buton_def():
			if durum == 1:
				kur1 = float(kur_girdi.get())
				sonuc.configure(text=f"{kur1} Dolar {round(dolar * kur1,2)} TL değerinde")

			elif durum == 2:
				kur2 = float(kur_girdi.get())
				sonuc.configure(text=f"{kur2} Euro {round(euro * kur2,2)} TL değerinde")

			elif durum == 3:
				kur3 = float(kur_girdi.get())
				sonuc.configure(text=f"{kur3} Sterlin {round(sterlin * kur3,2)} TL değerinde")

			elif durum == 4:
				kur4 = float(kur_girdi.get())
				sonuc.configure(text=f"{kur4} Ruble {round(ruble * kur4,2)} TL değerinde")

		kur_buton = ctk.CTkButton(
			window,
			text="Araştır",
			command=kur_buton_def
			).pack()

		sonuc = ctk.CTkLabel(
			window,
			text="",
			font=("italic",25),
			text_color="#0033FF"
			)
		sonuc.pack(pady=50)

		imza = ctk.CTkLabel(
			window,
			text="V1.1 | Yiğit Çıtak Inc. 2024©Tüm haklar saklıdır"
			).pack(pady=30)

		window.mainloop()
	except:
		uyari = ctk.CTk()
		uyari.title("Ekopro Hata: Veri bağlanıtsı erişilemedi")
		uyari.minsize(500,600)
		uyari.geometry("500x600+500+40")
		uyari.maxsize(500,600)
		uyari.iconbitmap("icon.ico")

		uyr = ctk.CTkLabel(
			uyari,
			text="İnternet bağlantınızı kontol edin\n\n\n\nError 020 :(",
			font=("italic",20)
			).pack()
		uyari.mainloop()



if __name__ == "__main__":
	program()