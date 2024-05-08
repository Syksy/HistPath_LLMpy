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
    "Olet lääketieteellinen assistentti, jonka tehtävänä on muuttaa vapaamuotoisena tekstinä olevia histopatologisia lausuntoja rakenteelliseen muotoon. Kaikkia kysyttyjä kohtia ei välttämättä löydy lausunnosta, jolloin kuuluu palauttaa puuttuvaa arvoa kuvaava NA.  Palauta rakenteelliseksi tulkittu lausunto JSON-formaatissa. Hae seuraaviin kysymyksiin vastaus (suluissa on esimerkit sallituista arvoista eri kohtiin): \n- Kuinka monta näytettä potilaalta on otettu [(Biopsioiden lukumäärä, koko elin yhtenä näytteenä, tai NA)] \n- Näytteiden koko tai paino [(grammoissa tai millimetreissä tai NA)] \n- Näytteen Gleason luokitus [(major+minor=summa, pelkkä summa tai NA)] \n- Onko kyseessä vain hyvänlaatuinen eturauhasen liikakasvu [(kyllä/ei/NA)] \n- Onko näytteessä havaittu perineuraalista eli neuronien ympäröivää pahanlaatuista kasvua [(kyllä/ei/NA)] \n- Onko näytteessä havaittu atypiaa eli tavallisesta kudoksesta poikkeavia muutoksia [(kyllä/ei/NA)] \nRakenteelliseksi muutettava lausunto seuraa alla ""-merkkien sisällä:\n\"",
    # 9: May 8th prompt 0.0
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Vastaa esitettyihin kysymyksiin annetun lausunnon perusteella. Anna vastaukset JSON-formaatissa. Anna vastauksissa avaimena merkkien ( ) välissä oleva sisältö kysymyskohtaisesti.\n\""
    # 10: May 8th prompt variant 0.1
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Olet erittäin kokenut histopatologiaan erikoistunut erikoislääkäri ja tehtäväsi on vastata esitettyihin kysymyksiin annetun lausunnon perusteella. Anna vastaukset JSON-formaatissa. Anna vastauksissa avaimena merkkien ( ) välissä oleva sisältö kysymyskohtaisesti.\n\"",
    # 11: May 8th prompt variant 1.0
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Tehtäväsi on etsiä lausunnosta alla listatut tiedot. Käy kohdat läpi askel kerrallaan. Anna vastaukset yhtenä objektina JSON-formaatissa.\n\"",
    # 12: May 8th prompt variant 1.1
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Olet erittäin kokenut histopatologiaan erikoistunut erikoislääkäri, jonka tehtävä on etsiä lausunnosta alla listatut tiedot. Käy kohdat läpi askel kerrallaan. Anna vastaukset yhtenä objektina JSON-formaatissa. \n\"",
    # 13: May 8th prompt variant 1.2
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Tehtäväsi on etsiä lausunnosta alla listatut tiedot. Käy kohdat läpi askel kerrallaan. Anna vastaukset yhtenä objektina JSON-formaatissa. Älä selitä vastauksia enempää, anna vastauksena vain JSON-tiedosto.\n\"",
    # 14: May 8th prompt variant 2.0
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Tehtäväsi on etsiä tietoa annetusta lausunnosta. Etsi vastaukset alla oleviin kysymyksiin. Lausunnosta ei välttämättä löydy vastauksia kaikkiin kysymyksiin, anna tällöin vastaukseksi ’NA’. Anna vastaukset JSON-formaatissa.\n\"",
    # 15: May 8th prompt variant 2.1
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Tehtäväsi on etsiä tietoa annetusta lausunnosta. Etsi vastaukset alla oleviin kysymyksiin. Anna vastaukset () merkkien välissä olevien ohjeiden mukaan. Anna vastaukset JSON-formaatissa.\n\"",
    # 16: May 8th prompt variant 2.2
    "Merkkien \"\" välissä on annettu histopatologin kirjoittama lausunto eturauhassyöpänäytteestä. Olet erittäin kokenut histopatologiaan erikoistunut erikoislääkäri, jonka tehtävä on etsiä tietoa annetusta lausunnosta. Etsi vastaukset alla oleviin kysymyksiin. Anna vastaukset () merkkien välissä olevien ohjeiden mukaan. Anna vastaukset JSON-formaatissa.\n\"",
    # 17: May 8th prompt variant 3.0
    "You will be provided with text delimited by quotes. The text is a medical note written by a pathologist and it is in Finnish. Your job is to extract information from the given text. Find answers to the questions below and answer in Finnish. You might not be able to find answers to all the questions, in these cases give ‘NA’ as the answer. Give the answers in JSON-format.\n\"",
    # 18: May 8th prompt variant 3.1
    "You will be provided with text delimited by quotes. The text is a medical note written by a pathologist and it is in Finnish. Your job is to extract information from the given text. Find answers to the questions below. Give the answers based on the instructions given between the parenthesis. Give the answers in JSON-format.\n\"",
    # 19: May 8th prompt variant 3.2
    "You will be provided with text delimited by quotes. The text is a medical note written by a histopathologist and it is in Finnish. Your job is to act as a very experienced doctor that specializes in pathology and extract information from the given text. Find the answers to the questions below. Give the answers based on the instructions given between the parenthesis. Give the answers in JSON-format.\n\""
    ]
