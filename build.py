#!/usr/bin/env python3
"""Generate a multilingual 'Iconic Locations of the Basque Country' site (en/es/eu/fr)."""
import json, html
from urllib.parse import quote

META = json.load(open("meta.json"))

def ipath(slug):
    return META.get(slug, {}).get("path", "")

def credit(slug):
    m = META.get(slug, {})
    if not m:
        return ""
    page = "https://commons.wikimedia.org/wiki/" + quote(m.get("title", "").replace(" ", "_"))
    return (f'Photo: {html.escape(m.get("artist","Unknown"))} \u00b7 '
            f'<a href="{page}" target="_blank" rel="noopener">{html.escape(m.get("license","See source"))}</a>')

LANGS = ["en", "es", "eu", "fr"]
LANG_LABEL = {"en": "English", "es": "Espa\u00f1ol", "eu": "Euskara", "fr": "Fran\u00e7ais"}
PAGE_FILE = {"en": "index.html", "es": "es.html", "eu": "eu.html", "fr": "fr.html"}

REGION_NAMES = {
 "en": {"Bizkaia":"Bizkaia","Gipuzkoa":"Gipuzkoa","Araba":"Araba","Navarre":"Navarre","Iparralde":"Iparralde"},
 "es": {"Bizkaia":"Bizkaia","Gipuzkoa":"Gipuzkoa","Araba":"\u00c1lava","Navarre":"Navarra","Iparralde":"Iparralde"},
 "eu": {"Bizkaia":"Bizkaia","Gipuzkoa":"Gipuzkoa","Araba":"Araba","Navarre":"Nafarroa","Iparralde":"Iparralde"},
 "fr": {"Bizkaia":"Biscaye","Gipuzkoa":"Guipuscoa","Araba":"Alava","Navarre":"Navarre","Iparralde":"Iparralde"},
}
REGION_COLOR = {"Bizkaia":"#c8102e","Gipuzkoa":"#0b7a3b","Araba":"#b06a00","Navarre":"#6a2c8f","Iparralde":"#1c6ea4"}

TAGS = {
 "city":       {"en":"City","es":"Ciudad","eu":"Hiria","fr":"Ville"},
 "culture":    {"en":"Culture","es":"Cultura","eu":"Kultura","fr":"Culture"},
 "art":        {"en":"Art","es":"Arte","eu":"Artea","fr":"Art"},
 "architecture":{"en":"Architecture","es":"Arquitectura","eu":"Arkitektura","fr":"Architecture"},
 "natural":    {"en":"Natural wonder","es":"Maravilla natural","eu":"Naturaren miraria","fr":"Merveille naturelle"},
 "heritage":   {"en":"Heritage","es":"Patrimonio","eu":"Ondarea","fr":"Patrimoine"},
 "coast":      {"en":"Coast","es":"Costa","eu":"Kostaldea","fr":"C\u00f4te"},
 "surf":       {"en":"Surf","es":"Surf","eu":"Surfa","fr":"Surf"},
 "history":    {"en":"History","es":"Historia","eu":"Historia","fr":"Histoire"},
 "unesco":     {"en":"UNESCO","es":"UNESCO","eu":"UNESCO","fr":"UNESCO"},
 "engineering":{"en":"Engineering","es":"Ingenier\u00eda","eu":"Ingeniaritza","fr":"Ing\u00e9nierie"},
 "nature":     {"en":"Nature","es":"Naturaleza","eu":"Natura","fr":"Nature"},
 "food":       {"en":"Food","es":"Gastronom\u00eda","eu":"Gastronomia","fr":"Gastronomie"},
 "geology":    {"en":"Geology","es":"Geolog\u00eda","eu":"Geologia","fr":"G\u00e9ologie"},
 "town":       {"en":"Town","es":"Villa","eu":"Herria","fr":"Bourg"},
 "green":      {"en":"Green","es":"Verde","eu":"Berdea","fr":"Vert"},
 "wine":       {"en":"Wine country","es":"Tierra del vino","eu":"Ardoaren lurra","fr":"Pays du vin"},
 "festival":   {"en":"Festival","es":"Fiesta","eu":"Jaia","fr":"F\u00eate"},
 "camino":     {"en":"Camino","es":"Camino","eu":"Bidea","fr":"Chemin"},
 "village":    {"en":"Village","es":"Aldea","eu":"Herrixka","fr":"Village"},
 "legend":     {"en":"Legend","es":"Leyenda","eu":"Kondaira","fr":"L\u00e9gende"},
 "mountain":   {"en":"Mountain","es":"Monta\u00f1a","eu":"Mendia","fr":"Montagne"},
 "spiritual":  {"en":"Spiritual","es":"Espiritual","eu":"Izpirituala","fr":"Spirituel"},
}

