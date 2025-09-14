("Welcome To Manga Reader Recommendations!")

genre = input("What Manga Genre are you Looking For? (action,comedy,romance) : ")

if genre.lower() == "action":
	print("You have Chosen Action")
	duration = input("How Long The Manga should be? (short, medium, long) : ")
	if duration.lower() == "short":
		print("You have chosen Short")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Alive (2003–2004) by Tsutomu Takahashi\n\t-Akumetsu (2002–2006) by Yoshiaki Tabata & Yūki Yugo\n\t-Dogs: Bullets & Carnage(2005–2015) by Shirow Miwa")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-All You Need Is Kill (2014) by Ryōsuke Takeuchi & Takeshi Obata\n\t-Green Blood (2011–2013) by Masasumi Kakizaki\n\t-Wolfsmund (2009–2015, but mainly ran in early 2010s) by Mitsuhisa Kuji")


	elif duration.lower() == "medium":
		print("You have chosen Medium")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Alive: The Final Evolution (2003–2010) by Tsutomu Takahashi\n\t-Battle Royale (2000–2005) by Koushun Takami\n\t-O-Parts Hunter (2001–2007) by Seishi Kishimoto")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-kame ga Kill! (2010–2016) by Takahiro & Tetsuya Tashiro\n\t-Terra Formars (2011–2019, first part) by Yū Sasuga & Kenichi Tachibana\n\t-Gangsta. (2011–2018, on hiatus) by Kohske")


	elif duration.lower() == "long":
		print("You have chosen Long")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Naruto (1999–2014) by Masashi Kishimoto\n\t-Bleach (2001–2016) by Tite Kubo\n\t-One Piece (1997–present) by Eiichiro Oda")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Attack on Titan (Shingeki no Kyojin) (2009–2021) by Hajime Isayama\n\t-My Hero Academia (Boku no Hero Academia) (2014–present) by Kohei Horikoshi\n\t-Tokyo Ghoul + :re (2011–2018) by Sui Ishida")


elif genre.lower() == "comedy":
	print("You have Chosen Comedy")
	duration = input("How Long The Manga should be? (short, medium, long) : ")
	if duration.lower() == "short":
		print("You have chosen Short")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Detroit Metal City (2005–2010) by Kiminori Wakasugi\n\t-School Rumble (2002–2009) by Jin Kobayashi\n\t-romartie High School (2000–2006) by Eiji Nonaka")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-I Am Here! (Koko ni Iru yo!) (2007–2010) by Ema Tōyama\n\t-Ore-sama Teacher (2007–2015) by Izumi Tsubaki\n\t-Ojisan and Marshmallow (2014–2016) by Rekomaru Otoi")


	elif duration.lower() == "medium":
		print("You have chosen Medium")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Great Teacher Onizuka: 14 Days in Shonan (2009–2011) by Tohru Fujisawa\n\t-Bamboo Blade (2004–2010) by Masahiro Totsuka & Aguri Igarashi\n\t-Midori Days (Midori no Hibi) (2002–2004) by Kazurou Inoue")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Monthly Girls’ Nozaki-kun (Gekkan Shoujo Nozaki-kun) (2011–present) by Izumi Tsubaki\n\t-Prison School (Kangoku Gakuen) (2011–2017) by Akira Hiramoto\n\t-Beelzebub (2009–2014) by Ryūhei Tamura")


	elif duration.lower() == "long":
		print("You have chosen Long")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Gintama (2003–2019) by Hideaki Sorachi\n\t-Hayate no Gotoku! (Hayate the Combat Butler) (2004–2017) by Kenjirou Hata\n\t-Ouran High School Host Club (2002–2010) by Bisco Hatori")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Assassination Classroom (Ansatsu Kyoushitsu) (2012–2016) by Yūsei Matsui\n\t-Saiki Kusuo no Psi-nan (The Disastrous Life of Saiki K.) (2012–2018) by Shūichi Asō\n\t-Silver Spoon (Gin no Saji) (2011–2019)")


elif genre.lower() == "romance":
	print("You have Chosen Romance")
	duration = input("How Long The Manga should be? (short, medium, long) : ")
	if duration.lower() == "short":
		print("You have chosen Short")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Midori Days (Midori no Hibi) (2002–2004) by Kazurou Inoue\n\t-LovelyComplex (2001–2006) by Aya Nakahara\n\t-Kare Kano: Side Stories (Kare Kano: Tokubetsu-ban) (2005–2006) by Masami Tsuda")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Orange (2012–2017) by Ichigo Takano\n\t-My Little Monster (Tonari no Kaibutsu-kun) (2008–2013) by Robico\n\t-Ojisan and Marshmallow (2014–2016) by Rekomaru Otoi")


	elif duration.lower() == "medium":
		print("You have chosen Medium")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Faster than a Kiss (2007–2011) by Meca Tanaka\n\t-Dengeki Daisy (2007–2013) by Kyousuke Motomi\n\t-We Were There (Bokura ga Ita) (2002–2012) by Yuki Obata")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Ao Haru Ride (Blue Spring Ride) (2011–2015) by Io Sakisaka\n\t-Say I Love You (Sukitte Ii na yo) (2008–2017) by Kanae Hazuki\n\t-Hirunaka no Ryuusei (Daytime Shooting Star) (2011–2014) by Mika Yamamori")


	elif duration.lower() == "long":
		print("You have chosen Long")
		era = input("From Which Manga Era? (2000, 2010) : ")
		if era == "2000":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Boys Over Flowers (Hana Yori Dango) (1992–2008) by Yoko Kamio\n\t-Fruits Basket (1998–2006) by Natsuki Takaya\n\t-Kimi ni Todoke: From Me to You (2005–2017) by Karuho Shiina")

		elif era == "2010":
			print(genre + "/" + duration + "/" + era) 
			print("Here is the list of available manga\n\t-Kimi ni Todoke: From Me to You (2006–2017) by Karuho Shiina\n\t-GE: Good Ending (2009–2013) by Kei Sasuga\n\t-Domestic Girlfriend (Domestic na Kanojo) (2014–2020) by Kei Sasuga")

else:
	print("404 not found")