post = [
    # End of prompt 0
    "\"\n1.	Analysoi annettua lääkärin kirjoittamaa lausuntoa, ja vastaa sen perusteella kysymyksiin a.-c. Anna kaikkien lausunnosta löydettyjen arvojen kanssa niihin liittyvä määre, jos sellainen on. Anna vastauksena vain numeerisia arvoja. Jos lausunnosta ei löydy selkeää vastausta, anna vastaus ’NA’. a.	Kuinka monta näytettä potilaalta on otettu? (Näytteiden määrä) b.	Minkä kokoisia otetut näytteet ovat? (Näytteiden koko) c.	Mikä on näytteiden Gleason-luokitus? (Gleason-luokitus) 2.	Analysoi annettua lääkärin kirjoittamaa lausuntoa, ja vastaa sen perusteella ’kyllä’ tai ’ei’ kysymyksiin d.-f., jos lausunnosta löytyy selkeä vastaus. Jos lausunnosta ei löydy selkeää vastausta, anna vastaus ’NA’.  d.	Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (Eturauhasen hyvälaatuinen liikakasvu) e.	Onko näytteessä havaittu perineuraalista kasvua? (Perineuraalinen kasvu) f.	Onko näytteessä havaittu atypiaa? (Atypia)",
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
    "\"",
    # 9: May 8th prompt 0.0
    "\"\nAnalysoi annettua histopatologin kirjoittamaa lausuntoa, ja vastaa sen perusteella kysymyksiin 1.-3. Anna kaikkien lausunnosta löydettyjen arvojen kanssa niihin liittyvä määre, jos sellainen on. Anna vastauksena vain numeerisia arvoja. Jos patologisesta lausunnosta ei löydy selkeää vastausta, anna vastaukseksi ’NA’. \n1.	Kuinka monta näytettä potilaalta on otettu? (Näytteiden määrä) \n2.	Minkä kokoisia otetut näytteet ovat? (Näytteiden koko) \n3.	Mikä on näytteiden Gleason-luokitus? (Gleason-luokitus) \nAnalysoi annettua histopatologin kirjoittamaa lausuntoa, ja vastaa sen perusteella kysymyksiin 4.-6., Anna vastaukseksi ’kyllä’ tai ’ei’, jos lausunnosta löytyy selkeä vastaus. Jos potilaslausunnosta ei löydy selkeää vastausta, anna vastaukseksi ’NA’. \n4.	Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (Eturauhasen hyvälaatuinen liikakasvu) \n5.	Onko näytteessä havaittu perineuraalista kasvua? (Perineuraalinen kasvu) \n6.	Onko näytteessä havaittu atypiaa? (Atypia)",
    # 10: May 8th prompt variant 0.1
    "\"\nAnalysoi annettua histopatologin kirjoittamaa lausuntoa, ja vastaa sen perusteella kysymyksiin 1.-3. Anna kaikkien lausunnosta löydettyjen arvojen kanssa niihin liittyvä määre, jos sellainen on. Anna vastauksena vain numeerisia arvoja. Jos patologisesta lausunnosta ei löydy selkeää vastausta, anna vastaukseksi ’NA’. \n1.	Kuinka monta näytettä potilaalta on otettu? (Näytteiden määrä) \n2.	Minkä kokoisia otetut näytteet ovat? (Näytteiden koko) \n3.	Mikä on näytteiden Gleason-luokitus? (Gleason-luokitus) \nAnalysoi annettua histopatologin kirjoittamaa lausuntoa, ja vastaa sen perusteella kysymyksiin 4.-6., Anna vastaukseksi ’kyllä’ tai ’ei’, jos lausunnosta löytyy selkeä vastaus. Jos potilaslausunnosta ei löydy selkeää vastausta, anna vastaukseksi ’NA’. \n4.	Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (Eturauhasen hyvälaatuinen liikakasvu) \n5.	Onko näytteessä havaittu perineuraalista kasvua? (Perineuraalinen kasvu) \n6.	Onko näytteessä havaittu atypiaa? (Atypia)",
    # 11: May 8th prompt variant 1.0
    "\"\n1.Näytteiden määrä: \n- Etsi lausunnosta maininta siitä, kuinka monta näytettä potilaalta on otettu. \n- Anna vastaukseksi otettujen näytteiden määrä \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden määrästä, anna vastaukseksi ’NA’ \n\n2.Näytteiden koko: \n- Etsi lausunnosta maininta siitä, minkä kokoisia potilaalta otetut näytteet ovat \n- Anna vastaukseksi näytteiden koko numeerisena arvona. Anna numeerisen arvon lisäksi lausunnossa mainittu määre, jos sellainen on \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden koosta, anna vastaukseksi ’NA’ \n\n3. Gleason-luokitus: \n- Etsi lausunnosta maininta näytteiden Gleason-luokituksesta \n- Anna vastaukseksi näytteiden Gleason-luokitus muodossa major+minor=summa tai pelkkä summa \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden Gleason-luokituksesta, anna vastaukseksi ’NA’ \n\n4.Hyvälaatuinen eturauhasen liikakasvu: \n- Etsi maininta siitä, onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’ei’. \n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’ \n\n5.Perineuraalinen kasvu: \n- Etsi maininta siitä, onko näytteessä havaittu perineuraalista kasvua vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on perineuraalista kasvua, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole perineuraalista kasvua, anna vastaukseksi ’ei’. \n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’ \n\n6.Atypia: \n- Etsi maininta siitä, onko näytteessä havaittu atypiaa vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on atypiaa, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole atypiaa, anna vastaukseksi ’ei’.\n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’",
    # 12: May 8th prompt variant 1.1
    "\"\n1.Näytteiden määrä: \n- Etsi lausunnosta maininta siitä, kuinka monta näytettä potilaalta on otettu. \n- Anna vastaukseksi otettujen näytteiden määrä \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden määrästä, anna vastaukseksi ’NA’ \n\n2.Näytteiden koko: \n- Etsi lausunnosta maininta siitä, minkä kokoisia potilaalta otetut näytteet ovat \n- Anna vastaukseksi näytteiden koko numeerisena arvona. Anna numeerisen arvon lisäksi lausunnossa mainittu määre, jos sellainen on \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden koosta, anna vastaukseksi ’NA’ \n\n3. Gleason-luokitus: \n- Etsi lausunnosta maininta näytteiden Gleason-luokituksesta \n- Anna vastaukseksi näytteiden Gleason-luokitus muodossa major+minor=summa tai pelkkä summa \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden Gleason-luokituksesta, anna vastaukseksi ’NA’ \n\n4.Hyvälaatuinen eturauhasen liikakasvu: \n- Etsi maininta siitä, onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’ei’. \n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’ \n\n5.Perineuraalinen kasvu: \n- Etsi maininta siitä, onko näytteessä havaittu perineuraalista kasvua vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on perineuraalista kasvua, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole perineuraalista kasvua, anna vastaukseksi ’ei’. \n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’ \n\n6.Atypia: \n- Etsi maininta siitä, onko näytteessä havaittu atypiaa vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on atypiaa, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole atypiaa, anna vastaukseksi ’ei’.\n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’",
    # 13: May 8th prompt variant 1.2
    "\"\n1.Näytteiden määrä: \n- Etsi lausunnosta maininta siitä, kuinka monta näytettä potilaalta on otettu. \n- Anna vastaukseksi otettujen näytteiden määrä \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden määrästä, anna vastaukseksi ’NA’ \n\n2.Näytteiden koko: \n- Etsi lausunnosta maininta siitä, minkä kokoisia potilaalta otetut näytteet ovat \n- Anna vastaukseksi näytteiden koko numeerisena arvona. Anna numeerisen arvon lisäksi lausunnossa mainittu määre, jos sellainen on \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden koosta, anna vastaukseksi ’NA’ \n\n3. Gleason-luokitus: \n- Etsi lausunnosta maininta näytteiden Gleason-luokituksesta \n- Anna vastaukseksi näytteiden Gleason-luokitus muodossa major+minor=summa tai pelkkä summa \n- Jos lausunnosta ei löydy selvää mainintaa näytteiden Gleason-luokituksesta, anna vastaukseksi ’NA’ \n\n4.Hyvälaatuinen eturauhasen liikakasvu: \n- Etsi maininta siitä, onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole hyvälaatuista eturauhasen liikakasvua, anna vastaukseksi ’ei’. \n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’ \n\n5.Perineuraalinen kasvu: \n- Etsi maininta siitä, onko näytteessä havaittu perineuraalista kasvua vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on perineuraalista kasvua, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole perineuraalista kasvua, anna vastaukseksi ’ei’. \n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’ \n\n6.Atypia: \n- Etsi maininta siitä, onko näytteessä havaittu atypiaa vai ei \n- Jos lausunnossa on selvästi kerrottu, että näytteessä on atypiaa, anna vastaukseksi ’kyllä’. Jos lausunnossa on selvästi kerrottu, että näytteessä ei ole atypiaa, anna vastaukseksi ’ei’.\n- Jos lausunnosta ei löydy selvää mainintaa, anna vastaukseksi ’NA’",
    # 14: May 8th prompt variant 2.0
    "\"\n1. Kuinka monta näytettä potilaalta on otettu? \n2. Minkä kokoisia otetut näytteet ovat?  \n3. Mikä on näytteiden Gleason-luokitus? \n4. Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? \n5. Onko näytteessä havaittu perineuraalista kasvua? \n6. Onko näytteessä havaittu atypiaa?",
    # 15: May 8th prompt variant 2.1
    "\"\n1. Kuinka monta näytettä potilaalta on otettu? (näytteiden määrä) \n2. Minkä kokoisia otetutu näytteet ovat? (näytteiden koko) \n3. Mikä on näytteiden Gleason-luokitus? (major+minor=summa/summa/NA) \n4. Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (kyllä/ei/NA) \n5. Onko näytteessä havaittu perineuraalista kasvua? (kyllä/ei/tai/NA)  \n6. Onko näytteessä havaittu atypiaa? (kyllä/ei/NA)",
    # 16: May 8th prompt variant 2.2
    "\"\n1. Kuinka monta näytettä potilaalta on otettu? (näytteiden määrä) \n2. Minkä kokoisia otetutu näytteet ovat? (näytteiden koko) \n3. Mikä on näytteiden Gleason-luokitus? (major+minor=summa/summa/NA) \n4. Onko näytteessä havaittu hyvälaatuista eturauhasen liikakasvua? (kyllä/ei/NA) \n5. Onko näytteessä havaittu perineuraalista kasvua? (kyllä/ei/tai/NA)  \n6. Onko näytteessä havaittu atypiaa? (kyllä/ei/NA)",
    # 17: May 8th prompt variant 3.0
    "\"\n1.	How many samples have been taken? \n2.	What is the size of the samples taken? \n3.	What is the Gleason score of the samples?  \n4.	Can BPH be detected in the samples taken? \n5.	Can perineural growth be detected in the samples taken?  \n6.	Can atypia be detected in the samples taken?",
    # 18: May 8th prompt variant 3.1
    "\"\n1. How many samples have been taken? (number of samples) \n2.What is the size of the samples taken? (size of samples) \n3.What is the Gleason score of the samples? (major+minor=sum/sum/NA) \n4.Can BPH be detected in the samples taken? (kyllä/ei/NA) \n5.Can perineural growth be detected in the samples taken? (kyllä/ei/NA/) \n6.Can atypia be detected in the samples taken? (kyllä/ei/NA)",
    # 19: May 8th prompt variant 3.2
    "\"\n1.	How many samples have been taken? (number of samples) \n2.	What is the size of the samples taken? (size of samples) \n3.	What is the Gleason score of the samples? (major+minor=sum/sum/NA) \n4.	Can BPH be detected in the samples taken? (kyllä/ei/NA) \n5.	Can perineural growth be detected in the samples taken? (yes/no/NA) \n6.	Can atypia be detected in the samples taken? (kyllä/ei/NA)"
]
# Statements in original Finnish
inputs_fin = [
    # 0
    "Tutkittavana edustava näyte prostatan tyyppipaikoista, yhteispituudelta 100mm. Havaitaan perineuraalia kasvua, suspekti maligni. Kohtalaisesti tulehdusmuutoksia, mutta ei selkeää malignia tai PIN löydöstä.",
    # 1
    "Kuusi formaliinifiksoitua preparaattia. A-D nähdään itsenäistä kasvua rauhasina, mutta C pieni alue rauhasten yhteensulautumista. E-F nähdään valtaosa kasvusta Gleason-luokkaa 3 (noin 60%), loput luokkaa 4, siis 3+4=7. Nämä näytteet vasemmasta lohkosta. Marginaalit kuitenkin puhtaat, eikä vesikkeli- tai perineuraali-invaasiota.",
    # 2
    "Näytteitä 3 prostatan paksuneulabiopsioita, edustavia näytekohdista. Näytteiden yhteispituus 90mm. Näkyy tulehdusmuutoksia, mutta ei atypiaa tai maligniin viittavia löydöksiä. Yksi näytteistä sisältää jonkin verran stroomaa (fibromuskulaari), ja rauhasrakenteita, mikä ehkä viittaisi hyperplasiaan. Esitiedoissa kuitenkin luki PSA:n arvon olleen 600, mahtoiko olla näppäilyvirhe?",
    # 3
    "Näytteinä prostatan paksuneulabiopsioita tyyppipaikoista otettuna, yhteispituus oikealta noin 60mm ja vasemmalta noin 80mm. Näytteestä B havaitaan karsinoomaa, joka menee jo Gleason tasolle 5 ja kokonais Gleason taso on 9 (4+5). Kyseistä muutosta noin 20% vasemmalla. Muissa näytteissä normaalia rauhasrakennetta, eikä merkittävää tulehdusta. WHO-luokituksen mukaan gradus 3.",
    # 4
    "Kaseteissa normaalin tavan mukaan otetut prostatabiopsioat, kokonaispituus n. 150mm. Näytteesssä 1B oikeasta basiksesta hyppää esiin fokus, jossa pieniä rauhasrakenteita, missä tuma-atypiaa ja morfologinen löydös vastaisi adenokarsinoomaa, mutta on niin niukka että jää suspisio-asteelle. Muissa näytteissä normaalia rauhaskudosta. /Lauri Lääkäri, Meilahti, 1.1.2021",
    # 5
    "Katsottavaksi tullut yhteensä noin 5g edestä prostatan höylälastuja, joista kaikki käyty läpi. Potilas ollut suspekti aiemmin kohonneen PSA:n takia. Skoopilla katsoen lähes kaikissa nähdään adenokarsinoomaa, edustavin Gleason 4:ää ja sen eri variantteja joten pistesumma 8. Löydös siis vahvistaa aiemman suspision.",
    # 6
    "Tutkittavaksi tullut prostatektomia-preparaatti, joka ajetaan kaseteilla normaalikaavan mukaan. Näytteissä D-G apexia, basis näytteissä K-P, seminaalivehikkeleitä O-Q. Ensimmäisessä leikkeessä havaitaan jo jonkin verran kasvainta perifeerisesti, ja tuumori lähellä kapselin reunaa. Läpikasvua ei nähdä eikä pos. reunamarginaaleja. Basis ja seminaalivehikkelit puhtaat. Löydetyt tuumorit Gleason 7-tasoista karsinoomaa, josta isompi osuus scoorauksella 3 n. 60% löydöksissä.",
    # 7
    "Näytteinä 6 kpl edustavia prostatabiopsioita tyyppipaikoista, yhteensä n. 120mm. Laseilla nähdään prostatakudoksessa paikoin basaalisoluhyperplasiaa. Immunovärjäyksissä näytteissä 3-4 basaalisolut rajoittuneet ja värjäykset positiivisia, mutta fokus niin pieni että ei voida varmaa syöpädiagnoosia antaa. Johtopäätös: Suspicio-löydös biopsioista, mutta diagnoosi epävarma.",
    # 8
    "Höyläyslastuja tuli yhteensä noin 30g, joista noin 20g käynnistettiin kuudessa blokissa. Histologisessa tarkastelussa havaitaan hyvänlaatuista prostatakudosta, missä ei atypiaa, malignia, tai karsinoomaa näy. Vähän nähtävissä läiskittäistä tulehdusta. Löydös sopii siis epäiltyyn hyvänlaatuiseen hyperplasiaan.",
    # 9
    "Yhteensä 13g edestä höyläyslastuja ajettiin kahdeksalla kasetilla. Karsinoomaa todettiin histologisesti blokeissa F & G, joiden kasvutapa oli Gleason 3+3=6.",
    # 10
    "Ajetaan prostatetomiapreparaatti normaalin kaavan mukaan, s.e. oikea lohko värjätty vihreällä ja vasen keltaisella väriaineella. Näytteet A-D basiksesta apexiin päin makroleikkeinä, ja apex näytteinä E-F ja basis G-N, ja loput seminaalivesikkelit molemmilta puolilta N-O. Nähdään makroleikkeissä useampi selkeä fokus, joissa vallitseva Gleason luokka on 4 ja mukana myös jonkin verran luokkaa 3. Pääosa löydöksistä basiksessa, mutta apex ja seminaalivesikkelit puhtaat. Perineuraalista invaasiota havaitaan runsaasti, ja kasvain infiltroi selvästi kapselin läpi rasvaan.",
    # 11
    "Tutkittavana prostatan paksuneulanäytteitä rutiinikaavion mukaisesti, jossa materiaalia noin 180mm. Biopsioita yhteensä 13 kpl; näytteissä 4, 6) havaittiin karsinoomaa yhteensä viidessä biopsiossa, joissa erillisiä rauhasia muodostavan luokan isompi osuus luokkaa 3 ja pienempi osuus 4 (jälkimmäisen osuus noin 30% löydetystä tuumorista).",
    # 12
    "Höyläyksestä saatuja lastuja ajettiin 12 kudosblokkia. Lastuissa pienessä osassa nähdään karsinoomaa. Kasvu pääosin itsenäistä rauhasrakennetta ja mukana myös rauhasten yhteenkasvua, mutta karsinooman osuus jää pieneksi (alle 5%). Neoplastiseksi tulkittavassa osuudessa Gleason summana 7, josta suuremman osuuden luokka 3 noin 60% tuumorista.",
    # 13
    "Prostatalastuja yhteensä noin 19g, josta laitettu 10g histologiaan. Näkyy paljon fibromuskulaaria stroomaa ja mattomaista pahanlaatuista kasvua stroomassa. Tumat suurentuneet, kooltaan vaihtelevat ja tumajyväset erottuvat selvästi. Noin puolet lastujen pinta-alasta kasvainkudosta, jossa Gleason luokituksessa eniten tasoa 5 ja toiseksi eniten tasoa 4.",
    # 14
    "Näytteinä kohdennetut prostatabiopsiat eri puolilta. Näytteessä 1) 10mm, 2) 8mm, 3) 14mm ja 4) 14mm materiaalia. Näyte 1 epäedustava, näytteet 2 ja 3 edustavat tervettä prostatakudosta. Näytteessä 4 nähdään koko lieriön pituudelta adenokarsinoomaa, isompi osuus rauhasrakenteita muodostaen (Gleason 3, noin 90%) ja pienempi osuus rauhasten yhteensulautumista (Gleason 4, 10%). Kapselin läpikasvua tai perineuraalista invaasiota ei näytteissä nähdä.",
    # 15
    "Näytteenä 1-6 prostatabiopsiat tyyppipaikoista. Näytteen 3 biopsiasylinterit eivät edustavia, sillä siinä ei nähdä prostatakudosta. Muutoin näytteet ovat edustavat ja nähdään benigniä prostatakudosta. Rauhasepiteeleissä ei myöskään havaita merkittävää atypiaa. Näytteistä ei siis löydetä karsinoomaa tai PIN-muutoksia.",
    # 16
    "Näytteenä prostatektomiaresekaatti, josta tehty kuusi makroleikettä ja normaalit mikroskooppileikkeet. Sekä apexista että basiksesta otetuista leikkeistä löytyy adenokarsinoomaa. Apexin pitkittäinen leike näyttää mikroksooppisesti rauhasten yhteensulautumista sopien parhaiten Gleason 4+4 luokkaan, kun taas basiksessa lähinnä luokkaa 3+4. Näiden malignien näytteiden fokusten koot n. 8mm ja 5mm. Ei kuitenkaan havaita kapselista uloskasvua, ja marginaalit ovat puhtaat.",
    # 17
    "Tutkittavana purkillinen prostatan paksuneulanäytteitä molemmilta puolilta, joista vasemman puolen fragmentit pituudeltaan 10 ja 7mm ja oikean puolen 15 ja 10mm. Kroonista tulehdusta nähdään systemaattisesti. Vasemman puolen fragmenteissa näkyy lähinnä matalalle erilaistunutta karsinoomasolukkoa, josta Gleason kasvutapaa 3 pääsääntöisesti ja toiseksi eniten tapaa 4. Lisäksi hermojen ja suonien ympärillä kasvustoa. Oikean puolen fragmentit taas eivät näytä malignilta.",
    # 18
    "Tutkittavana systeemibiopsianeulanäytteitä pituudeltaan yhteensä 4+6+3 vasemmalta ja 5+7+8mm oikealta. Näytteiden indeksoinnissa kuitenkin käynyt fiba, ja vasen on oikea ja vice versa. Korjauksen jälkeen oikean puolen ensimmäisessä ja kolmannessa näytteessä näkyy maligniin viittaavaa kasvua ja marginaalit positiivit. Vahva adenokarsinooma-suspisio siis. Näytteiden laatu kuitenkin kyseenalainen ja neulat eivät todnäk täysin edustuskelpoisia, joten suositellaan biopsiointia uudelleen ohjatusti fuusiona oikealle suspisio-alueelle.",
    # 19
    "Näytteenä on yhteensä 12.3g lastuja. Käynnistetään ne yhdellä kasetilla. Histologisessa tarkastelussa näkyy läiskittäistä kroonista tulehdusta, ja näytteistä tulee yleinen vaikutelma strooman hyperplasiasta. Mitään maligniin suoraan viittaavaa ei näy.",
    # 20
    "Tutkittavana kuusi biopsialieriötä otettuna kohonneen PSA:n takia. Pesäke 1. vasemmalta edestä, nähdään 5mm matkalla huonosti erilaistunutta atyyppista rauhasrakennetta. Kyseessä adenokarsinooma, jossa Gleason luokitus 4+4=8. Pesäke 2. vasemmalta keskeltä noin 10mm matkalla nähdään myös karsinoomakudosta, jossa Gleasonin pistesumma 4+3=7 ja graduksen 4 osuus n. 80%. Pesäkkeessä 3. oikealta keskeltä myös löydös jossa gradusten 3 ja 4 suhde n. 70:30%, joten summa 7 (3+4). Lopuissa näytteistä lähinnä epiteelissä hyperplastisia muutoksia.",
    # 21
    "Näytteinä yhteensä 4g höyläyslastuja, jotka käynnistetty kolmeen kudoskasettiin. Todetaan mikroskooppisesti suhteellisen normaalia prostatasolukkoa, jossa kuitenkin voimakasta polttoartefaktaa. Rauhaset melko tuhoutuneet polttoartefaktoista johtuen, mutta löydökset viittaisivat hienoisesti prostatahyperplasiaan.",
    # 22
    "Tutkittavana on prostatektomiapreparaatti, joka käynnistetään normaalilla kaavalla oikea lohko vihreällä ja vasen lohko keltaisella värjäten. Apex näytteisiin A-C, kaksi makroleikettä kohti basista D-E, F-G basis ja H-I kaksi näytettä seminaalivehikkeleistä. Histologiassa nähdään laaja kasvain, joka ulottuu apexista basikseen asti. Osassa apex-näytteitä ulottuu myös reunan merkattuun rajaan ja tulee pienet positiiviset reunamarginaalit. Suurin kasvainfokus on basiksen puolella, missä vallitseva Gleason luokka 3 ja luokan 4 erilaistumista melkein yhtä paljon. Ei havaita kuitenkaan kasvaimen läpikasvua kapselin ulkopuolelle.",
    # 23
    "Näyte (1) sisältää kaksi kudoslieriötä, joiden pituus 8+6mm. Pidemmässä nähdään noin 4mm pituudelta (noin puolet kokonaispituudesta) kasvainkudosta, jossa Gleason 3 -kasvutapaa 60% ja 4 -osuus n. 40%. Näyte (2) yksi 10mm, jossa kasvainkudosta n. 5mm pituudelta ja erilaistuminen Gleason 3 n. 70% ja 4-luokkaa 30%. Näyte (3) sis. 5+5mm, joissa ei havaita tavallisesta poikkeavaa prostatakudosta. Näytteissa (1) ja (2) nähdään myös PIN-muutoksia. Todetaan em. näytteistä siis Gleason 7:n prostatan adenokarsinooma.",
    # 24
    "Näytteeksi saadut prostatan elektrosektiolastut on käynnistetty kahdeksassa blokissa. Histologisessa tarkastelussa näkyy pääasiassa säännöllistä prostatakudosta, löydös siis benigni.",
    # 25
    "Näytteet 1-4: Mikroskopiassa nähdään että näytteessä nro 2 on noin 2mm kokoinen alue prostatan adenokarsinoomaa. Löydöksessä vallitsevampi Gleason on luokka 4, joskin luokka 3 on lähes yhtä suuri %. Nähdään jonkin verran siis fuusioituneita ja huonosti muodostuneita rauhasia.",
    # 26
    "Tutkittavana 12 edustavaa neulabiopsiaa prostatan tyyppipaikoista. Näytteiden yhteispituus on noin 150mm. Nähdään normaaleja rauhasrakenteita ja jonkin verran aaltoilevaa hyperplastisen kaltaista epiteeliä. Lopputulos on siis lähinnä benignin oloista kasvua. Lääk. Heikki Histopatologi",
    # 27
    "Näytteenä on edustavat prostatabiopsiat tyyppilokaatioista. Karsinoomaa löytyi seuraavasti: (1) oikean basiksen 8mm pituinen biopsia ja 7mm pituinen biopsia, joissa molemmissa Gleason 3 arkkitehtuuri pääsääntöisesti. (2) vasemmalla basiksessa 5mm myös Gleason 3 arkkitehtuurilla karsinoomalöydös. Toinen vasemman basiksen näyte puhdas. Loput näytteet myös puhtaita, joskin jonkin verran tulehdussolujen kertymää. Ei havaita tuma-atypiaa. Yhteenvetona 3/12 biopsiosta havaittu 3+3 tyypin adenokarsinoomaa.",
    # 28
    "Prostatan paksuneulabiopsianäytteet tutkittavana rutiinikaavion mukaisesti: 1 basis oikea, 2 keski oikea, 3 apex oikea, 4 basis vasen, 5 keski vasen, 6 apex vasen. Histologisesti leikkeet onnistuneita. Näytteissä 5-6 pieneltä alueelta (<1mm) nähdään Gleason 5 kasvutapaa, mutta pääosin havaitaan huonosti erilaistunutta Gleason 4+3=7 kasvua.",
    # 29
    "Tutkittavana kolme fuusiobiopsiaa prostatan suspektista fokuksesta. Yhteispituudesta 30mm nähdänä n. puolelta matkaa karsinoomafokuksia siten että pituudet noin 7, 6 ja 2mm. Näissä tason 3 graduksen kasvu promenttia kasvua, joskus jonkin verran myös Gleaosn 4 -tyypin silmukoituvaa rakenneta noin kolmasosalta karsinooman pituudelta. Yhteenvetona löydös score 7 yhteensä 15mm matkalta, jossa 3 arkkitehtuuri n. 2/3 ja 4 arkkitehtuuri n. 1/3 karsinooman osasta."
]
# Automatically translated version of the Finnish statements to examine effect of a mid-pipe translation step
inputs_eng = [
    # 30 (0 - translated)
    "A representative sample of prostate type sites, with a total length of 100mm, is being investigated. A perineural growth is observed, suspicious for malignancy. Moderate inflammatory changes, but no clear malignant or PIN findings.",
    # 31 (1 - translated)
    "Six formalin-fixed preparations. A-D shows independent growth as glands, but C a small area of glandular fusion. E-F, the majority of growth is seen in Gleason class 3 (about 60%), the rest in class 4, so 3+4=7. These samples from the left lobe. However, the margins are clean, and there is no vesicle or perineural invasion.",
    # 32 (2 - translated)
    "Samples of 3 prostatic core needle biopsies, representative of sample sites. The total length of the samples is 90mm. Inflammatory changes are visible, but no atypia or findings suggestive of malignancy. One of the samples contains some stroma (fibromuscular), and glandular structures, which would perhaps indicate hyperplasia. However, in the preliminary information it was written that the value of PSA was 600, could it have been a typing error?",
    # 33 (3 - translated)
    "As samples, thick-needle biopsies of the prostate taken from the type sites, total length on the right about 60mm and on the left about 80mm. A carcinoma is found in sample B, which already goes to Gleason level 5 and the total Gleason level is 9 (4+5). The change in question is about 20% on the left. In other samples, normal glandular structure and no significant inflammation. According to the WHO classification, grade 3.",
    # 34 (4 - translated)
    "Prostate biopsies taken according to the normal method in cassettes, total length approx. 150mm. In sample 1B, a focus jumps out from the right base, with small glandular structures, where nuclear atypia and the morphological findings correspond to adenocarcinoma, but it is so scarce that it remains at the stage of suspension. In other samples, normal glandular tissue. /Lauri Lääkäri, Meilahti, 1 January 2021",
    # 35 (5 - translated)
    "A total of about 5g of prostate shavings from the front came to view, all of which have been reviewed. The patient had previously been suspected due to an elevated PSA. Looking through the scope, adenocarcinoma is seen in almost all of them, the most representative being Gleason 4 and its various variants, so the total score is 8. The finding therefore confirms the previous suspicion.",
    # 36 (6 - translated)
    "A prostatectomy preparation that has been tested, which is run on cassettes according to the normal formula. Apex in specimens D-G, base in specimens K-P, seminal vesicles O-Q. In the first section, some tumor can already be seen peripherally, and the tumor near the edge of the capsule. Overgrowth is not seen and pos. edge margins. Basis and seminal vehicles clean. The tumors found are Gleason level 7 carcinoma, of which a larger proportion with a score of 3, approx. 60% of the findings.",
    # 37 (7 - translated)
    "As samples, 6 representative prostate biopsies from the type sites, approx. 120mm in total. The glasses show basal cell hyperplasia in places in the prostate tissue. In immunostaining samples 3-4, the basal cells are limited and the stainings are positive, but the focus is so small that a definite cancer diagnosis cannot be given. Conclusion: Suspicio finding on biopsies, but diagnosis uncertain.",
    # 38 (8 - translated)
    "About 30g of planing chips came in total, of which about 20g were started in six blocks. A histological examination reveals benign prostate tissue, where no atypia, malignancy, or carcinoma is visible. Little visible spotty inflammation. The finding is therefore suitable for suspected benign hyperplasia.",
    # 39 (9 - translated)
    "A total of 13g of planing chips were driven with eight cassettes. Carcinoma was found histologically in blocks F & G, whose growth pattern was Gleason 3+3=6.",
    # 40 (10 - translated)
    "Let's run the prostatectomy preparation according to the normal formula, s.e. right block dyed with green and left with yellow dye. Samples A-D from base to apex as macrosections, and apex as samples E-F and base G-N, and the remaining seminal vesicles from both sides N-O. Several clear foci can be seen in the macro sections, where the prevailing Gleason class is 4 and there is also some class 3. Most of the findings are in the base, but the apex and seminal vesicles are clean. Perineural invasion is abundantly observed, and the tumor clearly infiltrates through the capsule into the fat.",
    # 41 (11 - translated)
    "To be examined, thick needle samples of the prostate according to the routine chart, with about 180mm of material. A total of 13 biopsies; in samples 4, 6) carcinoma was found in a total of five biopsies, in which a larger proportion of the separate gland-forming class than class 3 and a smaller proportion of 4 (the latter accounted for about 30% of the tumor found).",
    # 42 (12 - translated)
    "The shavings obtained from planing were cut into 12 tissue blocks. Carcinoma is seen in a small part of the chips. Growth mainly of independent glandular structure and there is also growth of glands, but the proportion of carcinoma remains small (less than 5%). In the portion that can be interpreted as neoplastic, Gleason sum is 7, of which the larger portion is class 3, about 60% of the tumor.",
    # 43 (13 - translated)
    "About 19g of prostate shavings in total, of which 10g were put into histology. A lot of fibromuscular stroma and a carpet-like malignant growth in the stroma are seen. The nuclei are enlarged, vary in size and the nuclear grains are clearly distinguished. About half of the surface area of the chips is tumor tissue, with the highest level 5 and the second highest level 4 in the Gleason classification.",
    # 44 (14 - translated)
    "As samples, targeted prostate biopsies from different sides. In the sample 1) 10mm, 2) 8mm, 3) 14mm and 4) 14mm material. Sample 1 unrepresentative, samples 2 and 3 represent healthy prostate tissue. In sample 4, adenocarcinoma is seen along the entire length of the cylinder, a larger proportion forming glandular structures (Gleason 3, about 90%) and a smaller proportion forming glands (Gleason 4, 10%). Capsule overgrowth or perineural invasion are not seen in the samples.",
    # 45 (15 - translated)
    "Samples 1-6 are prostate biopsies from the type sites. The biopsy cylinders of sample 3 are not representative, as no prostate tissue can be seen. Otherwise, the samples are representative and benign prostate tissue is seen. No significant atypia is observed in the gland epithelia either. Therefore, no carcinoma or PIN changes are found in the samples.",
    # 46 (16 - translated)
    "As a sample, a prostatectomy resect, from which six macrosections and normal microscopic sections were made. Adenocarcinoma is found in sections taken from both the apex and the base. The longitudinal section of the apex microscopically shows the fusion of the glands, best suited to the Gleason 4+4 class, while in the base it is mostly class 3+4. The sizes of the foci of these malignant samples are approx. 8mm and 5mm. However, there is no outgrowth from the capsule, and the margins are clean.",
    # 47 (17 - translated)
    "For examination, a jar of thick-needle samples of the prostate from both sides, of which the fragments of the left side are 10 and 7 mm in length and the right side 15 and 10 mm. Chronic inflammation is seen systematically. In the fragments on the left side, you can see mostly low-differentiated carcinoma cells, of which Gleason growth type 3 is the main rule, and type 4 is the second most common. In addition, growth around nerves and vessels. The fragments on the right side, on the other hand, do not look malignant.",
    # 48 (18 - translated)
    "Systemic biopsy needle samples with a total length of 4+6+3 from the left and 5+7+8mm from the right are being examined. However, there was a fiba in the indexing of the samples, and the left is the right and vice versa. After correction, the first and third samples on the right side show malignant growth and positive margins. A strong adenocarcinoma suspicion, then. However, the quality of the samples is questionable and the needles are probably not fully representative, so it is recommended to re-biopsy as a guided fusion to the right suspension area.",
    # 49 (19 - translated)
    "The sample contains a total of 12.3g chips. Let's start them with one cartridge. Histological examination shows patchy chronic inflammation, and the specimens show a general impression of stromal hyperplasia. Nothing directly suggestive of malignancy is visible.",
    # 50 (20 - translated)
    "Six biopsy specimens were taken for examination due to elevated PSA. Colony 1. from the left front, a poorly differentiated atypical glandular structure can be seen 5mm away. It is an adenocarcinoma with a Gleason classification of 4+4=8. Colony 2. about 10mm from the left center can also be seen from carcinoma tissue, with a Gleason score of 4+3=7 and the proportion of grade 4 approx. 80%. In the colony 3rd from the right center also a find where the ratio of grades 3 and 4 is approx. 70:30%, so the sum is 7 (3+4). In the rest of the samples, mainly hyperplastic changes in the epithelium.",
    # 51 (21 - translated)
    "As samples, a total of 4g of planing chips, which were launched into three tissue cassettes. Microscopically, a relatively normal prostate cell is found, but with a strong burning artifact. Glands quite destroyed due to combustion artifacts, but the findings would suggest subtly prostatic hyperplasia.",
    # 52 (22 - translated)
    "The prostatectomy preparation is being investigated, which is started with the normal formula, coloring the right lobe with green and the left lobe with yellow. Apex to samples A-C, two macrosections per base D-E, F-G base and H-I two samples from seminal vesicles. Histology shows a large tumor that extends from the apex to the base. In some of the apex samples, it also extends to the marked border of the edge and there are small positive edge margins. The largest tumor focus is on the side of the base, where the prevailing Gleason grade 3 and grade 4 differentiation is almost equal. However, no growth of the tumor outside the capsule is observed.",
    # 53 (23 - translated)
    "Sample (1) contains two tissue cylinders with a length of 8+6mm. The longer one shows about 4mm of tumor tissue (about half of the total length) with Gleason 3 growth pattern 60% and 4 proportion approx. 40%. Sample (2) one 10mm, with tumor tissue approx. 5mm long and differentiation Gleason 3 approx. 70% and grade 4 30%. Sample (3) incl. 5+5mm, where no unusual prostate tissue is observed. Samples (1) and (2) also show PIN changes. We can confirm that Gleason 7 adenocarcinoma of the prostate is found in the aforementioned samples.",
    # 54 (24 - translated)
    "The sampled prostate electrosection chips have been started in eight blocks. The histological examination shows mainly regular prostate tissue, so the finding is benign.",
    # 55 (25 - translated)
    "Samples 1-4: Microscopy shows that in sample no. 2 there is an approximately 2mm area of adenocarcinoma of the prostate. The most prevalent Gleason in the finding is grade 4, although grade 3 is almost as large a %. So we see somewhat fused and poorly formed glands.",
    # 56 (26 - translated)
    "12 representative needle biopsies from prostate type sites under study. The total length of the samples is about 150 mm. Normal glandular structures and some undulating hyperplastic-like epithelium are seen. So the end result is mostly benign growth. medicine Heikki Histopathologist",
    # 57 (27 - translated)
    "The sample is representative prostate biopsies from type locations. Carcinoma was found as follows: (1) an 8mm long biopsy and a 7mm long biopsy of the right base, both with Gleason 3 architecture as a rule. (2) in the left base, 5 mm also with Gleason 3 architecture, carcinoma finding. Another left base sample clean. The rest of the samples are also clean, although there is some accumulation of inflammatory cells. No nuclear atypia is observed. In summary, type 3+3 adenocarcinoma was found in 3/12 biopsies.",
    # 58 (28 - translated)
    "Prostate core biopsy samples to be examined according to the routine chart: 1 base right, 2 center right, 3 apex right, 4 base left, 5 center left, 6 apex left. Histologically, the sections were successful. In samples 5-6 from a small area (<1mm), Gleason 5 growth patterns are seen, but mainly poorly differentiated Gleason 4+3=7 growth is observed.",
    # 59 (29 - translated)
    "Three fusion biopsies of a suspicious prostate focus are being investigated. From the total length of 30mm, seen from the side, there are carcinoma foci, so that the lengths are about 7, 6 and 2mm. In these, level 3 grade growth promotes growth, sometimes also some Gleaosn type 4 spliced structure for about one third of the length of the carcinoma. In summary, the finding is score 7 for a total distance of 15 mm, with 3 architecture approx. 2/3 and 4 architecture approx. 1/3 of the carcinoma part."
]