LOCATIONS = [
 dict(slug="bilbao", region="Bizkaia", tags=["city","culture"], i18n={
   "en":("Bilbao","Bilbo","The largest city in the Basque Country and its cultural engine. Once a gritty industrial port, Bilbao reinvented itself as a capital of design and art, with a walkable Casco Viejo, a celebrated food scene and riverside promenades that draw you toward the Guggenheim."),
   "es":("Bilbao","Bilbo","La ciudad m\u00e1s grande del Pa\u00eds Vasco y su motor cultural. Antiguo puerto industrial, Bilbao se reinvent\u00f3 como capital del dise\u00f1o y del arte, con un Casco Viejo peatonal, una c\u00e9lebre escena gastron\u00f3mica y paseos junto a la r\u00eda que conducen al Guggenheim."),
   "eu":("Bilbo","Bilbao","Euskal Herriko hiri handiena eta kultura-motorra. Industriako portu zaharra izandakoa, Bilbo diseinuaren eta artearen hiriburu bihurtu zen berriz: Alde Zaharra oinez ibiltzekoa, gastronomia-eszena ospetsua eta Guggenheimera daramaten ibaiko pasealekuak."),
   "fr":("Bilbao","Bilbo","La plus grande ville du Pays basque et son moteur culturel. Ancien port industriel, Bilbao s'est r\u00e9invent\u00e9e en capitale du design et de l'art, avec un Casco Viejo pi\u00e9ton, une sc\u00e8ne gastronomique r\u00e9put\u00e9e et des promenades le long de la ria qui m\u00e8nent au Guggenheim.")}),
 dict(slug="guggenheim", region="Bizkaia", tags=["art","architecture"], i18n={
   "en":("Guggenheim Museum Bilbao","Guggenheim Bilbao Museoa","Frank Gehry's titanium masterpiece, opened in 1997, turned a fading shipbuilding city into a global destination. Its shimmering, ship-like curves \u2014 guarded by Jeff Koons's giant \u201cPuppy\u201d \u2014 are the emblem of Bilbao's rebirth."),
   "es":("Museo Guggenheim Bilbao","Guggenheim Bilbao Museoa","La obra maestra de titanio de Frank Gehry, inaugurada en 1997, convirti\u00f3 una ciudad naval en decadencia en un destino mundial. Sus curvas brillantes, semejantes a un barco y custodiadas por el gigantesco \u00abPuppy\u00bb de Jeff Koons, son el emblema del renacer de Bilbao."),
   "eu":("Guggenheim Bilbao Museoa","Guggenheim Museoa","Frank Gehryren titaniozko maisulana, 1997an inauguratua, gainbeheran zegoen itsasontzi-hiri bat munduko helmuga bihurtu zuen. Itsasontzi baten antzeko kurba distiratsuak, Jeff Koonsen \u00abPuppy\u00bb erraldoiak zaintzen dituenak, Bilboren berpizkundearen ikurra dira."),
   "fr":("Mus\u00e9e Guggenheim Bilbao","Guggenheim Bilbao Museoa","Le chef-d'\u0153uvre de titane de Frank Gehry, inaugur\u00e9 en 1997, a transform\u00e9 une ville portuaire en d\u00e9clin en destination mondiale. Ses courbes scintillantes, semblables \u00e0 un navire et gard\u00e9es par l'immense \u00ab Puppy \u00bb de Jeff Koons, symbolisent la renaissance de Bilbao.")}),
 dict(slug="gaztelugatxe", region="Bizkaia", tags=["natural","heritage"], i18n={
   "en":("San Juan de Gaztelugatxe","Gaztelugatxe","A stone hermitage perched on a tiny islet, reached by a winding stone bridge and 241 steps. Famous worldwide as \u201cDragonstone\u201d in Game of Thrones, it is the most dramatic spot on the Biscay coast."),
   "es":("San Juan de Gaztelugatxe","Gaztelugatxe","Una ermita de piedra encaramada a un peque\u00f1o islote, a la que se llega por un puente sinuoso y 241 escalones. Famosa en todo el mundo como \u00abDragonstone\u00bb en Juego de Tronos, es el rinc\u00f3n m\u00e1s espectacular de la costa de Bizkaia."),
   "eu":("San Juan de Gaztelugatxe","Gaztelugatxe","Uhartetxo batean kokatutako harrizko ermita, harrizko zubi bihurri bat eta 241 eskailera igarota iristen dena. Mundu osoan ezaguna Game of Thrones telesaileko \u00abDragonstone\u00bb gisa, Bizkaiko kostaldeko txokorik ikusgarriena da."),
   "fr":("San Juan de Gaztelugatxe","Gaztelugatxe","Une chapelle de pierre perch\u00e9e sur un \u00eelot, accessible par un pont de pierre sinueux et 241 marches. Mondialement connue comme \u00ab Dragonstone \u00bb dans Game of Thrones, c'est le site le plus spectaculaire de la c\u00f4te de Biscaye.")}),
 dict(slug="mundaka", region="Bizkaia", tags=["coast","surf"], i18n={
   "en":("Mundaka","Mundaka","A picture-postcard fishing village at the mouth of the Urdaibai estuary, home to one of Europe's most famous left-hand waves. Whitewashed houses and the little Santa Catalina chapel overlook the water."),
   "es":("Mundaka","Mundaka","Un pueblo pesquero de postal en la desembocadura de la r\u00eda de Urdaibai, hogar de una de las olas izquierdas m\u00e1s famosas de Europa. Las casas encaladas y la peque\u00f1a capilla de Santa Catalina dominan el agua."),
   "eu":("Mundaka","Mundaka","Urdaibaiko itsasadarraren bokalean dagoen arrantzale-herri ederra, Europan ospetsuenetakoa den ezker olatu baten jaioterria. Etxe zuriak eta Santa Katalina kapera txikia uraren gainean daude."),
   "fr":("Mundaka","Mundaka","Un village de p\u00eacheurs de carte postale \u00e0 l'embouchure de la ria d'Urdaibai, berceau de l'une des vagues gauches les plus c\u00e9l\u00e8bres d'Europe. Les maisons blanchies \u00e0 la chaux et la petite chapelle Santa Catalina dominent l'eau.")}),
 dict(slug="guernica", region="Bizkaia", tags=["history","heritage"], i18n={
   "en":("Gernika","Guernica","The town immortalised by Picasso's Guernica after its bombing in 1937. Its Assembly House and the symbolic Tree of Gernika remain the beating heart of Basque self-government and identity."),
   "es":("Gernika","Guernica","La villa inmortalizada por el Guernica de Picasso tras su bombardeo en 1937. Su Casa de Juntas y el simb\u00f3lico \u00c1rbol de Gernika siguen siendo el coraz\u00f3n del autogobierno y la identidad vascos."),
   "eu":("Gernika","Guernica","1937ko bonbardaketaren ondoren Picassoren Guernica margolanak hilezkortu zuen herria. Bere Batzarretxea eta Gernikako Arbola sinbolikoa euskal autogobernuaren eta nortasunaren bihotza dira oraindik."),
   "fr":("Gernika","Guernica","La ville immortalis\u00e9e par le Guernica de Picasso apr\u00e8s son bombardement en 1937. Sa maison des Juntes et le symbolique Arbre de Gernika demeurent le c\u0153ur de l'autonomie et de l'identit\u00e9 basques.")}),
 dict(slug="vizcaya-bridge", region="Bizkaia", tags=["unesco","engineering"], i18n={
   "en":("Vizcaya Bridge","Bizkaiko Zubia","The world's oldest transporter bridge (1893) and a UNESCO World Heritage Site. It ferries cars and passengers across the Nervi\u00f3n estuary in a suspended gondola \u2014 a graceful feat of industrial-age engineering."),
   "es":("Puente de Bizkaia","Bizkaiko Zubia","El puente transbordador m\u00e1s antiguo del mundo (1893) y Patrimonio de la Humanidad de la UNESCO. Traslada coches y pasajeros de una orilla a otra de la r\u00eda del Nervi\u00f3n en una barquilla suspendida: una elegante proeza de la ingenier\u00eda industrial."),
   "eu":("Bizkaiko Zubia","Zubi Esekia","Munduko zubi transbordadore zaharrena (1893) eta UNESCOren Gizateriaren Ondarea. Kotxeak eta bidaiariak Nerbioi itsasadarraren bi ertzetan zehar garraiatzen ditu zintzilik dagoen ontzi batean: ingeniaritza industrialaren balentria dotorea."),
   "fr":("Pont de Biscaye","Bizkaiko Zubia","Le plus ancien pont transbordeur du monde (1893) et site du patrimoine mondial de l'UNESCO. Il fait traverser voitures et passagers d'une rive \u00e0 l'autre de la ria du Nervion dans une nacelle suspendue : un \u00e9l\u00e9gant exploit d'ing\u00e9nierie industrielle.")}),
 dict(slug="urdaibai", region="Bizkaia", tags=["nature","unesco"], i18n={
   "en":("Urdaibai Biosphere Reserve","Urdaibai","A UNESCO Biosphere Reserve where river, marsh and Atlantic coast meet. Its estuary and cliffs shelter rich birdlife and link the beaches, the villages of Mundaka and Bermeo, and the ancient cave of Santimami\u00f1e."),
   "es":("Reserva de la Biosfera de Urdaibai","Urdaibai","Una Reserva de la Biosfera de la UNESCO donde se encuentran el r\u00edo, la marisma y la costa atl\u00e1ntica. Su estuario y sus acantilados albergan una rica avifauna y enlazan playas, los pueblos de Mundaka y Bermeo y la antigua cueva de Santimami\u00f1e."),
   "eu":("Urdaibaiko Biosfera Erreserba","Urdaibai","UNESCOren Biosfera Erreserba bat, non ibaia, padura eta Atlantikoko kostaldea bat egiten duten. Bere itsasadarrak eta labarrek hegazti-aberastasun handia gordetzen dute, eta hondartzak, Mundaka eta Bermeoko herriak eta Santimami\u00f1e kobazulo zaharra lotzen dituzte."),
   "fr":("R\u00e9serve de biosph\u00e8re d'Urdaibai","Urdaibai","Une r\u00e9serve de biosph\u00e8re de l'UNESCO o\u00f9 se rejoignent le fleuve, le marais et la c\u00f4te atlantique. Son estuaire et ses falaises abritent une riche avifaune et relient les plages, les villages de Mundaka et Bermeo et l'ancienne grotte de Santimami\u00f1e.")}),
 dict(slug="san-sebastian", region="Gipuzkoa", tags=["city","food"], i18n={
   "en":("San Sebasti\u00e1n","Donostia","A belle-\u00e9poque seaside jewel, famed for the perfect shell-shaped La Concha bay and one of the highest concentrations of Michelin stars on Earth. Elegant boulevards, pintxos bars and Mount Igueldo frame the view."),
   "es":("San Sebasti\u00e1n","Donostia","Una joya costera de la belle \u00e9poque, famosa por la perfecta bah\u00eda en forma de concha de La Concha y una de las mayores concentraciones de estrellas Michelin del mundo. Elegantes bulevares, bares de pintxos y el monte Igueldo enmarcan la vista."),
   "eu":("Donostia","San Sebasti\u00e1n","Belle \u00e9poqueko kostaldeko harribitxia, La Concha badia perfektuarengatik eta munduko Michelin izar kontzentraziorik handienetako batengatik ezaguna. Bulebar dotoreek, pintxo-taberrek eta Igueldo mendiak ikuspegia osatzen dute."),
   "fr":("Saint-S\u00e9bastien","Donostia","Un joyau baln\u00e9aire de la Belle \u00c9poque, c\u00e9l\u00e8bre pour la baie parfaite en forme de coquille de La Concha et l'une des plus fortes concentrations d'\u00e9toiles Michelin au monde. Boulevards \u00e9l\u00e9gants, bars \u00e0 pintxos et mont Igueldo encadrent la vue.")}),
 dict(slug="zumaia-flysch", region="Gipuzkoa", tags=["natural","geology"], i18n={
   "en":("Zumaia Flysch","Zumaia","Layered rock formations that read like the pages of a giant book, recording 60 million years of Earth's history. The cliffs of Itzurun beach are a pilgrimage site for geologists and photographers alike."),
   "es":("Flysch de Zumaia","Zumaia","Formaciones rocosas estratificadas que se leen como las p\u00e1ginas de un libro gigante y registran 60 millones de a\u00f1os de historia de la Tierra. Los acantilados de la playa de Itzurun son un lugar de peregrinaci\u00f3n para ge\u00f3logos y fot\u00f3grafos."),
   "eu":("Zumaiako flyscha","Zumaia","Liburu erraldoi baten orrialdeak bezala irakurtzen diren arroka-geruzak, Lurraren historiako 60 milioi urte jasotzen dituztenak. Itzurungo hondartzako labarrak erromes-leku dira geologo eta argazkilarientzat."),
   "fr":("Flysch de Zumaia","Zumaia","Des formations rocheuses stratifi\u00e9es qui se lisent comme les pages d'un livre g\u00e9ant et enregistrent 60 millions d'ann\u00e9es d'histoire de la Terre. Les falaises de la plage d'Itzurun sont un lieu de p\u00e8lerinage pour g\u00e9ologues et photographes.")}),
 dict(slug="hondarribia", region="Gipuzkoa", tags=["town","coast"], i18n={
   "en":("Hondarribia","Hondarribia","A fortified border town opposite Hendaye, with a walled medieval centre, a castle that is now a parador, and a colourful fishermen's quarter right on the estuary."),
   "es":("Hondarribia","Fuenterrab\u00eda","Una villa fortificada fronteriza frente a Hendaya, con un casco medieval amurallado, un castillo hoy Parador y un colorido barrio de pescadores junto a la r\u00eda."),
   "eu":("Hondarribia","Hondarribia","Hendaia parean dagoen muga-herri gotortua, harresiz inguratutako Erdi Aroko alde zahar batekin, gaur egun Parador den gaztelu batekin eta arrantzaleen auzo koloretsu batekin itsasadarraren ondoan."),
   "fr":("Hondarribia","Fontarrabie","Une ville fortifi\u00e9e frontali\u00e8re face \u00e0 Hendaye, avec un centre m\u00e9di\u00e9val entour\u00e9 de remparts, un ch\u00e2teau devenu Parador et un quartier de p\u00eacheurs color\u00e9 au bord de la ria.")}),
 dict(slug="onati", region="Gipuzkoa", tags=["heritage","town"], i18n={
   "en":("O\u00f1ati","O\u00f1ate","Home to the oldest university in the Basque Country (1540). Its arcaded main square and Renaissance college make it one of the region's finest historic towns \u2014 and a gateway to the mountains of Arantzazu."),
   "es":("O\u00f1ati","O\u00f1ate","Sede de la universidad m\u00e1s antigua del Pa\u00eds Vasco (1540). Su plaza mayor porticada y su colegio renacentista la convierten en una de las villas hist\u00f3ricas m\u00e1s bellas de la regi\u00f3n, y en puerta de entrada a las monta\u00f1as de Arantzazu."),
   "eu":("O\u00f1ati","O\u00f1ati","Euskal Herriko unibertsitaterik zaharrena (1540) duen herria. Bere arkupeetako plaza nagusiak eta Errenazimentuko ikastetxeak eskualdeko herri historikorik ederrenetakoa bihurtzen dute, eta Arantzazuko mendietarako sarrera."),
   "fr":("O\u00f1ati","O\u00f1ate","Si\u00e8ge de la plus ancienne universit\u00e9 du Pays basque (1540). Sa grand-place \u00e0 arcades et son coll\u00e8ge Renaissance en font l'une des plus belles villes historiques de la r\u00e9gion, et une porte d'entr\u00e9e vers les montagnes d'Arantzazu.")}),
 dict(slug="arantzazu", region="Gipuzkoa", tags=["heritage","art"], i18n={
   "en":("Sanctuary of Arantzazu","Arantzazuko santutegia","A bold modern basilica set deep in the Aizkorri mountains, adorned with monumental sculptures by Jorge Oteiza and work by Eduardo Chillida. A spiritual and artistic landmark of the Basque cultural revival."),
   "es":("Santuario de Arantzazu","Arantzazuko santutegia","Una atrevida bas\u00edlica moderna enclavada en el macizo de Aizkorri, decorada con esculturas monumentales de Jorge Oteiza y obra de Eduardo Chillida. Un hito espiritual y art\u00edstico del renacimiento cultural vasco."),
   "eu":("Arantzazuko santutegia","Arantzazu","Aizkorriko mendigunean kokatutako basilika moderno ausarta, Jorge Oteizaren eskultura monumentalez eta Eduardo Chillidaren lanekin apaindua. Euskal berpizkunde kulturalaren mugarri espiritual eta artistikoa."),
   "fr":("Sanctuaire d'Arantzazu","Arantzazuko santutegia","Une audacieuse basilique moderne nich\u00e9e au c\u0153ur du massif d'Aizkorri, orn\u00e9e de sculptures monumentales de Jorge Oteiza et d'\u0153uvres d'Eduardo Chillida. Un jalon spirituel et artistique de la renaissance culturelle basque.")}),
 dict(slug="loyola", region="Gipuzkoa", tags=["heritage","spiritual"], i18n={
   "en":("Sanctuary of Loyola","Loiolako santutegia","The birthplace of St. Ignatius of Loyola, founder of the Jesuits. The monumental baroque sanctuary, crowned by an immense gilded dome, is one of the grandest religious complexes in Spain."),
   "es":("Santuario de Loyola","Loiolako santutegia","Lugar de nacimiento de San Ignacio de Loyola, fundador de los jesuitas. El monumental santuario barroco, coronado por una inmensa c\u00fapula dorada, es uno de los conjuntos religiosos m\u00e1s grandiosos de Espa\u00f1a."),
   "eu":("Loiolako santutegia","Loyola","Ignazio Loiolakoa, jesuiten sortzailea, jaio zen lekua. Barrokozko santutegi monumentala, urrezko kupula izugarri batez koroatua, Espainiako multzo erlijioso ikusgarrienetako bat da."),
   "fr":("Sanctuaire de Loyola","Loiolako santutegia","Lieu de naissance de saint Ignace de Loyola, fondateur des j\u00e9suites. Le monumental sanctuaire baroque, couronn\u00e9 d'une immense coupole dor\u00e9e, est l'un des plus grandioses ensembles religieux d'Espagne.")}),
 dict(slug="vitoria-gasteiz", region="Araba", tags=["city","green"], i18n={
   "en":("Vitoria-Gasteiz","Gasteiz","The Basque Country's capital and a European pioneer of green urban living. Its medieval, almond-shaped old town and the Plaza de la Virgen Blanca sit beside a celebrated \u201cgreen ring\u201d of parks."),
   "es":("Vitoria-Gasteiz","Gasteiz","La capital del Pa\u00eds Vasco y pionera europea de la vida urbana sostenible. Su casco medieval en forma de almendra y la Plaza de la Virgen Blanca conviven con un c\u00e9lebre \u00abanillo verde\u00bb de parques."),
   "eu":("Gasteiz","Vitoria-Gasteiz","Euskal Herriko hiriburua eta hiri-bizitza jasangarriaren aitzindari europarra. Bere almendra-formako Erdi Aroko alde zaharra eta Andre Maria Zuriaren plaza parke-eraztun berde ospetsu batekin batera daude."),
   "fr":("Vitoria-Gasteiz","Gasteiz","La capitale du Pays basque et une pionni\u00e8re europ\u00e9enne de la vie urbaine durable. Son centre m\u00e9di\u00e9val en forme d'amande et la Plaza de la Virgen Blanca c\u00f4toient un c\u00e9l\u00e8bre \u00ab anneau vert \u00bb de parcs.")}),
 dict(slug="laguardia", region="Araba", tags=["wine","heritage"], i18n={
   "en":("Laguardia","Guardia","A hilltop medieval town ringed by walls in the heart of the Rioja Alavesa wine country. Its bodegas, cobbled lanes and vineyard views make it the capital of Basque wine tourism."),
   "es":("Laguardia","Guardia","Una villa medieval amurallada en lo alto de una colina, en plena Rioja Alavesa. Sus bodegas, callejones empedrados y vistas sobre los vi\u00f1edos la convierten en la capital del enoturismo vasco."),
   "eu":("Guardia","Laguardia","Muino baten gaineko Erdi Aroko herri harresitua, Arabako Errioxan. Bere upategiek, galtzada-harrizko kaleek eta mahastien gaineko ikuspegiek euskal ardo-turismoko hiriburu bihurtzen dute."),
   "fr":("Laguardia","Guardia","Une ville m\u00e9di\u00e9vale fortifi\u00e9e perch\u00e9e sur une colline, au c\u0153ur de la Rioja Alavesa. Ses caves, ses ruelles pav\u00e9es et ses vues sur les vignobles en font la capitale de l'\u0153notourisme basque.")}),
 dict(slug="anana", region="Araba", tags=["unesco","heritage"], i18n={
   "en":("Salinas de A\u00f1ana","A\u00f1anako Gatz Harana","A rare inland salt valley with thousands of wooden evaporation terraces, worked since Roman times. This extraordinary, UNESCO-recognised landscape is one of the oldest salt-production sites in Europe."),
   "es":("Salinas de A\u00f1ana","A\u00f1anako Gatz Harana","Un raro valle salino interior con miles de terrazas de evaporaci\u00f3n de madera, explotadas desde la \u00e9poca romana. Este paisaje excepcional, reconocido por la UNESCO, es uno de los yacimientos de sal m\u00e1s antiguos de Europa."),
   "eu":("A\u00f1anako Gatz Harana","Salinas de A\u00f1ana","Barnealdeko gatz-haran bitxia, zurezko milaka lurruntze-terraza dituena, erromatar garaitik ustiatuak. UNESCOk aitortutako paisaia aparta hau Europako gatz-ekoizpen gune zaharrenetako bat da."),
   "fr":("Salines d'A\u00f1ana","A\u00f1anako Gatz Harana","Une rare vall\u00e9e salif\u00e8re int\u00e9rieure avec des milliers de terrasses d'\u00e9vaporation en bois, exploit\u00e9es depuis l'\u00e9poque romaine. Ce paysage exceptionnel, reconnu par l'UNESCO, est l'un des plus anciens sites de production de sel d'Europe.")}),
 dict(slug="pamplona", region="Navarre", tags=["city","festival"], i18n={
   "en":("Pamplona","Iru\u00f1ea","Capital of Navarre and famous the world over for San Ferm\u00edn, when runners sprint ahead of bulls through the streets. Its Gothic cathedral, star-shaped citadel and pintxos scene reward visitors all year round."),
   "es":("Pamplona","Iru\u00f1a","Capital de Navarra y famosa en todo el mundo por San Ferm\u00edn, cuando los corredores se lanzan ante los toros por las calles. Su catedral g\u00f3tica, su ciudadela estrellada y su escena de pintxos recompensan al visitante todo el a\u00f1o."),
   "eu":("Iru\u00f1ea","Pamplona","Nafarroako hiriburua, mundu osoan Sanferminengatik ezaguna, korrikalariek zezenen aurrean kaleetan zehar egiten dutenean. Bere katedral gotikoak, izar-formako zitadelak eta pintxo-eszenak urte osoan saritzen dute bisitaria."),
   "fr":("Pampelune","Iru\u00f1ea","Capitale de la Navarre, mondialement connue pour la San Ferm\u00edn, lorsque les coureurs s'\u00e9lancent devant les taureaux dans les rues. Sa cath\u00e9drale gothique, sa citadelle en \u00e9toile et sa sc\u00e8ne de pintxos r\u00e9compensent le visiteur toute l'ann\u00e9e.")}),
 dict(slug="roncesvalles", region="Navarre", tags=["heritage","camino"], i18n={
   "en":("Roncesvalles","Orreaga","A legendary pass on the Camino de Santiago, where Roland's epic battle was fought. Its Gothic collegiate church and monastery have welcomed weary pilgrims for a thousand years."),
   "es":("Roncesvalles","Orreaga","Un paso legendario del Camino de Santiago, donde se libr\u00f3 la \u00e9pica batalla de Rold\u00e1n. Su colegiata g\u00f3tica y su monasterio acogen a los peregrinos desde hace mil a\u00f1os."),
   "eu":("Orreaga","Roncesvalles","Donejakue Bideko mendate legendarioa, non Rolanden bataila epikoa gertatu zen. Bere kolegiata eliza gotikoak eta monasterioak mila urte daramatzate erromesak hartzen."),
   "fr":("Roncevaux","Orreaga","Un col l\u00e9gendaire du chemin de Saint-Jacques, o\u00f9 fut livr\u00e9e l'\u00e9pop\u00e9e de Roland. Son \u00e9glise coll\u00e9giale gothique et son monast\u00e8re accueillent les p\u00e8lerins depuis mille ans.")}),
 dict(slug="ujue", region="Navarre", tags=["village","heritage"], i18n={
   "en":("Uju\u00e9","Uxue","A tiny hilltop village crowned by a fortified Romanesque church, offering sweeping views across Navarre. Its honey-coloured lanes feel frozen in the Middle Ages."),
   "es":("Uju\u00e9","Uxue","Una peque\u00f1a aldea en lo alto de una colina, coronada por una iglesia rom\u00e1nica fortificada, con amplias vistas de Navarra. Sus callejones color miel parecen detenidos en la Edad Media."),
   "eu":("Uxue","Uju\u00e9","Muino baten gaineko herrixka txikia, eliza erromaniko gotortu batez koroatua, Nafarroako ikuspegi zabalak eskaintzen dituena. Bere ezti-koloreko kaleak Erdi Aroan geldituak ematen dute."),
   "fr":("Uju\u00e9","Uxue","Un petit village au sommet d'une colline, couronn\u00e9 d'une \u00e9glise romane fortifi\u00e9e, offrant de vastes vues sur la Navarre. Ses ruelles couleur miel semblent fig\u00e9es au Moyen \u00c2ge.")}),
 dict(slug="zugarramurdi", region="Navarre", tags=["legend","nature"], i18n={
   "en":("Zugarramurdi","Zugarramurdi","A village of legend whose caves hosted the \u201cwitches of Zugarramurdi,\u201d tried by the Inquisition in 1610. The vast limestone cavern and its museum tell one of Europe's most famous witchcraft stories."),
   "es":("Zugarramurdi","Zugarramurdi","Una aldea de leyenda cuyas cuevas acogieron a las \u00abbrujas de Zugarramurdi\u00bb, juzgadas por la Inquisici\u00f3n en 1610. La vasta caverna de caliza y su museo cuentan una de las historias de brujer\u00eda m\u00e1s famosas de Europa."),
   "eu":("Zugarramurdi","Zugarramurdi","Kondairazko herrixka, bere kobazuloek \u00abZugarramurdiko sorginak\u00bb hartu zituztenekoa, Inkisizioak 1610ean epaituak. Kareharrizko haitzulo zabalak eta museoak Europako sorginkeria-istoriorik ospetsuenetako bat kontatzen dute."),
   "fr":("Zugarramurdi","Zugarramurdi","Un village de l\u00e9gende dont les grottes ont abrit\u00e9 les \u00ab sorci\u00e8res de Zugarramurdi \u00bb, jug\u00e9es par l'Inquisition en 1610. La vaste caverne calcaire et son mus\u00e9e racontent l'une des histoires de sorcellerie les plus c\u00e9l\u00e8bres d'Europe.")}),
 dict(slug="biarritz", region="Iparralde", tags=["coast","city"], i18n={
   "en":("Biarritz","Miarritze","The glamorous queen of the French Basque coast, once a favourite of Empress Eug\u00e9nie and European royalty. Surf culture, a grand casino and the Rocher de la Vierge meet belle-\u00e9poque elegance."),
   "es":("Biarritz","Miarritze","La glamurosa reina de la costa vasca francesa, anta\u00f1o favorita de la emperatriz Eugenia y de la realeza europea. La cultura del surf, un gran casino y la Rocher de la Vierge se dan cita con la elegancia de la belle \u00e9poque."),
   "eu":("Miarritze","Biarritz","Euskal kostalde frantseseko erregina glamurosa, garai batean Eugenia enperatrizaren eta Europako errege-erreginen gogokoena. Surfa, kasino handi bat eta Rocher de la Vierge belle \u00e9poqueko dotoreziarekin bat egiten dute."),
   "fr":("Biarritz","Miarritze","La reine glamour de la c\u00f4te basque fran\u00e7aise, autrefois favorite de l'imp\u00e9ratrice Eug\u00e9nie et de la royaut\u00e9 europ\u00e9enne. Culture du surf, grand casino et Rocher de la Vierge c\u00f4toient l'\u00e9l\u00e9gance de la Belle \u00c9poque.")}),
 dict(slug="bayonne", region="Iparralde", tags=["city","food"], i18n={
   "en":("Bayonne","Baiona","A cultured river port known for its Gothic cathedral, half-timbered houses and, above all, its chocolate. Bayonne gave France its chocolate trade and remains a gourmet capital of the north."),
   "es":("Bayona","Baiona","Un culto puerto fluvial conocido por su catedral g\u00f3tica, sus casas de entramado de madera y, sobre todo, su chocolate. Bayona dio a Francia su comercio de chocolate y sigue siendo una capital gourmet del norte."),
   "eu":("Baiona","Baiona","Ibai-portu kultua, katedral gotikoagatik, zurezko egiturazko etxeei esker eta, batez ere, txokolateagatik ezaguna. Baionak Frantziani txokolate-merkataritza eman zion eta iparraldeko gourmet-hiriburua izaten jarraitzen du."),
   "fr":("Bayonne","Baiona","Un port fluvial cultiv\u00e9 connu pour sa cath\u00e9drale gothique, ses maisons \u00e0 colombages et, surtout, son chocolat. Bayonne a donn\u00e9 \u00e0 la France son commerce du chocolat et reste une capitale gourmande du nord.")}),
 dict(slug="saint-jean-de-luz", region="Iparralde", tags=["coast","town"], i18n={
   "en":("Saint-Jean-de-Luz","Donibane Lohizune","A sheltered fishing port and royal wedding town, where Louis XIV married Mar\u00eda Teresa in 1660. A crescent bay, colourful Basque houses and a lively old harbour make it irresistible."),
   "es":("San Juan de Luz","Donibane Lohizune","Un puerto pesquero resguardado y villa de boda real, donde Luis XIV se cas\u00f3 con Mar\u00eda Teresa en 1660. Una bah\u00eda en forma de media luna, casas vascas de colores y un animado puerto viejo."),
   "eu":("Donibane Lohizune","Saint-Jean-de-Luz","Portu arrantzale babestua eta errege-ezkontzako herria, non Luis XIV.a Maria Teresarekin ezkondu zen 1660an. Ilargierdi-formako badia, euskal etxe koloretsuak eta portu zahar bizia."),
   "fr":("Saint-Jean-de-Luz","Donibane Lohizune","Un port de p\u00eache abrit\u00e9 et une ville de mariage royal, o\u00f9 Louis XIV \u00e9pousa Marie-Th\u00e9r\u00e8se en 1660. Une baie en croissant, des maisons basques color\u00e9es et un vieux port anim\u00e9.")}),
 dict(slug="la-rhune", region="Iparralde", tags=["mountain","nature"], i18n={
   "en":("La Rhune","Larrun","The western Pyrenees' signature peak (905 m), climbed by a charming 1924 rack railway. Panoramic views sweep across the coast, the mountains and both sides of the French\u2013Spanish border."),
   "es":("La Rhune","Larrun","El pico emblem\u00e1tico de los Pirineos occidentales (905 m), al que sube un encantador tren cremallera de 1924. Las vistas panor\u00e1micas abarcan la costa, las monta\u00f1as y ambos lados de la frontera franco-espa\u00f1ola."),
   "eu":("Larrun","La Rhune","Mendebaldeko Pirinioetako gailur enblematikoa (905 m), 1924ko tren kremailera xarmangarri batek igotzen duena. Ikuspegi panoramikoek kostaldea, mendiak eta frantziar-spaniar mugaren bi aldeak hartzen dituzte."),
   "fr":("La Rhune","Larrun","Le sommet embl\u00e9matique des Pyr\u00e9n\u00e9es occidentales (905 m), gravi par un charmant train \u00e0 cr\u00e9maill\u00e8re de 1924. Les panoramas s'\u00e9tendent sur la c\u00f4te, les montagnes et les deux versants de la fronti\u00e8re franco-espagnole.")}),
]

