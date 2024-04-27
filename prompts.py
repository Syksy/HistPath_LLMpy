pre = [
    "Merkkien \"\" välissä on annettu lääkärin kirjoittama potilaslausunto. Vastaa esitettyihin kysymyksiin. Anna vastaukset JSON-formaatissa. Anna vastauksissa avaimena merkkien ( ) välissä oleva sisältö kysymyskohtaisesti.\n\"",
    "Merkkien \"\" välissä on annettu lääkärin kirjoittama potilaslausunto. Tehtäväsi on toimia lääketieteellisenä assistenttina ja etsiä potilaslausunnosta alla listatut tiedot. Käy kysymykset läpi askel kerrallaan. Anna vastaukset JSON-formaatissa. \"",
    "Merkkien \"\" välissä on annettu lääkärin kirjoittama potilaslausunto. Tehtäväsi on etsiä tietoa annetusta potilaslausunnosta. Etsi vastaukset alla oleviin kysymyksiin. Anna vastaukset () merkkien välissä olevien ohjeiden mukaan. Anna vastaukset JSON-formaatissa.\"",
    "You will be provided with text delimited by quotes (symbols \"\"). The text is a medical note written by a doctor and it is in Finnish. Your job is to extract information from the given text. Find the answers to the questions below. Give the answers based on the instructions given between the parenthesis. Give the answers in JSON-format. \""
    ]
post = [
    # Typo: old prompt told to answer only a-c
    "\"\n1.	Analysoi annettua lääkärin kirjoittamaa potilaslausuntoa, ja vastaa sen perusteella kysymyksiin a.-f. Anna kaikkien lausunnosta löydettyjen arvojen kanssa niihin liittyvä määre, jos sellainen on. Anna vastauksena vain numeerisia arvoja. Jos potilaslausunnosta ei löydy selkeää vastausta, anna vastaus ’NA’. a.	Kuinka monta näytettä potilaalta on otettu? (Näytteiden määrä) b.	Minkä kokoisia otetut näytteet ovat? (Näytteiden koko) c.	Mikä on näytteiden Gleason-luokitus? (Gleason-luokitus) 2.	Analysoi annettua lääkärin kirjoittamaa potilaslausuntoa, ja vastaa sen perusteella ’kyllä’ tai ’ei’ kysymyksiin d.-f., jos lausunnosta löytyy selkeä vastaus. Jos potilaslausunnosta ei löydy selkeää vastausta, anna vastaus ’NA’.  d.	Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (Eturauhasen hyvälaatuinen liikakasvu) e.	Onko näytteessä havaittu perineuraalista kasvua? (Perineuraalinen kasvu) f.	Onko näytteessä havaittu atypiaa? (Atypia)",
    "\"\n1. Näytteiden määrä: \n- Etsi potilaslausunnosta maininta siitä, kuinka monta näytettä potilaalta on otettu. \n- Anna vastaukseksi otettujen näytteiden määrä. \n- Jos potilaslausunnosta ei löydy selvää mainintaa näytteiden määrästä, anna vastaukseksi ’NA’ \n 2.Näytteiden koko: \n - Etsi potilaslausunnosta maininta siitä, minkä kokoisia potilaalta otetut näytteet ovat. \n Anna vastaukseksi näytteiden koko numeerisena arvona. Anna numeerisen arvon lisäksi potilaslausunnossa mainittu määre, jos sellainen on. \n Jos potilaslausunnosta ei löydy selvää mainintaa näytteiden koosta, anna vastaukseksi ’NA’. \n3. Gleason-luokitus: \n Etsi potilaslausunnosta maininta näytteiden Gleason-luokituksesta. \nAnna vastaukseksi näytteiden Gleason-luokitus muodossa major+minor=summa tai pelkkä summa. \nJos potilaslausunnosta ei löydy selvää mainintaa näytteiden Gleason-luokituksesta, anna vastaukseksi ’NA’. \n4.Hyvälaatuinen eturauhasen liikakasvu: \nEtsi maininta siitä, onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua vai ei. \nJos potilaslausunnossa on selvästi kerrottu, että näytteessä on hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’kyllä’. Jos potilaslausunnossa on selvästi kerrottu, että näytteessä ei ole hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’ei’. \nJos potilaslausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’. \n5.Perineuraalinen kasvu: \nEtsi maininta siitä, onko näytteessä havaittu perineuraalista kasvua vai ei. \nJos potilaslausunnossa on selvästi kerrottu, että näytteessä on perineuraalista kasvua, anna vastaukseksi ’kyllä’. Jos potilaslausunnossa on selvästi kerrottu, että näytteessä ei ole perineuraalista kasvua, anna vastaukseksi ’ei’. \nJos potilaslausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’ \n6.Atypia: \n- Etsi maininta siitä, onko näytteessä havaittu atypiaa vai ei. \nJos potilaslausunnossa on selvästi kerrottu, että näytteessä on atypiaa, anna vastaukseksi ’kyllä’. Jos potilaslausunnossa on selvästi kerrottu, että näytteessä ei ole atypiaa, anna vastaukseksi ’ei’. \n-Jos potilaslausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’",
    "\"\n1. Kuinka monta näytettä potilaalta on otettu? (näytteiden määrä)\n2. Mikä on otettujen näytteiden koko? (näytteiden koko)\n3. Mikä on näytteiden Gleason-luokitus? (major+minor=summa, summa tai ’NA’)\n4. Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (’kyllä’, ’ei’ tai ’NA’)\n5. Onko näytteessä havaittu perineuraalista kasvua? (’kyllä’, ’ei’ tai ’NA’) \n6. Onko näytteessä havaittu atypiaa? (’kyllä’, ’ei’ tai ’NA’)",
    "\"\n1.	How many samples have been taken? (number of samples)\n2. What is the size of the samples taken? (size of samples)\n3. What is the Gleason score of the samples? (major+minor=sum, sum or ‘NA’)\n4. Can BPH be detected in the samples taken? (‘yes’, ‘no’ or ‘NA’)\n5. Can perineural growth be detected in the samples taken? (‘yes’, ‘no’ or ‘NA’)\n6. Can atypia be detected in the samples taken? ('yes’, ‘no’ or ‘NA’)"
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
    "Näytteinä 6 kpl edustavia prostatabiopsioita tyyppipaikoista, yhteensä n. 120mm. Laseilla nähdään prostatakudoksessa paikoin basaalisoluhyperplasiaa. Immunovärjäyksissä näytteissä 3-4 basaalisolut rajoittuneet ja värjäykset positiivisia, mutta fokus niin pieni että ei voida varmaa syöpädiagnoosia antaa. Johtopäätös: Suspicio-löydös biopsioista, mutta diagnoosi epävarmaa.",
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
    "A histo-pathological statement in Finnish.",
    # 22
    "A histo-pathological statement in Finnish.",
    # 23
    "A histo-pathological statement in Finnish.",
    # 24
    "A histo-pathological statement in Finnish.",
    # 25
    "A histo-pathological statement in Finnish.",
    # 26
    "A histo-pathological statement in Finnish.",
    # 27
    "A histo-pathological statement in Finnish.",
    # 28
    "A histo-pathological statement in Finnish.",
    # 29
    "A histo-pathological statement in Finnish.",
    # 30
    "A histo-pathological statement in Finnish.",
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