# Nonsensical independent gibberish statements (ought to produce e.g. NAs, test for false positives)
inputs_gib = [
    # 60 - Gibberish 0
    "Beep boop? Boop biip. Blarp!",
    # 61 - Gibberish 1
    "Lorem ipsum, 1+2=9, foo bar -0% yks kaks kolme on yhteensä kuus.",
    # 62 - Gibberish 2
    "Tämä on harhaanjohtava lause, jonka tehtävänä on testata uskoisiko kielimalli esimerkiksi löydetyn Gleason ryhmän olevan miinus sata ja että mukamas näyte painoi tuhat kiloa.",
    # 63 - Gibberish 3
    "Potilas saapuu kivuliaana ensiapuun, selkeä olkapään luksaatio lateraalisesti polkapyöräonnettomuudesta johtuen. Jonkin verran spontaania lihasspasmia, ja potilas selkeän kivulias. Tilataan akuutti röntgen mahdollisten murtumien arvioimiseksi, mutta kuvissa ei näy poikkeavaa. Yritetään luksaation korjaamista rentouttamalla ja rotatoimalla kättä, mutta siinä onnistumatta. Lopulta kipulääkkeiden avulla olkapää saadaan paikoilleen ja potilas jaa osastolle tarkkailtavaksi.",
    #
    "SYNTAX ERROR IN SQL QUERY; ERROR CODE 123 - Query parameters {sample_count, sample_amount, gleason_grade, patient_bph, sample_perineural_invasion, sample_atypia} not found - double check column names and queried MAIN_TABLE. RETURN*"
]