UI = {
 "en": dict(nav_about="About", nav_places="Locations", nav_credits="Credits",
   title="Iconic Locations of the Basque Country \u2014 Euskal Herria",
   meta="A documented guide to the iconic locations of the Basque Country: cities, coast, mountains, art and heritage across Bizkaia, Gipuzkoa, Araba, Navarre and Iparralde.",
   hero_title="The Basque Country", hero_sub="Iconic locations of a land between the mountains and the sea",
   hero_lead="Twenty-four remarkable places across Bizkaia, Gipuzkoa, Araba, Navarre and Iparralde \u2014 from Frank Gehry's titanium museum and dragon-stone staircases to painted flysch cliffs, salt valleys and witch-caves.",
   cta1="Explore the Locations", cta2="About the Region",
   about_tag="The Region", about_h2="A country of seven provinces",
   about_p1="The Basque Country \u2014 <em>Euskal Herria</em>, \u201cthe land of the Basque speakers\u201d \u2014 straddles the western Pyrenees where Spain meets France. It is home to the Basques, one of Europe's oldest peoples, with a language, <em>Euskara</em>, that is a mystery to linguists: a living isolate unrelated to any other tongue on Earth.",
   about_p2="Historically it counts seven provinces: <strong>Bizkaia</strong>, <strong>Gipuzkoa</strong>, <strong>Araba</strong> and <strong>Navarre</strong> in Spain, and <strong>Lapurdi</strong>, <strong>Zuberoa</strong> and <strong>Behe Nafarroa</strong> (together <em>Iparralde</em>) in France. The landscape runs from wild Atlantic surf beaches and fishing villages to green mountain valleys, vineyards and three of the country's great modern museums.",
   about_p3="Its people are fiercely proud of their identity \u2014 expressed in the red, green and white <em>Ikurri\u00f1a</em> flag, the swirling <em>lauburu</em> symbol, the sport of <em>pelota</em>, and a culinary culture that has made San Sebasti\u00e1n one of the greatest places to eat on the planet.",
   caption="The flysch cliffs of Zumaia \u2014 60 million years of Earth history, on the Gipuzkoa coast.",
   facts=[("7","Traditional provinces"),("Euskara","Europe's oldest language isolate"),
          ("3","UNESCO listings featured here"),("1","World-famous left-hand wave (Mundaka)"),
          ("\u2248 3M","Basque speakers &amp; residents"),("Bay of Biscay","Wild Atlantic coastline")],
   places_tag="The Locations", places_h2="Places worth crossing the world for",
   places_sub="Filter by province or region. Colours match the badges on each place.", all="All",
   credits_summary="Image credits &amp; licences (\u00a9 their respective authors, via Wikimedia Commons)",
   footer="A fan-made, informational guide to the iconic locations of the Basque Country / Euskal Herria. Descriptions are provided in good faith; photographs are credited to their authors under their respective licences."),

 "es": dict(nav_about="La Regi\u00f3n", nav_places="Lugares", nav_credits="Cr\u00e9ditos",
   title="Lugares ic\u00f3nicos del Pa\u00eds Vasco \u2014 Euskal Herria",
   meta="Una gu\u00eda de los lugares ic\u00f3nicos del Pa\u00eds Vasco: ciudades, costa, monta\u00f1as, arte y patrimonio en Bizkaia, Gipuzkoa, \u00c1lava, Navarra e Iparralde.",
   hero_title="El Pa\u00eds Vasco", hero_sub="Lugares ic\u00f3nicos de una tierra entre el mar y las monta\u00f1as",
   hero_lead="Veinticuatro lugares extraordinarios en Bizkaia, Gipuzkoa, \u00c1lava, Navarra e Iparralde: desde el museo de titanio de Frank Gehry y las escaleras de piedra del drag\u00f3n hasta los acantilados de flysch, las salinas y las cuevas de las brujas.",
   cta1="Explorar los lugares", cta2="Sobre la regi\u00f3n",
   about_tag="La Regi\u00f3n", about_h2="Un pa\u00eds de siete provincias",
   about_p1="El Pa\u00eds Vasco \u2014 <em>Euskal Herria</em>, \u00abla tierra de los vascohablantes\u00bb \u2014 se extiende a ambos lados de los Pirineos occidentales, donde Espa\u00f1a se encuentra con Francia. Es la patria de los vascos, uno de los pueblos m\u00e1s antiguos de Europa, con una lengua, el <em>euskara</em>, que desconcierta a los ling\u00fcistas: un aislado vivo sin parentesco con ninguna otra lengua del mundo.",
   about_p2="Hist\u00f3ricamente cuenta con siete provincias: <strong>Bizkaia</strong>, <strong>Gipuzkoa</strong>, <strong>\u00c1lava</strong> y <strong>Navarra</strong> en Espa\u00f1a, y <strong>Lapurdi</strong>, <strong>Zuberoa</strong> y <strong>Behe Nafarroa</strong> (en conjunto, <em>Iparralde</em>) en Francia. El paisaje va de las salvajes playas atl\u00e1nticas y los pueblos pesqueros a los verdes valles, los vi\u00f1edos y tres de los grandes museos modernos del pa\u00eds.",
   about_p3="Su gente est\u00e1 profundamente orgullosa de su identidad, expresada en la <em>ikurri\u00f1a</em> roja, verde y blanca, el s\u00edmbolo giratorio del <em>lauburu</em>, el deporte de la <em>pelota</em> y una cultura culinaria que ha convertido a San Sebasti\u00e1n en uno de los mejores lugares del mundo para comer.",
   caption="Los acantilados de flysch de Zumaia: 60 millones de a\u00f1os de historia de la Tierra, en la costa de Gipuzkoa.",
   facts=[("7","Provincias tradicionales"),("Euskara","La lengua aislada m\u00e1s antigua de Europa"),
          ("3","Sitios de la UNESCO incluidos aqu\u00ed"),("1","Ola izquierda de fama mundial (Mundaka)"),
          ("\u2248 3M","Vascoparlantes y residentes"),("Golfo de Bizkaia","Salvaje costa atl\u00e1ntica")],
   places_tag="Los Lugares", places_h2="Lugares por los que cruzar\u00edas el mundo",
   places_sub="Filtra por provincia o regi\u00f3n. Los colores coinciden con las etiquetas de cada lugar.", all="Todos",
   credits_summary="Cr\u00e9ditos y licencias de las im\u00e1genes (\u00a9 de sus respectivos autores, v\u00eda Wikimedia Commons)",
   footer="Gu\u00eda informativa hecha por un aficionado sobre los lugares ic\u00f3nicos del Pa\u00eds Vasco / Euskal Herria. Las descripciones se ofrecen de buena fe; las fotograf\u00edas se atribuyen a sus autores bajo sus respectivas licencias."),

 "eu": dict(nav_about="Eskualdea", nav_places="Lekuak", nav_credits="Kredituak",
   title="Euskal Herriko leku ikonikoak \u2014 Euskal Herria",
   meta="Euskal Herriko leku ikonikoen gida: hiriak, kostaldea, mendiak, artea eta ondarea Bizkaia, Gipuzkoa, Araba, Nafarroa eta Iparraldean.",
   hero_title="Euskal Herria", hero_sub="Itsasoaren eta mendien arteko herri baten leku ikonikoak",
   hero_lead="Hogeita lau leku aparta Bizkaia, Gipuzkoa, Araba, Nafarroa eta Iparraldean: Frank Gehryren titaniozko museotik eta dragoiaren harrizko eskaileretara, flysch labarrak, gatz-haranak eta sorginen kobazuloak barne.",
   cta1="Arakatu lekuak", cta2="Eskualdeari buruz",
   about_tag="Eskualdea", about_h2="Zazpi probintziako herria",
   about_p1="Euskal Herria \u2014 euskaraz mintzo direnen lurra \u2014 Mendebaldeko Pirinioen bi aldeetan zabaltzen da, Espainia eta Frantzia elkartzen diren tokian. Euskaldunen sorterria da, Europako herririk zaharrenetako bat, hizkuntza batekin, <em>euskara</em>, hizkuntzalariek ulertzen ez dutena: munduan beste inongo hizkuntzarekin ahaidetasunik ez duen hizkuntza bakartua.",
   about_p2="Historikoki zazpi probintzia ditu: <strong>Bizkaia</strong>, <strong>Gipuzkoa</strong>, <strong>Araba</strong> eta <strong>Nafarroa</strong> Espainian, eta <strong>Lapurdi</strong>, <strong>Zuberoa</strong> eta <strong>Behe Nafarroa</strong> (elkarrekin, <em>Iparralde</em>) Frantzian. Paisaia hondartza atlantiko basatietatik eta arrantzale-herrietatik haran berdeetara, mahastietara eta herrialdeko hiru museo moderno handietara doa.",
   about_p3="Bere jendea oso harro dago bere nortasunaz, bandera gorri, berde eta zurian (<em>ikurrina</em>), <em>lauburuaren</em> ikurrean, <em>pilota</em> jokoan eta San Sebastian munduko jateko lekurik onenetakoa bihurtu duen sukaldaritza-kulturan islatzen dena.",
   caption="Zumaiako flysch labarrak: Lurraren historiako 60 milioi urte, Gipuzkoako kostaldean.",
   facts=[("7","Probintzia tradizionalak"),("Euskara","Europako hizkuntza bakartu zaharrena"),
          ("3","Hemen agertzen diren UNESCO ondareak"),("1","Mundu osoan ezaguna den ezker olatua (Mundaka)"),
          ("\u2248 3M","Euskaldunak eta biztanleak"),("Bizkaiko Golkoa","Atlantikoko kostalde basatia")],
   places_tag="Lekuak", places_h2="Mundua zeharkatzeko moduko lekuak",
   places_sub="Iragazi probintziaren edo eskualdearen arabera. Koloreak leku bakoitzaren etiketei dagozkie.", all="Guztiak",
   credits_summary="Irudi-kredituak eta lizentziak (\u00a9 egile bakoitza, Wikimedia Commons bidez)",
   footer="Zale batek egindako gida informatzailea Euskal Herriko leku ikonikoei buruz. Deskribapenak borondate onez ematen dira; argazkiak egileei egozten zaizkie beren lizentzien arabera."),

 "fr": dict(nav_about="La R\u00e9gion", nav_places="Lieux", nav_credits="Cr\u00e9dits",
   title="Lieux embl\u00e9matiques du Pays basque \u2014 Euskal Herria",
   meta="Un guide des lieux embl\u00e9matiques du Pays basque : villes, c\u00f4te, montagnes, art et patrimoine en Biscaye, Guipuscoa, Alava, Navarre et Iparralde.",
   hero_title="Le Pays basque", hero_sub="Lieux embl\u00e9matiques d'une terre entre mer et montagne",
   hero_lead="Vingt-quatre lieux remarquables en Biscaye, Guipuscoa, Alava, Navarre et Iparralde : du mus\u00e9e de titane de Frank Gehry aux escaliers de pierre du dragon, en passant par les falaises de flysch, les salines et les grottes des sorci\u00e8res.",
   cta1="Explorer les lieux", cta2="\u00c0 propos de la r\u00e9gion",
   about_tag="La R\u00e9gion", about_h2="Un pays de sept provinces",
   about_p1="Le Pays basque \u2014 <em>Euskal Herria</em>, \u00ab le pays de ceux qui parlent basque \u00bb \u2014 s'\u00e9tend de part et d'autre des Pyr\u00e9n\u00e9es occidentales, l\u00e0 o\u00f9 l'Espagne rencontre la France. C'est la patrie des Basques, l'un des peuples les plus anciens d'Europe, dot\u00e9 d'une langue, l'<em>euskara</em>, qui d\u00e9route les linguistes : un isolat vivant sans parent\u00e9 avec aucune autre langue au monde.",
   about_p2="Elle compte historiquement sept provinces : la <strong>Biscaye</strong>, le <strong>Guipuscoa</strong>, l'<strong>Alava</strong> et la <strong>Navarre</strong> en Espagne, et le <strong>Labourd</strong>, la <strong>Soule</strong> et la <strong>Basse-Navarre</strong> (r\u00e9unis sous le nom d'<em>Iparralde</em>) en France. Le paysage va des plages atlantiques sauvages et des villages de p\u00eacheurs aux vertes vall\u00e9es, aux vignobles et \u00e0 trois des grands mus\u00e9es modernes du pays.",
   about_p3="Sa population est profond\u00e9ment fi\u00e8re de son identit\u00e9, exprim\u00e9e par l'<em>ikurri\u00f1a</em> rouge, verte et blanche, le symbole tournant du <em>lauburu</em>, le sport de la <em>pelote</em> et une culture culinaire qui a fait de Saint-S\u00e9bastien l'un des meilleurs endroits du monde pour manger.",
   caption="Les falaises de flysch de Zumaia : 60 millions d'ann\u00e9es d'histoire de la Terre, sur la c\u00f4te du Guipuscoa.",
   facts=[("7","Provinces traditionnelles"),("Euskara","Le plus ancien isolat linguistique d'Europe"),
          ("3","Sites UNESCO pr\u00e9sent\u00e9s ici"),("1","Vague gauche de renomm\u00e9e mondiale (Mundaka)"),
          ("\u2248 3M","Locuteurs basques et habitants"),("Golfe de Gascogne","C\u00f4te atlantique sauvage")],
   places_tag="Les Lieux", places_h2="Des lieux qui valent le tour du monde",
   places_sub="Filtrez par province ou r\u00e9gion. Les couleurs correspondent aux badges de chaque lieu.", all="Tous",
   credits_summary="Cr\u00e9dits et licences des images (\u00a9 leurs auteurs respectifs, via Wikimedia Commons)",
   footer="Guide informatif r\u00e9alis\u00e9 par un passionn\u00e9 sur les lieux embl\u00e9matiques du Pays basque / Euskal Herria. Les descriptions sont fournies de bonne foi ; les photographies sont cr\u00e9dit\u00e9es \u00e0 leurs auteurs selon leurs licences respectives."),
}

