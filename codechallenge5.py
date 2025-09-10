print("Welcome To Manga Reader Recommendations!")

genre = input("What Manga Genre are you Looking For? (action, comedy, romance, horror) : ").lower()
duration = input("How Long The Manga should be? (short, medium, long) : ").lower()
era = input("From Which Manga Era? (2000, 2010) : ")

if genre == "action" and duration == "short" and era == "2000":
    print("Action/Short/2000")
    print("Here is the list of available manga\n\t- Alive (2003–2004) by Tsutomu Takahashi\n\t- Akumetsu (2002–2006) by Yoshiaki Tabata\n\t- Dogs: Bullets & Carnage (2005–2015) by Shirow Miwa")

elif genre == "action" and duration == "medium" and era == "2000":
    print("Action/Medium/2000")
    print("Here is the list of available manga\n\t- Black Cat (2000–2004) by Kentaro Yabuki\n\t- Tenjho Tenge (1997–2010) by Oh! great\n\t- Samurai Deeper Kyo (1999–2006) by Akimine Kamijyo")

elif genre == "action" and duration == "long" and era == "2000":
    print("Action/Long/2000")
    print("Here is the list of available manga\n\t- Naruto (1999–2014) by Masashi Kishimoto\n\t- Bleach (2001–2016) by Tite Kubo\n\t- One Piece (1997–present) by Eiichiro Oda")


elif genre == "action" and duration == "short" and era == "2010":
    print("Action/Short/2010")
    print("Here is the list of available manga\n\t- All You Need Is Kill (2014) by Ryōsuke Takeuchi & Takeshi Obata\n\t- Green Blood (2011–2013) by Masasumi Kakizaki\n\t- Wolfsmund (2009–2015) by Mitsuhisa Kuji")

elif genre == "action" and duration == "medium" and era == "2010":
    print("Action/Medium/2010")
    print("Here is the list of available manga\n\t- Attack on Titan (2009–2021) by Hajime Isayama\n\t- Blue Exorcist (2009–present) by Kazue Kato\n\t- Deadman Wonderland (2007–2013) by Jinsei Kataoka & Kazuma Kondou")

elif genre == "action" and duration == "long" and era == "2010":
    print("Action/Long/2010")
    print("Here is the list of available manga\n\t- My Hero Academia (2014–present) by Kohei Horikoshi\n\t- Black Clover (2015–present) by Yūki Tabata\n\t- Seven Deadly Sins (2012–2020) by Nakaba Suzuki")


elif genre == "comedy" and duration == "short" and era == "2000":
    print("Comedy/Short/2000")
    print("Here is the list of available manga\n\t- Cromartie High School (2000–2006) by Eiji Nonaka\n\t- Bobobo-bo Bo-bobo (2001–2007) by Yoshio Sawai\n\t- Sexy Commando Gaiden (1995–2002) by Kyosuke Usuta")

elif genre == "comedy" and duration == "medium" and era == "2000":
    print("Comedy/Medium/2000")
    print("Here is the list of available manga\n\t- Genshiken (2002–2006) by Shimoku Kio\n\t- School Rumble (2002–2009) by Jin Kobayashi\n\t- Hayate no Gotoku! (2004–2017) by Kenjirou Hata")

elif genre == "comedy" and duration == "long" and era == "2000":
    print("Comedy/Long/2000")
    print("Here is the list of available manga\n\t- Gintama (2003–2019) by Hideaki Sorachi\n\t- Great Teacher Onizuka (1997–2002) by Tooru Fujisawa\n\t- Detroit Metal City (2005–2010) by Kiminori Wakasugi")


elif genre == "comedy" and duration == "short" and era == "2010":
    print("Comedy/Short/2010")
    print("Here is the list of available manga\n\t- I Can't Understand What My Husband Is Saying (2011–2014) by Cool-kyou Shinja\n\t- Please Go Home, Akutsu-san! (2017–2021) by Taichi Nagaoka\n\t- Ojisan and Marshmallow (2014–2015) by Rekomaru Otoi")

elif genre == "comedy" and duration == "medium" and era == "2010":
    print("Comedy/Medium/2010")
    print("Here is the list of available manga\n\t- Monthly Girls’ Nozaki-kun (2011–present) by Izumi Tsubaki\n\t- Prison School (2011–2017) by Akira Hiramoto\n\t- Beelzebub (2009–2014) by Ryūhei Tamura")

elif genre == "comedy" and duration == "long" and era == "2010":
    print("Comedy/Long/2010")
    print("Here is the list of available manga\n\t- The Disastrous Life of Saiki K. (2012–2018) by Shūichi Asō\n\t- Assassination Classroom (2012–2016) by Yūsei Matsui\n\t- Sket Dance (2007–2013) by Kenta Shinohara")