# Language agnostic prompt construction
def getPrompt(promptIndex, inputIndex):
    return pre[promptIndex] + (inputs_fin + inputs_eng + inputs_gib)[inputIndex] + post[promptIndex]

# Language sensitive prompt construction
def getFullPrompt(promptIndex, inputIndex):
    if promptIndex in getFinPrompts():
        return pre[promptIndex] + (inputs_fin + inputs_gib)[inputIndex] + post[promptIndex]
    elif promptIndex in getEngPrompts():
        return pre[promptIndex] + (inputs_eng + inputs_gib)[inputIndex] + post[promptIndex]

# Printable formatted illustrative prompt construction
def getPrintablePrompt(promptIndex, inputIndex):
    return pre[promptIndex] + "<INPUT STATEMENT>" + post[promptIndex]


def getInput(inputIndex):
    return (inputs_fin + inputs_eng + inputs_gib)[inputIndex]

def getMaxInputs():
    return len(inputs_fin + inputs_eng + inputs_gib)

def getMaxPrompts():
    return len(pre)

# Return indices for the Finnish prompt formulations
def getFinPrompts():
    return [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def getEngPrompts():
    return [2, 17, 18, 19]

# Return indices for the Finnish input statements
def getFinInputs():
    return list(range(0, 29))

# Return indices for the Finnish to English machine translated input statements
def getEngInputs():
    return list(range(30, 59))

# Return indices for the statements that are gibberish (and ideally should produce full sets of NA or similar)
def getGibInputs():
    return list(range(60, 62))