CSS = """
  :root{--cream:#f7f4ee;--paper:#fff;--ink:#20261f;--muted:#6b746a;--red:#c8102e;--green:#0b7a3b;--line:#e4ded2;}
  *{box-sizing:border-box}
  html{scroll-behavior:smooth;scroll-padding-top:74px}
  body{margin:0;background:var(--cream);color:var(--ink);font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased}
  img{max-width:100%;display:block} a{color:inherit}
  .wrap{max-width:1200px;margin:0 auto;padding:0 clamp(1.1rem,4vw,2.5rem)}
  h1,h2,h3{font-family:"Playfair Display",Georgia,serif;margin:0}
  nav.top{position:sticky;top:0;z-index:50;background:rgba(247,244,238,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
  nav.top .inner{max-width:1200px;margin:0 auto;padding:.7rem clamp(1.1rem,4vw,2.5rem);display:flex;align-items:center;justify-content:space-between;gap:1rem}
  nav.top .logo{display:flex;align-items:center;gap:.55rem;font-family:"Playfair Display",serif;font-weight:700;font-size:1.02rem}
  .lauburu{width:22px;height:22px;fill:var(--red)}
  nav.top .links{display:flex;align-items:center;gap:1.1rem;flex-wrap:wrap}
  nav.top .links a{color:var(--muted);text-decoration:none;font-size:.82rem;font-weight:600}
  nav.top .links a:hover{color:var(--ink)}
  .langs{display:flex;gap:.3rem;border:1px solid var(--line);border-radius:999px;padding:.2rem;background:#fff}
  .langs a{font-size:.76rem;font-weight:700;color:var(--muted);text-decoration:none;padding:.28rem .6rem;border-radius:999px}
  .langs a:hover{color:var(--ink)}
  .langs a.active{background:var(--red);color:#fff}
  .hero{position:relative;min-height:78vh;display:flex;align-items:flex-end;overflow:hidden;background:#111}
  .hero .bg{position:absolute;inset:0;background-size:cover;background-position:center 40%}
  .hero .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,20,15,.35),rgba(15,20,15,.72) 60%,rgba(15,20,15,.92))}
  .hero .content{position:relative;z-index:2;width:100%;padding:4rem 0 3rem;color:#fff}
  .hero .eyebrow{font-size:.76rem;font-weight:700;letter-spacing:.4em;text-transform:uppercase;color:#f4d58d;display:flex;align-items:center;gap:.6rem}
  .hero .eyebrow .lauburu{fill:#f4d58d;width:18px;height:18px}
  .hero h1{font-size:clamp(2.4rem,7.5vw,5.4rem);line-height:1.02;margin:.5rem 0 .3rem;font-weight:800}
  .hero .sub{font-family:"Playfair Display",serif;font-style:italic;font-size:clamp(1.15rem,2.8vw,1.8rem);color:#eadfce}
  .hero .lead{max-width:640px;color:#d9d5cc;margin:1rem 0 1.6rem}
  .hero .cta{display:flex;gap:.7rem;flex-wrap:wrap}
  .btn{display:inline-block;padding:.7rem 1.4rem;border-radius:999px;text-decoration:none;font-weight:700;font-size:.84rem;background:#fff;color:var(--ink);transition:.2s}
  .btn.alt{background:var(--red);color:#fff} .btn:hover{transform:translateY(-2px)}
  section{padding:clamp(2.75rem,6vw,4.75rem) 0}
  .sec-head{margin-bottom:1.9rem;max-width:780px}
  .sec-head .tag{font-size:.74rem;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:var(--red)}
  .sec-head h2{font-size:clamp(2rem,5vw,3.2rem);margin:.2rem 0 .5rem;line-height:1.05}
  .sec-head p{color:var(--muted);margin:0}
  .intro{display:grid;grid-template-columns:1.15fr .85fr;gap:2.5rem;align-items:center}
  .intro p{font-size:1.04rem;color:#3b423a;margin:0 0 1rem}
  .intro figure{margin:0;border-radius:1rem;overflow:hidden;border:1px solid var(--line);box-shadow:0 18px 40px rgba(30,30,20,.12)}
  .intro figcaption{font-size:.72rem;color:var(--muted);padding:.5rem .7rem;background:#fff}
  .facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem}
  .fact{background:var(--paper);border:1px solid var(--line);border-radius:.9rem;padding:1.2rem 1.15rem}
  .fact .k{font-family:"Playfair Display",serif;font-size:1.5rem;font-weight:700;display:block}
  .fact .l{font-size:.8rem;color:var(--muted)}
  .fact.r .k{color:var(--red)} .fact.g .k{color:var(--green)}
  .filters{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:1.6rem}
  .filter{border:1.5px solid var(--rc,#999);color:var(--rc,#333);background:transparent;border-radius:999px;padding:.45rem 1rem;font:inherit;font-size:.82rem;font-weight:700;cursor:pointer;transition:.18s}
  .filter:hover{background:color-mix(in srgb,var(--rc) 10%,transparent)}
  .filter.active{background:var(--rc,#333);color:#fff}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:1.5rem}
  .loc{background:var(--paper);border:1px solid var(--line);border-radius:1rem;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 10px 26px rgba(30,30,20,.06);transition:.25s}
  .loc:hover{transform:translateY(-5px);box-shadow:0 22px 46px rgba(30,30,20,.14)}
  .loc.hide{display:none}
  .loc-img{position:relative;aspect-ratio:16/10;overflow:hidden;background:#eee}
  .loc-img img{width:100%;height:100%;object-fit:cover;transition:transform .6s}
  .loc:hover .loc-img img{transform:scale(1.06)}
  .region-badge{position:absolute;top:.7rem;left:.7rem;background:var(--rc);color:#fff;font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.28rem .6rem;border-radius:999px}
  .loc-body{padding:1.15rem 1.25rem 1.3rem;display:flex;flex-direction:column;flex:1}
  .loc-body h3{font-size:1.32rem;line-height:1.15}
  .alt{font-family:"Playfair Display",serif;font-style:italic;color:var(--red);font-size:.92rem;margin:.1rem 0 .6rem}
  .loc-body p{margin:0 0 1rem;color:#414840;font-size:.93rem}
  .chips{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:.9rem}
  .chip{font-size:.68rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--green);background:#e9f2ea;border-radius:999px;padding:.22rem .6rem}
  .credit{margin-top:auto;font-size:.66rem;color:#9a9f94}
  .credit a{color:#8a8f84;text-decoration:none;border-bottom:1px dotted #c9cec2}
  .credits{border-top:1px solid var(--line);margin-top:2rem;padding-top:1rem;color:var(--muted);font-size:.8rem}
  .credits summary{cursor:pointer;font-weight:600;color:var(--ink)}
  .credits ul{columns:2;column-gap:2rem;list-style:none;padding:0;margin:.6rem 0 0}
  footer{border-top:1px solid var(--line);padding:2rem 0;color:var(--muted);font-size:.8rem}
  @media(max-width:820px){.intro{grid-template-columns:1fr}.credits ul{columns:1}nav.top .links .nava{display:none}}
"""

