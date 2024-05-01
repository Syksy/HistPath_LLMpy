pre = [
    # Prompt 0
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Vastaa esitettyihin kysymyksiin. Anna vastaukset JSON-formaatissa. Anna vastauksissa avaimena merkkien ( ) välissä oleva sisältö kysymyskohtaisesti.\n\"",
    # Prompt 1
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Tehtäväsi on toimia lääketieteellisenä assistenttina ja etsiä lausunnosta alla listatut tiedot. Käy kysymykset läpi askel kerrallaan. Anna vastaukset JSON-formaatissa. \"",
    # Prompt 2
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Tehtäväsi on etsiä tietoa annetusta lausunnosta. Etsi vastaukset alla oleviin kysymyksiin. Anna vastaukset () merkkien välissä olevien ohjeiden mukaan. Anna vastaukset JSON-formaatissa.\"",
    # Prompt 3
    "You will be provided with a histopathological prostate cancer sample statement delimited by quotes (symbols \"\"). The text is a medical note written by a pathologist and it is in Finnish. Your job is to extract information from the given text. Find the answers to the questions below. Give the answers based on the instructions given between the parenthesis. Give the answers in JSON-format. \"",
    # Prompt 4 bare
    "Olet lääketieteellinen assistentti, jonka tehtävänä on muuttaa vapaamuotoisena tekstinä olevia histopatologisia lausuntoja rakenteelliseen muotoon. Kaikkia kysyttyjä kohtia ei välttämättä löydy lausunnosta, jolloin kuuluu palauttaa puuttuvaa arvoa kuvaava NA.  Palauta rakenteelliseksi tulkittu lausunto JSON-formaatissa. Hae seuraaviin kysymyksiin vastaus: \n- Kuinka monta näytettä potilaalta on otettu \n- Näytteiden koko tai paino \n- Näytteen Gleason luokitus \n- Onko kyseessä vain hyvänlaatuinen eturauhasen liikakasvu \n- Onko näytteessä havaittu perineuraalista eli neuronien ympäröivää pahanlaatuista kasvua \n- Onko näytteessä havaittu atypiaa eli tavallisesta kudoksesta poikkeavia muutoksia \nRakenteelliseksi muutettava lausunto seuraa alla ""-merkkien sisällä:\n\"",
    # Prompt 4 variant 1 (5)
    "Olet lääketieteellinen assistentti, jonka tehtävänä on muuttaa vapaamuotoisena tekstinä olevia histopatologisia lausuntoja rakenteelliseen muotoon. Lausuntoja on kolmea päätyyppiä: (1) Biopsianäytteitä, joissa neuloilla on otettu useita ohuita näytteitä eturauhasesta mahdollisen syövän löytämiseksi; (2) Radikaaliprostatektomianäytteitä, joissa koko eturauhanen on poistettu olemassaolevan syövän hoitamiseksi ja koko elin on tutkittavana; (3) Niin sanottuja höyläyslastuja eturauhasen TURP-hoidosta, jossa ylikasvaneesta eturauhasesta on poistettu ylimääräistä osaa ja halutaan varmistua että kyseessä ei ole ollut syöpäkasvua. Kaikkia kysyttyjä kohtia ei välttämättä löydy lausunnosta, jolloin kuuluu palauttaa puuttuvaa arvoa kuvaava NA.  Palauta rakenteelliseksi tulkittu lausunto JSON-formaatissa. Hae seuraaviin kysymyksiin vastaus: \n- Kuinka monta näytettä potilaalta on otettu \n- Näytteiden koko tai paino \n- Näytteen Gleason luokitus \n- Onko kyseessä vain hyvänlaatuinen eturauhasen liikakasvu \n- Onko näytteessä havaittu perineuraalista eli neuronien ympäröivää pahanlaatuista kasvua \n- Onko näytteessä havaittu atypiaa eli tavallisesta kudoksesta poikkeavia muutoksia \nRakenteelliseksi muutettava lausunto seuraa alla ""-merkkien sisällä:\n\"",
    # Prompt 4 variant 2 (6)
    "Olet erittäin kokenut histopatologiaan erikoistunut erikoislääkäri, jonka tehtävänä on muuttaa ammattitaitoisesti vapaamuotoisena tekstinä olevia histopatologisia lausuntoja rakenteelliseen muotoon. Kaikkia kysyttyjä kohtia ei välttämättä löydy lausunnosta, jolloin kuuluu palauttaa puuttuvaa arvoa kuvaava NA.  Palauta rakenteelliseksi tulkittu lausunto JSON-formaatissa. Hae seuraaviin kysymyksiin vastaus: \n- Kuinka monta näytettä potilaalta on otettu \n- Näytteiden koko tai paino \n- Näytteen Gleason luokitus \n- Onko kyseessä vain hyvänlaatuinen eturauhasen liikakasvu \n- Onko näytteessä havaittu perineuraalista eli neuronien ympäröivää pahanlaatuista kasvua \n- Onko näytteessä havaittu atypiaa eli tavallisesta kudoksesta poikkeavia muutoksia \nRakenteelliseksi muutettava lausunto seuraa alla ""-merkkien sisällä:\n\"",
    # Prompt 4 variant 3 (7)
    "Olet lääketieteellinen assistentti, jonka tehtävänä on muuttaa vapaamuotoisena tekstinä olevia histopatologisia lausuntoja rakenteelliseen muotoon. Kaikkia kysyttyjä kohtia ei välttämättä löydy lausunnosta, jolloin kuuluu palauttaa puuttuvaa arvoa kuvaava NA. Jos koet että jokin vastaus on epävarma, on tärkeämpää palauttaa puuttuva arvo NA kuin palauttaa arvo jonka tarkkuus on kyseenalainen. Huomaa myös, että vaikka lausunnosta puuttuisi tieto jostain kysytystä arvosta, vastauksen kuuluu olla NA eikä nolla tai ei. Palauta rakenteelliseksi tulkittu lausunto JSON-formaatissa. Hae seuraaviin kysymyksiin vastaus: \n- Kuinka monta näytettä potilaalta on otettu \n- Näytteiden koko tai paino \n- Näytteen Gleason luokitus \n- Onko kyseessä vain hyvänlaatuinen eturauhasen liikakasvu \n- Onko näytteessä havaittu perineuraalista eli neuronien ympäröivää pahanlaatuista kasvua \n- Onko näytteessä havaittu atypiaa eli tavallisesta kudoksesta poikkeavia muutoksia \nRakenteelliseksi muutettava lausunto seuraa alla ""-merkkien sisällä:\n\"",
    # Prompt 4 variant 4 (8)
    "Olet lääketieteellinen assistentti, jonka tehtävänä on muuttaa vapaamuotoisena tekstinä olevia histopatologisia lausuntoja rakenteelliseen muotoon. Kaikkia kysyttyjä kohtia ei välttämättä löydy lausunnosta, jolloin kuuluu palauttaa puuttuvaa arvoa kuvaava NA.  Palauta rakenteelliseksi tulkittu lausunto JSON-formaatissa. Hae seuraaviin kysymyksiin vastaus (suluissa on esimerkit sallituista arvoista eri kohtiin): \n- Kuinka monta näytettä potilaalta on otettu [(Biopsioiden lukumäärä, koko elin yhtenä näytteenä, tai NA)] \n- Näytteiden koko tai paino [(grammoissa tai millimetreissä tai NA)] \n- Näytteen Gleason luokitus [(major+minor=summa, pelkkä summa tai NA)] \n- Onko kyseessä vain hyvänlaatuinen eturauhasen liikakasvu [(kyllä/ei/NA)] \n- Onko näytteessä havaittu perineuraalista eli neuronien ympäröivää pahanlaatuista kasvua [(kyllä/ei/NA)] \n- Onko näytteessä havaittu atypiaa eli tavallisesta kudoksesta poikkeavia muutoksia [(kyllä/ei/NA)] \nRakenteelliseksi muutettava lausunto seuraa alla ""-merkkien sisällä:\n\""
    ]
