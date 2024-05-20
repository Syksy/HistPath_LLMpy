# Regex
import re

# Define correct answers and allow in assessing output correctness, via e.g. regular expressions / grepping
# 30 synthetic histopathology statements originally in Finnish (machine-translated to English as well)

# Note: Syntax "(?!)" is used in regex to never be true; this is for the if-elif-else structure consistency

# Curated correct answers for grepping through returned JSON fields
# 30 prompts (with translations, tot. 60); not counting the 10 gibberish with all presumably false
rightwrong = [
    # Input 0
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavana edustava näyte prostatan tyyppipaikoista, yhteispituudelta 100mm. Havaitaan perineuraalia kasvua,
        # suspekti maligni. Kohtalaisesti tulehdusmuutoksia, mutta ei selkeää malignia tai PIN löydöstä."
        # Question 0 - Number of samples
        [["1|NA"], ["(?!)"]],
        # Question 1 - Size of samples
        [["100|100mm|100 mm"], ["(?!)"]],
        # Question 2 - Gleason score
        [["(?!)"], ["suspekti maligni"]],
        # Question 3 - Was BPH detected
        [["NA"], ["ei|no|false"]],
        # Question 4 - Was perineural growth detected
        [["havaitaan|kyllä|yes|true"], ["ei|no|false"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["ei|no|false|kyllä"]]
    ],
    # Input 1
    [
        # [Correct answers grep], [False answers grep]
        # "Kuusi formaliinifiksoitua preparaattia. A-D nähdään itsenäistä kasvua rauhasina, mutta C pieni alue
        # rauhasten yhteensulautumista. E-F nähdään valtaosa kasvusta Gleason-luokkaa 3 (noin 60%), loput luokkaa 4,
        # siis 3+4=7. Nämä näytteet vasemmasta lohkosta. Marginaalit kuitenkin puhtaat, eikä vesikkeli-
        # tai perineuraali-invaasiota."
        # Question 0 - Number of samples
        [["6|kuusi|six"], ["NA"]],
        # Question 1 - Size of samples
        [["NA|ei saatavilla|ei mainittu"], ["formaliinifiksoitua|formaliinifiksoitu|formalin-fixed|small"]],
        # Question 2 - Gleason score
        [["7|3\\+4=7|7 \\(3\\+4\\)|\\(3\\+4=7\\)"], [""]],
        # Question 3 - Was BPH detected
        [["ei|ei mainittu|NA"], ["kyllä|yes|true"]],
        # Question 4 - Was perineural growth detected
        [["ei|no|false"], [""]],
        # Question 5 - Is atypia present in the sample
        [["ei|ei mainittu|no|false|NA"], ["kyllä|yes|true"]]
    ],
    # Input 2
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteitä 3 prostatan paksuneulabiopsioita, edustavia näytekohdista. Näytteiden yhteispituus 90mm.
        # Näkyy tulehdusmuutoksia, mutta ei atypiaa tai maligniin viittavia löydöksiä. Yksi näytteistä sisältää jonkin
        # verran stroomaa (fibromuskulaari), ja rauhasrakenteita, mikä ehkä viittaisi hyperplasiaan. Esitiedoissa
        # kuitenkin luki PSA:n arvon olleen 600, mahtoiko olla näppäilyvirhe?"
        # Question 0 - Number of samples
        [["3|kolme|three"], [""]],
        # Question 1 - Size of samples
        [["90|90mm|90 mm"], [""]],
        # Question 2 - Gleason score
        [["NA"], ["(?!)"]],
        # Question 3 - Was BPH detected
        [["kyllä|yes|true|NA|mahdol|ehkä"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["no|ei|false|yes|kyllä|true"]],
        # Question 5 - Is atypia present in the sample
        [["ei|no|false"], ["kyllä|yes|true|NA"]]
    ],
    # Input 3
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteinä prostatan paksuneulabiopsioita tyyppipaikoista otettuna, yhteispituus oikealta noin 60mm ja
        # vasemmalta noin 80mm. Näytteestä B havaitaan karsinoomaa, joka menee jo Gleason tasolle 5 ja kokonais
        # Gleason taso on 9 (4+5). Kyseistä muutosta noin 20% vasemmalla. Muissa näytteissä normaalia rauhasrakennetta,
        # eikä merkittävää tulehdusta. WHO-luokituksen mukaan gradus 3."
        # Question 0 - Number of samples
        [["useita|NA|multiple"], ["2|koko elin"]],
        # Question 1 - Size of samples
        [["60mm ja 80mm|noin 60mm ja vasemmalta noin 80mm|140mm|60|80"], ["(?!)"]],
        # Question 2 - Gleason score
        [["9|4\\+5=9"], ["NA"]],
        # Question 3 - Was BPH detected
        [["NA|ei"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["kyllä|yes|true"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 4
    [
        # [Correct answers grep], [False answers grep]
        # "Kaseteissa normaalin tavan mukaan otetut prostatabiopsioat, kokonaispituus n. 150mm. Näytteesssä 1B
        # oikeasta basiksesta hyppää esiin fokus, jossa pieniä rauhasrakenteita, missä tuma-atypiaa ja morfologinen
        # löydös vastaisi adenokarsinoomaa, mutta on niin niukka että jää suspisio-asteelle. Muissa näytteissä normaalia
        # rauhaskudosta. /Lauri Lääkäri, Meilahti, 1.1.2021"
        # Question 0 - Number of samples
        [["usea|multiple|NA"], ["1"]],
        # Question 1 - Size of samples
        [["150|150mm|150 mm"], [""]],
        # Question 2 - Gleason score
        [["(?!)"], ["3\\+3"]],
        # Question 3 - Was BPH detected
        [["ei|no|false|NA"], ["kyllä|yes|true"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["kyllä|yes|true"], ["ei|no|false"]]
    ],
    # Input 5
    [
        # [Correct answers grep], [False answers grep]
        # "Katsottavaksi tullut yhteensä noin 5g edestä prostatan höylälastuja, joista kaikki käyty läpi. Potilas
        # ollut suspekti aiemmin kohonneen PSA:n takia. Skoopilla katsoen lähes kaikissa nähdään adenokarsinoomaa,
        # edustavin Gleason 4:ää ja sen eri variantteja joten pistesumma 8. Löydös siis vahvistaa aiemman suspision."
        # Question 0 - Number of samples
        [["NA"], ["1"]],
        # Question 1 - Size of samples
        [["5|5g|5 g"], ["(?!)"]],
        # Question 2 - Gleason score
        [["8|4\\+4=8|pistesumma 8"], ["4|4\\+\\?=\\?8"]],
        # Question 3 - Was BPH detected
        [["NA|ei|no|false"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 6
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavaksi tullut prostatektomia-preparaatti, joka ajetaan kaseteilla normaalikaavan mukaan. Näytteissä
        # D-G apexia, basis näytteissä K-P, seminaalivehikkeleitä O-Q. Ensimmäisessä leikkeessä havaitaan jo jonkin
        # verran kasvainta perifeerisesti, ja tuumori lähellä kapselin reunaa. Läpikasvua ei nähdä eikä pos.
        # reunamarginaaleja. Basis ja seminaalivehikkelit puhtaat. Löydetyt tuumorit Gleason 7-tasoista karsinoomaa,
        # josta isompi osuus scoorauksella 3 n. 60% löydöksissä."
        # Question 0 - Number of samples
        [["^1$|koko elin|17|seitsemäntoista|14|neljätoista|seventeen|fourteen|whole organ"], [""]],
        # Question 1 - Size of samples
        [["NA"], ["(?!)"]],
        # Question 2 - Gleason score
        [["^7$|3\\+4=7|7\\/3\\+4|7 \\(3\\+4\\)"], ["7\\+3=10"]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["Ei mainintaa|ei ole mainittu"], ["(?!)"]]
    ],
    # Input 7
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteinä 6 kpl edustavia prostatabiopsioita tyyppipaikoista, yhteensä n. 120mm. Laseilla nähdään
        # prostatakudoksessa paikoin basaalisoluhyperplasiaa. Immunovärjäyksissä näytteissä 3-4 basaalisolut
        # rajoittuneet ja värjäykset positiivisia, mutta fokus niin pieni että ei voida varmaa syöpädiagnoosia antaa.
        # Johtopäätös: Suspicio-löydös biopsioista, mutta diagnoosi epävarma."
        # Question 0 - Number of samples
        [["6|kuusi|six"], [""]],
        # Question 1 - Size of samples
        [["120|120mm|120 mm"], [""]],
        # Question 2 - Gleason score
        [["NA"], ["(?!)"]],
        # Question 3 - Was BPH detected
        [["kyllä|yes|true|hyperplasiaa"], ["ei|no|false"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["kyllä|yes|true"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 8
    [
        # [Correct answers grep], [False answers grep]
        # "Höyläyslastuja tuli yhteensä noin 30g, joista noin 20g käynnistettiin kuudessa blokissa. Histologisessa
        # tarkastelussa havaitaan hyvänlaatuista prostatakudosta, missä ei atypiaa, malignia, tai karsinoomaa näy.
        # Vähän nähtävissä läiskittäistä tulehdusta. Löydös sopii siis epäiltyyn hyvänlaatuiseen hyperplasiaan."
        # Question 0 - Number of samples
        [["6|kuusi|six"], ["(?!)"]],
        # Question 1 - Size of samples
        [["30|20|30 g|20 g"], ["(?!)"]],
        # Question 2 - Gleason score
        [["NA|ei mainintaa"], ["(?!)"]],
        # Question 3 - Was BPH detected
        [["kyllä|yes|true"], ["ei|no|false"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei|no|false"], ["kyllä|yes|true"]],
        # Question 5 - Is atypia present in the sample
        [["ei|no|false"], ["kyllä|yes|true"]]
    ],
    # Input 9
    [
        # [Correct answers grep], [False answers grep]
        # "Yhteensä 13g edestä höyläyslastuja ajettiin kahdeksalla kasetilla. Karsinoomaa todettiin histologisesti
        # blokeissa F & G, joiden kasvutapa oli Gleason 3+3=6."
        # Question 0 - Number of samples
        [["8|kahdeksan|eight"], ["(?!)"]],
        # Question 1 - Size of samples
        [["13|13g|13 g"], [""]],
        # Question 2 - Gleason score
        [["6|3\\+3=6|6 \\(3\\+3\\)|^3\\+3$"], ["(?!)"]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 10
    [
        # [Correct answers grep], [False answers grep]
        # "Ajetaan prostatetomiapreparaatti normaalin kaavan mukaan, s.e. oikea lohko värjätty vihreällä ja vasen
        # keltaisella väriaineella. Näytteet A-D basiksesta apexiin päin makroleikkeinä, ja apex näytteinä E-F ja
        # basis G-N, ja loput seminaalivesikkelit molemmilta puolilta N-O. Nähdään makroleikkeissä useampi selkeä
        # fokus, joissa vallitseva Gleason luokka on 4 ja mukana myös jonkin verran luokkaa 3. Pääosa löydöksistä
        # basiksessa, mutta apex ja seminaalivesikkelit puhtaat. Perineuraalista invaasiota havaitaan runsaasti, ja
        # kasvain infiltroi selvästi kapselin läpi rasvaan."
        # Question 0 - Number of samples
        [["15|viisitoista|fifteen"], [""]],
        # Question 1 - Size of samples
        [["NA"], ["(?!)"]],
        # Question 2 - Gleason score
        [["4\\+3=7|"], ["^4$|^3$"]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["kyllä|yes|true"], ["ei|no|false"]],
        # Question 5 - Is atypia present in the sample
        [["NA|ei mainintaa"], ["kyllä|yes|true"]]
    ],
    # Input 11
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavana prostatan paksuneulanäytteitä rutiinikaavion mukaisesti, jossa materiaalia noin 180mm.
        # Biopsioita yhteensä 13 kpl; näytteissä 4, 6) havaittiin karsinoomaa yhteensä viidessä biopsiossa, joissa
        # erillisiä rauhasia muodostavan luokan isompi osuus luokkaa 3 ja pienempi osuus 4 (jälkimmäisen osuus noin
        # 30% löydetystä tuumorista)."
        # Question 0 - Number of samples
        [["13|kolmetoist|thirteen"], ["(?!)"]],
        # Question 1 - Size of samples
        [["180|180mm|180 mm"], [""]],
        # Question 2 - Gleason score
        [["^3\\+4$|^3\\+4=7$|7 \\(3\\+4\\)"], [""]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 12
    [
        # [Correct answers grep], [False answers grep]
        # "Höyläyksestä saatuja lastuja ajettiin 12 kudosblokkia. Lastuissa pienessä osassa nähdään karsinoomaa.
        # Kasvu pääosin itsenäistä rauhasrakennetta ja mukana myös rauhasten yhteenkasvua, mutta karsinooman osuus
        # jää pieneksi (alle 5%). Neoplastiseksi tulkittavassa osuudessa Gleason summana 7, josta suuremman osuuden
        # luokka 3 noin 60% tuumorista."
        # Question 0 - Number of samples
        [["12|kaksitoist|twelve"], ["(?!)"]],
        # Question 1 - Size of samples
        [["NA|ei saatavilla"], ["pieni"]],
        # Question 2 - Gleason score
        [["^7$|^3\\+4=7$|7 \\(3\\+4"], [""]],
        # Question 3 - Was BPH detected
        [["NA|ei"], ["kyllä|yes|true"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei mainittu"], ["kyllä|yes|true"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 13
    [
        # [Correct answers grep], [False answers grep]
        # "Prostatalastuja yhteensä noin 19g, josta laitettu 10g histologiaan. Näkyy paljon fibromuskulaaria
        # stroomaa ja mattomaista pahanlaatuista kasvua stroomassa. Tumat suurentuneet, kooltaan vaihtelevat ja
        # tumajyväset erottuvat selvästi. Noin puolet lastujen pinta-alasta kasvainkudosta, jossa Gleason luokituksessa
        # eniten tasoa 5 ja toiseksi eniten tasoa 4."
        # Question 0 - Number of samples
        [["NA"], [""]],
        # Question 1 - Size of samples
        [["19g|10g|19 g|10 g|9|10"], ["(?!)"]],
        # Question 2 - Gleason score
        [["^5\\+4=9$|^9$|^5\\+4$"], ["^5$"]],
        # Question 3 - Was BPH detected
        [["NA|ei|no|false"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei|no|false"], ["kyllä|yes|true"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 14
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteinä kohdennetut prostatabiopsiat eri puolilta. Näytteessä 1) 10mm, 2) 8mm, 3) 14mm ja 4) 14mm
        # materiaalia. Näyte 1 epäedustava, näytteet 2 ja 3 edustavat tervettä prostatakudosta. Näytteessä 4 nähdään
        # koko lieriön pituudelta adenokarsinoomaa, isompi osuus rauhasrakenteita muodostaen (Gleason 3, noin 90%) ja
        # pienempi osuus rauhasten yhteensulautumista (Gleason 4, 10%). Kapselin läpikasvua tai perineuraalista
        # invaasiota ei näytteissä nähdä."
        # Question 0 - Number of samples
        [["4|four|neljä"], [""]],
        # Question 1 - Size of samples
        [["14mm"], ["(?!)"]],
        # Question 2 - Gleason score
        [["3\\+4=7|^7$"], [""]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["ei|no|false"], ["kyllä|yes|true"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 15
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteenä 1-6 prostatabiopsiat tyyppipaikoista. Näytteen 3 biopsiasylinterit eivät edustavia, sillä
        # siinä ei nähdä prostatakudosta. Muutoin näytteet ovat edustavat ja nähdään benigniä prostatakudosta.
        # Rauhasepiteeleissä ei myöskään havaita merkittävää atypiaa. Näytteistä ei siis löydetä karsinoomaa
        # tai PIN-muutoksia."
        # Question 0 - Number of samples
        [["6|kuusi|six"], [""]],
        # Question 1 - Size of samples
        [["NA"], ["(?!)"]],
        # Question 2 - Gleason score
        [["NA|Ei saatavil|Ei löydetty|Ei karsin"], [""]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["ei|no|false"], [""]]
    ],
    # Input 16
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteenä prostatektomiaresekaatti, josta tehty kuusi makroleikettä ja normaalit mikroskooppileikkeet.
        # Sekä apexista että basiksesta otetuista leikkeistä löytyy adenokarsinoomaa. Apexin pitkittäinen leike
        # näyttää mikroksooppisesti rauhasten yhteensulautumista sopien parhaiten Gleason 4+4 luokkaan, kun taas
        # basiksessa lähinnä luokkaa 3+4. Näiden malignien näytteiden fokusten koot n. 8mm ja 5mm. Ei kuitenkaan
        # havaita kapselista uloskasvua, ja marginaalit ovat puhtaat."
        # Question 0 - Number of samples
        [["6|koko elin|kuusi|1|one|whole organ"], [""]],
        # Question 1 - Size of samples
        [["8mm|8|8 mm"], [""]],
        # Question 2 - Gleason score
        [["^4\\+4|^4\\+4=8|8"], [""]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA|ei havaittu|ei mainittu"], ["(?!)"]]
    ],
    # Input 17
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavana purkillinen prostatan paksuneulanäytteitä molemmilta puolilta, joista vasemman puolen
        # fragmentit pituudeltaan 10 ja 7mm ja oikean puolen 15 ja 10mm. Kroonista tulehdusta nähdään systemaattisesti.
        # Vasemman puolen fragmenteissa näkyy lähinnä matalalle erilaistunutta karsinoomasolukkoa, josta Gleason
        # kasvutapaa 3 pääsääntöisesti ja toiseksi eniten tapaa 4. Lisäksi hermojen ja suonien ympärillä kasvustoa.
        # Oikean puolen fragmentit taas eivät näytä malignilta."
        # Question 0 - Number of samples
        [["4|neljä|four"], [""]],
        # Question 1 - Size of samples
        [["10|7|15|10"], [""]],
        # Question 2 - Gleason score
        [["^3\\+4=7|^3+4$"], [""]],
        # Question 3 - Was BPH detected
        [["NA|ei mainittu"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["kyllä|yes|true"], ["NA|ei|no|false"]],
        # Question 5 - Is atypia present in the sample
        [["NA|ei mainittu"], ["(?!)"]]
    ],
    # Input 18
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavana systeemibiopsianeulanäytteitä pituudeltaan yhteensä 4+6+3 vasemmalta ja 5+7+8mm oikealta.
        # Näytteiden indeksoinnissa kuitenkin käynyt fiba, ja vasen on oikea ja vice versa. Korjauksen jälkeen oikean
        # puolen ensimmäisessä ja kolmannessa näytteessä näkyy maligniin viittaavaa kasvua ja marginaalit positiivit.
        # Vahva adenokarsinooma-suspisio siis. Näytteiden laatu kuitenkin kyseenalainen ja neulat eivät todnäk täysin
        # edustuskelpoisia, joten suositellaan biopsiointia uudelleen ohjatusti fuusiona oikealle suspisio-alueelle."
        # Question 0 - Number of samples
        [["^6$|kuusi|six"], [""]],
        # Question 1 - Size of samples
        [["4\\+6\\+3|5\\+7\\+8|13|20|33"], ["(?!)"]],
        # Question 2 - Gleason score
        [["NA"], ["^4\\+3=7$|^4\\+6=10$|^4\\3=7|3\\+4=7$"]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 19
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteenä on yhteensä 12.3g lastuja. Käynnistetään ne yhdellä kasetilla. Histologisessa tarkastelussa näkyy
        # läiskittäistä kroonista tulehdusta, ja näytteistä tulee yleinen vaikutelma strooman hyperplasiasta. Mitään
        # maligniin suoraan viittaavaa ei näy"
        # Question 0 - Number of samples
        [["NA|^1$"], ["(?!)"]],
        # Question 1 - Size of samples
        [["12.3|12,3|12.3 g|12,3 g"], [""]],
        # Question 2 - Gleason score
        [["NA"], [""]],
        # Question 3 - Was BPH detected
        [["kyllä|yes|true"], ["ei|no|false|NA"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 20
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavana kuusi biopsialieriötä otettuna kohonneen PSA:n takia. Pesäke 1. vasemmalta edestä, nähdään
        # 5mm matkalla huonosti erilaistunutta atyyppista rauhasrakennetta. Kyseessä adenokarsinooma, jossa Gleason
        # luokitus 4+4=8. Pesäke 2. vasemmalta keskeltä noin 10mm matkalla nähdään myös karsinoomakudosta, jossa
        # Gleasonin pistesumma 4+3=7 ja graduksen 4 osuus n. 80%. Pesäkkeessä 3. oikealta keskeltä myös löydös jossa
        # gradusten 3 ja 4 suhde n. 70:30%, joten summa 7 (3+4). Lopuissa näytteistä lähinnä epiteelissä hyperplastisia
        # muutoksia."
        # Question 0 - Number of samples
        [["^6$|kuusi|six"], [""]],
        # Question 1 - Size of samples
        [["^5$|5mm|5 mm"], ["(?!)"]],
        # Question 2 - Gleason score
        [["^4\\+4=8$|^\\[\\'8|^\\[8"], [""]],
        # Question 3 - Was BPH detected
        [[""], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei maini"], ["kyllä|yes|true"]],
        # Question 5 - Is atypia present in the sample
        [["kyllä|yes|true"], ["NA|ei|no|false"]]
    ],
    # Input 21
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteinä yhteensä 4g höyläyslastuja, jotka käynnistetty kolmeen kudoskasettiin. Todetaan mikroskooppisesti
        # suhteellisen normaalia prostatasolukkoa, jossa kuitenkin voimakasta polttoartefaktaa. Rauhaset melko
        # tuhoutuneet polttoartefaktoista johtuen, mutta löydökset viittaisivat hienoisesti prostatahyperplasiaan."
        # Question 0 - Number of samples
        [["NA|3"], ["(?!)"]],
        # Question 1 - Size of samples
        [["4|4g|4 g"], [""]],
        # Question 2 - Gleason score
        [["NA|ei mainit"], [""]],
        # Question 3 - Was BPH detected
        [["kyllä|yes|true"], [""]],
        # Question 4 - Was perineural growth detected
        [["NA|ei|no|false"], [""]],
        # Question 5 - Is atypia present in the sample
        [["NA|ei|no|false"], [""]]
    ],
    # Input 22
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavana on prostatektomiapreparaatti, joka käynnistetään normaalilla kaavalla oikea lohko vihreällä
        # ja vasen lohko keltaisella värjäten. Apex näytteisiin A-C, kaksi makroleikettä kohti basista D-E, F-G basis
        # ja H-I kaksi näytettä seminaalivehikkeleistä. Histologiassa nähdään laaja kasvain, joka ulottuu apexista
        # basikseen asti. Osassa apex-näytteitä ulottuu myös reunan merkattuun rajaan ja tulee pienet positiiviset
        # reunamarginaalit. Suurin kasvainfokus on basiksen puolella, missä vallitseva Gleason luokka 3 ja luokan 4
        # erilaistumista melkein yhtä paljon. Ei havaita kuitenkaan kasvaimen läpikasvua kapselin ulkopuolelle."
        # Question 0 - Number of samples
        [["NA|^9$"], ["(?!)"]],
        # Question 1 - Size of samples
        [["NA|ei tiedossa|ei saatavilla"], ["(?!)"]],
        # Question 2 - Gleason score
        [["^3\\+4=7|^3\\+4$|^7$"], [""]],
        # Question 3 - Was BPH detected
        [["NA|ei mainintaa"], ["kyllä|yes|true"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei mainintaa"], ["kyllä|yes|true"]],
        # Question 5 - Is atypia present in the sample
        [["NA|ei mainintaa"], ["kyllä|yes|true"]]
    ],
    # Input 23
    [
        # [Correct answers grep], [False answers grep]
        # "Näyte (1) sisältää kaksi kudoslieriötä, joiden pituus 8+6mm. Pidemmässä nähdään noin 4mm pituudelta
        # (noin puolet kokonaispituudesta) kasvainkudosta, jossa Gleason 3 -kasvutapaa 60% ja 4 -osuus n. 40%.
        # Näyte (2) yksi 10mm, jossa kasvainkudosta n. 5mm pituudelta ja erilaistuminen Gleason 3 n. 70% ja 4-luokkaa
        # 30%. Näyte (3) sis. 5+5mm, joissa ei havaita tavallisesta poikkeavaa prostatakudosta. Näytteissa (1) ja (2)
        # nähdään myös PIN-muutoksia. Todetaan em. näytteistä siis Gleason 7:n prostatan adenokarsinooma."
        # Question 0 - Number of samples
        [["3|kolme|three"], ["(?!)"]],
        # Question 1 - Size of samples
        [["8+6mm|4mm|5mm|5+5mm"], ["(?!)"]],
        # Question 2 - Gleason score
        [["^3\\+4=7|^7$"], [""]],
        # Question 3 - Was BPH detected
        [["NA|ei tiedossa"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei mainita|ei tiedossa"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA|kyllä|PIN"], ["(?!)"]]
    ],
    # Input 24
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteeksi saadut prostatan elektrosektiolastut on käynnistetty kahdeksassa blokissa. Histologisessa
        # tarkastelussa näkyy pääasiassa säännöllistä prostatakudosta, löydös siis benigni."
        # Question 0 - Number of samples
        [["NA|8|kahdeks|eight"], ["(?!)"]],
        # Question 1 - Size of samples
        [["NA"], ["(?!)"]],
        # Question 2 - Gleason score
        [["NA|ei saatavilla"], ["(?!)"]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 25
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteet 1-4: Mikroskopiassa nähdään että näytteessä nro 2 on noin 2mm kokoinen alue prostatan
        # adenokarsinoomaa. Löydöksessä vallitsevampi Gleason on luokka 4, joskin luokka 3 on lähes yhtä suuri %.
        # Nähdään jonkin verran siis fuusioituneita ja huonosti muodostuneita rauhasia."
        # Question 0 - Number of samples
        [["4|neljä|four"], [""]],
        # Question 1 - Size of samples
        [["2|2mm|2 mm"], [""]],
        # Question 2 - Gleason score
        [["4\\+3=7|^4\\+3"], [""]],
        # Question 3 - Was BPH detected
        [["NA|ei mainittu"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei mainintaa|ei mainittu"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA|ei mainintaa|ei mainittu"], ["(?!)"]]
    ],
    # Input 26
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavana 12 edustavaa neulabiopsiaa prostatan tyyppipaikoista. Näytteiden yhteispituus on noin 150mm.
        # Nähdään normaaleja rauhasrakenteita ja jonkin verran aaltoilevaa hyperplastisen kaltaista epiteeliä.
        # Lopputulos on siis lähinnä benignin oloista kasvua. Lääk. Heikki Histopatologi"
        # Question 0 - Number of samples
        [["12|kaksitoist|twelve"], [""]],
        # Question 1 - Size of samples
        [["150|150mm|150 mm"], [""]],
        # Question 2 - Gleason score
        [["NA"], [""]],
        # Question 3 - Was BPH detected
        [["NA|kyllä|yes|true"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ],
    # Input 27
    [
        # [Correct answers grep], [False answers grep]
        # "Näytteenä on edustavat prostatabiopsiat tyyppilokaatioista. Karsinoomaa löytyi seuraavasti: (1) oikean
        # basiksen 8mm pituinen biopsia ja 7mm pituinen biopsia, joissa molemmissa Gleason 3 arkkitehtuuri
        # pääsääntöisesti. (2) vasemmalla basiksessa 5mm myös Gleason 3 arkkitehtuurilla karsinoomalöydös.
        # Toinen vasemman basiksen näyte puhdas. Loput näytteet myös puhtaita, joskin jonkin verran tulehdussolujen
        # kertymää. Ei havaita tuma-atypiaa. Yhteenvetona 3/12 biopsiosta havaittu 3+3 tyypin adenokarsinoomaa."
        # Question 0 - Number of samples
        [["^12$|kaksitoista|twelve"], ["(?!)"]],
        # Question 1 - Size of samples
        [["8mm|7mm|5mm|8 mm|7 mm|5 mm"], [""]],
        # Question 2 - Gleason score
        [["^6$|3\\+3=6|3\\+3"], ["(?!)"]],
        # Question 3 - Was BPH detected
        [["NA|ei havaittu|ei mainint"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei havaittu|ei mainint"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["ei|no|false"], [""]]
    ],
    # Input 28
    [
        # [Correct answers grep], [False answers grep]
        # "Prostatan paksuneulabiopsianäytteet tutkittavana rutiinikaavion mukaisesti: 1 basis oikea, 2 keski oikea,
        # 3 apex oikea, 4 basis vasen, 5 keski vasen, 6 apex vasen. Histologisesti leikkeet onnistuneita. Näytteissä
        # 5-6 pieneltä alueelta (<1mm) nähdään Gleason 5 kasvutapaa, mutta pääosin havaitaan huonosti erilaistunutta
        # Gleason 4+3=7 kasvua."
        # Question 0 - Number of samples
        [["^6$"], [""]],
        # Question 1 - Size of samples
        [["1mm|1 mm"], [""]],
        # Question 2 - Gleason score
        [["4\\+3=7|^7$"], [""]],
        # Question 3 - Was BPH detected
        [["NA|ei mainittu"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA|ei mainittu"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA|ei mainittu"], ["(?!)"]]
    ],
    # Input 29
    [
        # [Correct answers grep], [False answers grep]
        # "Tutkittavana kolme fuusiobiopsiaa prostatan suspektista fokuksesta. Yhteispituudesta 30mm nähdänä n.
        # puolelta matkaa karsinoomafokuksia siten että pituudet noin 7, 6 ja 2mm. Näissä tason 3 graduksen kasvu
        # promenttia kasvua, joskus jonkin verran myös Gleaosn 4 -tyypin silmukoituvaa rakenneta noin kolmasosalta
        # karsinooman pituudelta. Yhteenvetona löydös score 7 yhteensä 15mm matkalta, jossa 3 arkkitehtuuri n. 2/3
        # ja 4 arkkitehtuuri n. 1/3 karsinooman osasta."
        # Question 0 - Number of samples
        [["3|kolme|three"], [""]],
        # Question 1 - Size of samples
        [["30mm|30|30 mm"], [""]],
        # Question 2 - Gleason score
        [["^7$|3\\+4=7|score 7|gleason 7|7 \\(3\\+4\\)"], [""]],
        # Question 3 - Was BPH detected
        [["NA"], ["(?!)"]],
        # Question 4 - Was perineural growth detected
        [["NA"], ["(?!)"]],
        # Question 5 - Is atypia present in the sample
        [["NA"], ["(?!)"]]
    ]
]

# Query candidate correct and false answers and return correct (+1), false (-1), or uncertain (0)
def getRegexCorrect(answer : str, inputIndex : int, questionIndex : int) -> int:
    # Wrap the machine-translated answers (0-29 in Finnish, 30-59 are the same machine translated to English)
    if inputIndex >= 30 & inputIndex < 60:
        inputIndex -= 30
    # Gibberish inputs are always wrong if the answer is not NA
    if inputIndex >= 60 & inputIndex < 70:
        if answer == "NA":
            return 1
        else:
            return -1
    # Regex (boolean) for matching for right answers
    if bool(re.search(rightwrong[inputIndex][questionIndex][0][0], answer, re.IGNORECASE)):
        return 1
    # Regex (boolean) for matching for wrong answers
    elif bool(re.search(rightwrong[inputIndex][questionIndex][1][0], answer, re.IGNORECASE)):
        return -1
    # If we fall through the answer is ambiguous and cannot be assigned right/wrong definitely
    else:
        return 0