JS = """
  var btns=document.querySelectorAll('.filter'),cards=document.querySelectorAll('.loc');
  btns.forEach(function(b){b.addEventListener('click',function(){
    btns.forEach(function(x){x.classList.remove('active')});b.classList.add('active');
    var f=b.dataset.f;
    cards.forEach(function(c){c.classList.toggle('hide',!(f==='all'||c.dataset.region===f));});
  });});
"""

LAUBURU = ('<svg class="lauburu" viewBox="0 0 100 100" aria-hidden="true">'
           + "".join(f'<path d="M50 50 C 46 30 54 14 78 10 C 64 26 60 38 50 50 Z" transform="rotate({a} 50 50)"/>'
                     for a in (0, 90, 180, 270)) + '</svg>')

HERO = ipath("gaztelugatxe")
INTRO_IMG = ipath("zumaia-flysch")

def lang_switch(active):
    out = []
    for lg in LANGS:
        cls = ' class="active"' if lg == active else ""
        out.append(f'<a href="{PAGE_FILE[lg]}" hreflang="{lg}"{cls}>{LANG_LABEL[lg]}</a>')
    return "".join(out)

def card(l, lang):
    name, alt, desc = l["i18n"][lang]
    p = ipath(l["slug"])
    tags = "".join(f'<span class="chip">{html.escape(TAGS[t][lang])}</span>' for t in l["tags"])
    return f"""
      <article class="loc" data-region="{l['region']}">
        <div class="loc-img">
          <img src="{html.escape(p)}" alt="{html.escape(name)}" loading="lazy" />
          <span class="region-badge" style="--rc:{REGION_COLOR[l['region']]}">{html.escape(REGION_NAMES[lang][l['region']])}</span>
        </div>
        <div class="loc-body">
          <h3>{html.escape(name)}</h3>
          <div class="alt">{html.escape(alt)}</div>
          <p>{html.escape(desc)}</p>
          <div class="chips">{tags}</div>
          <div class="credit">{credit(l['slug'])}</div>
        </div>
      </article>"""