elif genre == "romance" and duration == "short" and era == "2000":
    print("Romance/Short/2000")
    print("Here is the list of available manga\n\t- Saikano (2000–2001) by Shin Takahashi\n\t- Bokura ga Ita (2002–2012) by Yuki Obata\n\t- Aqua (2001–2002) by Kozue Amano")

elif genre == "romance" and duration == "medium" and era == "2000":
    print("Romance/Medium/2000")
    print("Here is the list of available manga\n\t- Lovely★Complex (2001–2006) by Aya Nakahara\n\t- Peach Girl (1997–2003) by Miwa Ueda\n\t- Boys Be… (2000–2007) by Masahiro Itabashi & Hiroyuki Tamakoshi")

elif genre == "romance" and duration == "long" and era == "2000":
    print("Romance/Long/2000")
    print("Here is the list of available manga\n\t- Fruits Basket (1998–2006) by Natsuki Takaya\n\t- Hana yori Dango (1992–2004) by Yoko Kamio\n\t- Hot Gimmick (2000–2005) by Miki Aihara")

# --- 2010s ---
elif genre == "romance" and duration == "short" and era == "2010":
    print("Romance/Short/2010")
    print("Here is the list of available manga\n\t- Horimiya (2011–2021) by HERO & Daisuke Hagiwara\n\t- ReLIFE (2013–2018) by Yayoiso\n\t- Ojousama no Untenshu (2009–2011) by Keiko Ishihara")

elif genre == "romance" and duration == "medium" and era == "2010":
    print("Romance/Medium/2010")
    print("Here is the list of available manga\n\t- Ao Haru Ride (2011–2015) by Io Sakisaka\n\t- Strobe Edge (2007–2010) by Io Sakisaka\n\t- Tonari no Kaibutsu-kun (2008–2013) by Robico")

elif genre == "romance" and duration == "long" and era == "2010":
    print("Romance/Long/2010")
    print("Here is the list of available manga\n\t- Kimi ni Todoke (2006–2017) by Karuho Shiina\n\t- GE: Good Ending (2009–2013) by Kei Sasuga\n\t- Domestic Girlfriend (2014–2020) by Kei Sasuga")


elif genre == "horror" and duration == "short" and era == "2000":
    print("Horror/Short/2000")
    print("Here is the list of available manga\n\t- Uzumaki (1998–1999, popular in 2000s) by Junji Ito\n\t- The Enigma of Amigara Fault (2002) by Junji Ito\n\t- Goth (2000–2001) by Otsuichi & Kendi Oiwa")

elif genre == "horror" and duration == "medium" and era == "2000":
    print("Horror/Medium/2000")
    print("Here is the list of available manga\n\t- MPD Psycho (1997–2014) by Eiji Otsuka & Shou Tajima\n\t- Hellsing (1997–2008) by Kouta Hirano\n\t- Homunculus (2003–2011) by Hideo Yamamoto")

elif genre == "horror" and duration == "long" and era == "2000":
    print("Horror/Long/2000")
    print("Here is the list of available manga\n\t- Gantz (2000–2013) by Hiroya Oku\n\t- Bastard!! (1988–2010) by Kazushi Hagiwara\n\t- Blade of the Immortal (1993–2012) by Hiroaki Samura")


elif genre == "horror" and duration == "short" and era == "2010":
    print("Horror/Short/2010")
    print("Here is the list of available manga\n\t- Franken Fran (2006–2012) by Katsuhisa Kigitsu\n\t- Magical Girl Apocalypse (2012–2017) by Kentaro Sato\n\t- Ajin: Demi-Human (2012–2021) by Gamon Sakurai")

elif genre == "horror" and duration == "medium" and era == "2010":
    print("Horror/Medium/2010")
    print("Here is the list of available manga\n\t- I Am a Hero (2009–2017) by Kengo Hanazawa\n\t- Another (2010–2012) by Yukito Ayatsuji & Hiro Kiyohara\n\t- High-Rise Invasion (2013–2019) by Tsuina Miura & Takahiro Oba")

elif genre == "horror" and duration == "long" and era == "2010":
    print("Horror/Long/2010")
    print("Here is the list of available manga\n\t- Tokyo Ghoul (2011–2014) & Tokyo Ghoul:re (2014–2018) by Sui Ishida\n\t- Devilman Grimoire (2011–2013) by Go Nagai & Rui Takato\n\t- Terra Formars (2011–2019) by Yu Sasuga & Kenichi Tachibana")

else:
    print("404 not found.")