post = [
    # Typo: old prompt told to answer only a-c
    # End of prompt 0
    "\"\n1.	Analysoi annettua lääkärin kirjoittamaa lausuntoa, ja vastaa sen perusteella kysymyksiin a.-f. Anna kaikkien lausunnosta löydettyjen arvojen kanssa niihin liittyvä määre, jos sellainen on. Anna vastauksena vain numeerisia arvoja. Jos lausunnosta ei löydy selkeää vastausta, anna vastaus ’NA’. a.	Kuinka monta näytettä potilaalta on otettu? (Näytteiden määrä) b.	Minkä kokoisia otetut näytteet ovat? (Näytteiden koko) c.	Mikä on näytteiden Gleason-luokitus? (Gleason-luokitus) 2.	Analysoi annettua lääkärin kirjoittamaa lausuntoa, ja vastaa sen perusteella ’kyllä’ tai ’ei’ kysymyksiin d.-f., jos lausunnosta löytyy selkeä vastaus. Jos lausunnosta ei löydy selkeää vastausta, anna vastaus ’NA’.  d.	Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (Eturauhasen hyvälaatuinen liikakasvu) e.	Onko näytteessä havaittu perineuraalista kasvua? (Perineuraalinen kasvu) f.	Onko näytteessä havaittu atypiaa? (Atypia)",
    # End of prompt 1
    "\"\n1. Näytteiden määrä: \n- Etsi lausunnosta maininta siitä, kuinka monta näytettä potilaalta on otettu. \n- Anna vastaukseksi otettujen näytteiden määrä. \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden määrästä, anna vastaukseksi ’NA’ \n 2.Näytteiden koko: \n - Etsi lausunnosta maininta siitä, minkä kokoisia potilaalta otetut näytteet ovat. \n Anna vastaukseksi näytteiden koko numeerisena arvona. Anna numeerisen arvon lisäksi lausunnossa mainittu määre, jos sellainen on. \n Jos lausunnosta ei löydy selvää mainintaa näytteiden koosta, anna vastaukseksi ’NA’. \n3. Gleason-luokitus: \n Etsi lausunnosta maininta näytteiden Gleason-luokituksesta. \nAnna vastaukseksi näytteiden Gleason-luokitus muodossa major+minor=summa tai pelkkä summa. \nJos lausunnosta ei löydy selvää mainintaa näytteiden Gleason-luokituksesta, anna vastaukseksi ’NA’. \n4.Hyvälaatuinen eturauhasen liikakasvu: \nEtsi maininta siitä, onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua vai ei. \nJos lausunnossa on selvästi kerrottu, että näytteessä on hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’ei’. \nJos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’. \n5.Perineuraalinen kasvu: \nEtsi maininta siitä, onko näytteessä havaittu perineuraalista kasvua vai ei. \nJos lausunnossa on selvästi kerrottu, että näytteessä on perineuraalista kasvua, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole perineuraalista kasvua, anna vastaukseksi ’ei’. \nJos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’ \n6.Atypia: \n- Etsi maininta siitä, onko näytteessä havaittu atypiaa vai ei. \nJos lausunnossa on selvästi kerrottu, että näytteessä on atypiaa, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole atypiaa, anna vastaukseksi ’ei’. \n-Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’",
    # End of prompt 2
    "\"\n1. Kuinka monta näytettä potilaalta on otettu? (näytteiden määrä)\n2. Mikä on otettujen näytteiden koko? (näytteiden koko)\n3. Mikä on näytteiden Gleason-luokitus? (major+minor=summa, summa tai ’NA’)\n4. Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (’kyllä’, ’ei’ tai ’NA’)\n5. Onko näytteessä havaittu perineuraalista kasvua? (’kyllä’, ’ei’ tai ’NA’) \n6. Onko näytteessä havaittu atypiaa? (’kyllä’, ’ei’ tai ’NA’)",
    # End of prompt 3
    "\"\n1.	How many samples have been taken? (number of samples)\n2. What is the size of the samples taken? (size of samples)\n3. What is the Gleason score of the samples? (major+minor=sum, sum or ‘NA’)\n4. Can BPH be detected in the samples taken? (‘yes’, ‘no’ or ‘NA’)\n5. Can perineural growth be detected in the samples taken? (‘yes’, ‘no’ or ‘NA’)\n6. Can atypia be detected in the samples taken? ('yes’, ‘no’ or ‘NA’)",
    # End of prompt 4 bare
    "\"",
    # End of prompt 4 variant 1 (5)
    "\"",
    # End of prompt 4 variant 2 (6)
    "\"",
    # End of prompt 4 variant 3 (7)
    "\"",
    # End of prompt 4 variant 4 (8)
    "\""
]
inputs = [
    # 1
    "Tutkittavana edustava näyte prostatan tyyppipaikoista, yhteispituudelta 100mm. Havaitaan perineuraalia kasvua, suspekti maligni. Kohtalaisesti tulehdusmuutoksia, mutta ei selkeää malignia tai PIN löydöstä.",
    # 2
    "Kuusi formaliinifiksoitua preparaattia. A-D nähdään itsenäistä kasvua rauhasina, mutta C pieni alue rauhasten yhteensulautumista. E-F nähdään valtaosa kasvusta Gleason-luokkaa 3 (noin 60%), loput luokkaa 4, siis 3+4=7. Nämä näytteet vasemmasta lohkosta. Marginaalit kuitenkin puhtaat, eikä vesikkeli- tai perineuraali-invaasiota.",
    # 3
    "Näytteitä 3 prostatan paksuneulabiopsioita, edustavia näytekohdista. Näytteiden yhteispituus 90mm. Näkyy tulehdusmuutoksia, mutta ei atypiaa tai maligniin viittavia löydöksiä. Yksi näytteistä sisältää jonkin verran stroomaa (fibromuskulaari), ja rauhasrakenteita, mikä ehkä viittaisi hyperplasiaan. Esitiedoissa kuitenkin luki PSA:n arvon olleen 600, mahtoiko olla näppäilyvirhe?",
    # 4
    "Näytteinä prostatan paksuneulabiopsioita tyyppipaikoista otettuna, yhteispituus oikealta noin 60mm ja vasemmalta noin 80mm. Näytteestä B havaitaan karsinoomaa, joka menee jo Gleason tasolle 5 ja kokonais Gleason taso on 9 (4+5). Kyseistä muutosta noin 20% vasemmalla. Muissa näytteissä normaalia rauhasrakennetta, eikä merkittävää tulehdusta. WHO-luokituksen mukaan gradus 3.",
    # 5
    "Kaseteissa normaalin tavan mmukaan otetut prostatabiopsioat, kokonaispituus n. 150mm. Näytteesssä 1B oikeasta basiksesta hyppää esiin fokus, jossa pieniä rauhasrakenteita, missä tuma-atypiaa ja morfologinen löydös vastaisi adenokarsinoomaa, mutta on niin niukka että jää suspisio-asteelle. Muissa näytteissä normaalia rauhaskudosta. /Lauri Lääkäri, Meilahti, 1.1.2021",
    # 6
    "Katsottavaksi tullut yhteensä noin 5g edestä prostatan höylälastuja, joista kaikki käyty läpi. Potilas ollut suspekti aiemmin kohonneen PSA:n takia. Skoopilla katsoen lähes kaikissa nähdään adenokarsinoomaa, edustavin Gleason 4:ää ja sen eri variantteja joten pistesumma 8. Löydös siis vahvistaa aiemman suspision.",
    # 7
    "Tutkittavaksi tullut prostatektomia-preparaatti, joka ajetaan kaseteilla normaalikaavan mukaan. Näytteissä D-G apexia, basis näytteissä K-P, seminaalivehikkeleitä O-Q. Ensimmäisessä leikkeessä havaitaan jo jonkin verran kasvainta perifeerisesti, ja tuumori lähellä kapselin reunaa. Läpikasvua ei nähdä eikä pos. reunamarginaaleja. Basis ja seminaalivehikkelit puhtaat. Löydetyt tuumorit Gleason 7-tasoista karsinoomaa, josta isompi osuus scoorauksella 3 n. 60% löydöksissä.",
    # 8
    "Näytteinä 6 kpl edustavia prostatabiopsioita tyyppipaikoista, yhteensä n. 120mm. Laseilla nähdään prostatakudoksessa paikoin basaalisoluhyperplasiaa. Immunovärjäyksissä näytteissä 3-4 basaalisolut rajoittuneet ja värjäykset positiivisia, mutta fokus niin pieni että ei voida varmaa syöpädiagnoosia antaa. Johtopäätös: Suspicio-löydös biopsioista, mutta diagnoosi epävarma.",
    # 9
    "Höyläyslastuja tuli yhteensä noin 30g, joista noin 20g käynnistettiin kuudessa blokissa. Histologisessa tarkastelussa havaitaan hyvänlaatuista prostatakudosta, missä ei atypiaa, malignia, tai karsinoomaa näy. Vähän nähtävissä läiskittäistä tulehdusta. Löydös sopii siis epäiltyyn hyvänlaatuiseen hyperplasiaan.",
    # 10
    "Yhteensä 13g edestä höyläyslastuja ajettiin kahdeksalla kasetilla. Karsinoomaa todettiin histologisesti blokeissa F & G, joiden kasvutapa oli Gleason 3+3=6.",
    # 11
    "Ajetaan prostatetomiapreparaatti normaalin kaavan mukaan, s.e. oikea lohko värjätty vihreällä ja vasen keltaisella väriaineella. Näytteet A-D basiksesta apexiin päin makroleikkeinä, ja apex näytteinä E-F ja basis G-N, ja loput seminaalivesikkelit molemmilta puolilta N-O. Nähdään makroleikkeissä useampi selkeä fokus, joissa vallitseva Gleason luokka on 4 ja mukana myös jonkin verran luokkaa 3. Pääosa löydöksistä basiksessa, mutta apex ja seminaalivesikkelit puhtaat. Perineuraalista invaasiota havaitaan runsaasti, ja kasvain infiltroi selvästi kapselin läpi rasvaan.",
    # 12
    "Tutkittavana prostatan paksuneulanäytteitä rutiinikaavion mukaisesti, jossa materiaalia noin 180mm. Biopsioita yhteensä 13 kpl; näytteissä 4, 6) havaittiin karsinoomaa yhteensä viidessä biopsiossa, joissa erillisiä rauhasia muodostavan luokan isompi osuus luokkaa 3 ja pienempi osuus 4 (jälkimmäisen osuus noin 30% löydetystä tuumorista).",
    # 13
    "Höyläyksestä saatuja lastuja ajettiin 12 kudosblokkia. Lastuissa pienessä osassa nähdään karsinoomaa. Kasvu pääosin itsenäistä rauhasrakennetta ja mukana myös rauhasten yhteenkasvua, mutta karsinooman osuus jää pieneksi (alle 5%). Neoplastiseksi tulkittavassa osuudessa Gleason summana 7, josta suuremman osuuden luokka 3 noin 60% tuumorista.",
    # 14
    "Prostatalastuja yhteensä noin 19g, josta laitettu 10g histologiaan. Näkyy paljon fibromuskulaaria stroomaa ja mattomaista pahanlaatuista kasvua stroomassa. Tumat suurentuneet, kooltaan vaihtelevat ja tumajyväset erottuvat selvästi. Noin puolet lastujen pinta-alasta kasvainkudosta, jossa Gleason luokituksessa eniten tasoa 5 ja toiseksi eniten tasoa 4.",
    # 15
    "Näytteinä kohdennetut prostatabiopsiat eri puolilta. Näytteessä 1) 10mm, 2) 8mm, 3) 14mm ja 4) 14mm materiaalia. Näyte 1 epäedustava, näytteet 2 ja 3 edustavat tervettä prostatakudosta. Näytteessä 4 nähdään koko lieriön pituudelta adenokarsinoomaa, isompi osuus rauhasrakenteita muodostaen (Gleason 3, noin 90%) ja pienempi osuus rauhasten yhteensulautumista (Gleason 4, 10%). Kapselin läpikasvua tai perineuraalista invaasiota ei näytteissä nähdä.",
    # 16
    "Näytteenä 1-6 prostatabiopsiat tyyppipaikoista. Näytteen 3 biopsiasylinterit eivät edustavia, sillä siinä ei nähdä prostatakudosta. Muutoin näytteet ovat edustavat ja nähdään benigniä prostatakudosta. Rauhasepiteeleissä ei myöskään havaita merkittävää atypiaa. Näytteistä ei siis löydetä karsinoomaa tai PIN-muutoksia.",
    # 17
    "Näytteenä prostatektomiaresekaatti, josta tehty kuusi makroleikettä ja normaalit mikroskooppileikkeet. Sekä apexista että basiksesta otetuista leikkeistä löytyy adenokarsinoomaa. Apexin pitkittäinen leike näyttää mikroksooppisesti rauhasten yhteensulautumista sopien parhaiten Gleason 4+4 luokkaan, kun taas basiksessa lähinnä luokkaa 3+4. Näiden malignien näytteiden fokusten koot n. 8mm ja 5mm. Ei kuitenkaan havaita kapselista uloskasvua, ja marginaalit ovat puhtaat.",
    # 18
    "Tutkittavana purkillinen prostatan paksuneulanäytteitä molemmilta puolilta, joista vasemman puolen fragmentit pituudeltaan 10 ja 7mm ja oikean puolen 15 ja 10mm. Kroonista tulehdusta nähdään systemaattisesti. Vasemman puolen fragmenteissa näkyy lähinnä matalalle erilaistunutta karsinoomasolukkoa, josta Gleason kasvutapaa 3 pääsääntöisesti ja toiseksi eniten tapaa 4. Lisäksi hermojen ja suonien ympärillä kasvustoa. Oikean puolen fragmentit taas eivät näytä malignilta.",
    # 19
    "Tutkittavana systeemibiopsianeulanäytteitä pituudeltaan yhteensä 4+6+3 vasemmalta ja 5+7+8mm oikealta. Näytteiden indeksoinnissa kuitenkin käynyt fiba, ja vasen on oikea ja vice versa. Korjauksen jälkeen oikean puolen ensimmäisessä ja kolmannessa näytteessä näkyy maligniin viittaavaa kasvua ja marginaalit positiivit. Vahva adenokarsinooma-suspisio siis. Näytteiden laatu kuitenkin kyseenalainen ja neulat eivät todnäk täysin edustuskelpoisia, joten suositellaan biopsiointia uudelleen ohjatusti fuusiona oikealle suspisio-alueelle.",
    # 20
    "Näytteenä on yhteensä 12.3g lastuja. Käynnistetään ne yhdellä kasetilla. Histologisessa tarkastelussa näkyy läiskittäistä kroonista tulehdusta, ja näytteistä tulee yleinen vaikutelma strooman hyperplasiasta. Mitään maligniin suoraan viittaavaa ei näy.",
    # 21
    "Tutkittavana kuusi biopsialieriötä otettuna kohonneen PSA:n takia. Pesäke 1. vasemmalta edestä, nähdään 5mm matkalla huonosti erilaistunutta atyyppista rauhasrakennetta. Kyseessä adenokarsinooma, jossa Gleason luokitus 4+4=8. Pesäke 2. vasemmalta keskeltä noin 10mm matkalla nähdään myös karsinoomakudosta, jossa Gleasonin pistesumma 4+3=7 ja graduksen 4 osuus n. 80%. Pesäkkeessä 3. oikealta keskeltä myös löydös jossa gradusten 3 ja 4 suhde n. 70:30%, joten summa 7 (3+4). Lopuissa näytteistä lähinnä epiteelissä hyperplastisia muutoksia.",
    # 22
    "Näytteinä yhteensä 4g höyläyslastuja, jotka käynnistetty kolmeen kudoskasettiin. Todetaan mikroskooppisesti suhteellisen normaalia prostatasolukkoa, jossa kuitenkin voimakasta polttoartefaktaa. Rauhaset melko tuhoutuneet polttoartefaktoista johtuen, mutta löydökset viittaisivat hienoisesti prostatahyperplasiaan.",
    # 23
    "Tutkittavana on prostatektomiapreparaatti, joka käynnistetään normaalilla kaavalla oikea lohko vihreällä ja vasen lohko keltaisella värjäten. Apex näytteisiin A-C, kaksi makroleikettä kohti basista D-E, F-G basis ja H-I kaksi näytettä seminaalivehikkeleistä. Histologiassa nähdään laaja kasvain, joka ulottuu apexista basikseen asti. Osassa apex-näytteitä ulottuu myös reunan merkattuun rajaan ja tulee pienet positiiviset reunamarginaalit. Suurin kasvainfokus on basiksen puolella, missä vallitseva Gleason luokka 3 ja luokan 4 erilaistumista melkein yhtä paljon. Ei havaita kuitenkaan kasvaimen läpikasvua kapselin ulkopuolelle.",
    # 24
    "Näyte (1) sisältää kaksi kudoslieriötä, joiden pituus 8+6mm. Pidemmässä nähdään noin 4mm pituudelta (noin puolet kokonaispituudesta) kasvainkudosta, jossa Gleason 3 -kasvutapaa 60% ja 4 -osuus n. 40%. Näyte (2) yksi 10mm, jossa kasvainkudosta n. 5mm pituudelta ja erilaistuminen Gleason 3 n. 70% ja 4-luokkaa 30%. Näyte (3) sis. 5+5mm, joissa ei havaita tavallisesta poikkeavaa prostatakudosta. Näytteissa (1) ja (2) nähdään myös PIN-muutoksia. Todetaan em. näytteistä siis Gleason 7:n prostatan adenokarsinooma.",
    # 25
    "Näytteeksi saadut prostatan elektrosektiolastut on käynnistetty kahdeksassa blokissa. Histologisessa tarkastelussa näkyy pääasiassa säännöllistä prostatakudosta, löydös siis benigni.",
    # 26
    "Näytteet 1-4: Mikroskopiassa nähdään että näytteessä nro 2 on noin 2mm kokoinen alue prostatan adenokarsinoomaa. Löydöksessä vallitsevampi Gleason on luokka 4, joskin luokka 3 on lähes yhtä suuri %. Nähdään jonkin verran siis fuusioituneita ja huonosti muodostuneita rauhasia.",
    # 27
    "Tutkittavana 12 edustavaa neulabiopsiaa prostatan tyyppipaikoista. Näytteiden yhteispituus on noin 150mm. Nähdään normaaleja rauhasrakenteita ja jonkin verran aaltoilevaa hyperplastisen kaltaista epiteeliä. Lopputulos on siis lähinnä benignin oloista kasvua. Lääk. Heikki Histopatologi",
    # 28
    "Näytteenä on edustavat prostatabiopsiat tyyppilokaatioista. Karsinoomaa löytyi seuraavasti: (1) oikean basiksen 8mm pituinen biopsia ja 7mm pituinen biopsia, joissa molemmissa Gleason 3 arkkitehtuuri pääsääntöisesti. (2) vasemmalla basiksessa 5mm myös Gleason 3 arkkitehtuurilla karsinoomalöydös. Toinen vasemman basiksen näyte puhdas. Loput näytteet myös puhtaita, joskin jonkin verran tulehdussolujen kertymää. Ei havaita tuma-atypiaa. Yhteenvetona 3/12 biopsiosta havaittu 3+3 tyypin adenokarsinoomaa.",
    # 29
    "Prostatan paksuneulabiopsianäytteet tutkittavana rutiinikaavion mukaisesti: 1 basis oikea, 2 keski oikea, 3 apex oikea, 4 basis vasen, 5 keski vasen, 6 apex vasen. Histologisesti leikkeet onnistuneita. Näytteissä 5-6 pieneltä alueelta (<1mm) nähdään Gleason 5 kasvutapaa, mutta pääosin havaitaan huonosti erilaistunutta Gleason 4+3=7 kasvua.",
    # 30
    "Tutkittavana kolme fuusiobiopsiaa prostatan suspektista fokuksesta. Yhteispituudesta 30mm nähdänä n. puolelta matkaa karsinoomafokuksia siten että pituudet noin 7, 6 ja 2mm. Näissä tason 3 graduksen kasvu promenttia kasvua, joskus jonkin verran myös Gleaosn 4 -tyypin silmukoituvaa rakenneta noin kolmasosalta karsinooman pituudelta. Yhteenvetona löydös score 7 yhteensä 15mm matkalta, jossa 3 arkkitehtuuri n. 2/3 ja 4 arkkitehtuuri n. 1/3 karsinooman osasta.",
    # Gibberish 1 (31)
    "Beep boop? Boop biip. Blarp!",
    # Gibberish 2 (32)
    "Lorem ipsum, 1+2=9, foo bar -0% yks kaks kolme on yhteensä kuus.",
    # Gibberish 3 (33)
    "Tämä on harhaanjohtava lause, jonka tehtävänä on testata uskoisiko kielimalli esimerkiksi löydetyn Gleason ryhmän olevan miinus sata ja että mukamas näyte painoi tuhat kiloa."
]

def getPrompt(promptIndex, inputIndex):
    return pre[promptIndex] + inputs[inputIndex] + post[promptIndex]

def getInput(inputIndex):
    return inputs[inputIndex]

def getMaxInputs():
    return len(inputs)

def getMaxPrompts():
    return len(pre)