def credits_list():
    items = []
    for slug, m in META.items():
        page = "https://commons.wikimedia.org/wiki/" + quote(m.get("title", "").replace(" ", "_"))
        items.append(f'<li>{html.escape(m.get("artist","Unknown"))} \u2014 '
                     f'<a href="{page}" target="_blank" rel="noopener">{html.escape(m.get("license","See source"))}</a></li>')
    return "".join(items)

def build_page(lang):
    u = UI[lang]
    cards = "".join(card(l, lang) for l in LOCATIONS)
    filters = "".join(f'<button class="filter" data-f="{r}" style="--rc:{c}">{html.escape(REGION_NAMES[lang][r])}</button>'
                      for r, c in REGION_COLOR.items())
    facts = "".join(
        f'<div class="fact {"r" if i==0 else ("g" if i==1 else "")}"><span class="k">{k}</span><span class="l">{l}</span></div>'
        for i, (k, l) in enumerate(u["facts"]))
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{html.escape(u['title'])}</title>
<meta name="description" content="{html.escape(u['meta'])}" />
<meta property="og:title" content="{html.escape(u['title'])}" />
<meta property="og:description" content="{html.escape(u['meta'])}" />
<meta property="og:type" content="website" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%97%BA%EF%B8%8F%3C/text%3E%3C/svg%3E" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet" />
<style>{CSS}</style>
</head>
<body>
<nav class="top"><div class="inner">
  <div class="logo">{LAUBURU} Basque Country \u00b7 Euskal Herria</div>
  <div class="links">
    <a class="nava" href="#about">{html.escape(u['nav_about'])}</a>
    <a class="nava" href="#places">{html.escape(u['nav_places'])}</a>
    <a class="nava" href="#credits">{html.escape(u['nav_credits'])}</a>
    <div class="langs">{lang_switch(lang)}</div>
  </div>
</div></nav>

<header class="hero">
  <div class="bg" style="background-image:url('{html.escape(HERO)}')"></div><div class="shade"></div>
  <div class="content wrap">
    <div class="eyebrow">{LAUBURU} Euskal Herria</div>
    <h1>{html.escape(u['hero_title'])}</h1>
    <div class="sub">{html.escape(u['hero_sub'])}</div>
    <p class="lead">{html.escape(u['hero_lead'])}</p>
    <div class="cta">
      <a class="btn alt" href="#places">{html.escape(u['cta1'])}</a>
      <a class="btn" href="#about">{html.escape(u['cta2'])}</a>
    </div>
  </div>
</header>

<section id="about"><div class="wrap">
  <div class="sec-head"><div class="tag">{html.escape(u['about_tag'])}</div><h2>{html.escape(u['about_h2'])}</h2></div>
  <div class="intro">
    <div>
      <p>{u['about_p1']}</p>
      <p>{u['about_p2']}</p>
      <p>{u['about_p3']}</p>
    </div>
    <figure>
      <img src="{html.escape(INTRO_IMG)}" alt="{html.escape(u['caption'])}" />
      <figcaption>{html.escape(u['caption'])}</figcaption>
    </figure>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="facts">{facts}</div>
</div></section>

<section id="places" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><div class="tag">{html.escape(u['places_tag'])}</div><h2>{html.escape(u['places_h2'])}</h2>
    <p>{html.escape(u['places_sub'])}</p></div>
  <div class="filters">
    <button class="filter active" data-f="all" style="--rc:#20261f">{html.escape(u['all'])}</button>
    {filters}
  </div>
  <div class="grid">{cards}
  </div>
</div></section>

<div class="wrap" id="credits">
  <details class="credits">
    <summary>{u['credits_summary']}</summary>
    <ul>{credits_list()}</ul>
  </details>
  <footer>{html.escape(u['footer'])}</footer>
</div>

<script>{JS}</script>
</body>
</html>
"""

for lang in LANGS:
    html_out = build_page(lang)
    open(PAGE_FILE[lang], "w").write(html_out)
    print(f"wrote {PAGE_FILE[lang]} ({lang}) {len(html_out)} bytes")
