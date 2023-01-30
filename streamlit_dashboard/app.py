# -*- coding: utf-8 -*-
# Importation des librairies standards 
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu as om
import folium
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
from PIL import Image
import plotly.graph_objects as go
from IPython.display import HTML
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import streamlit_folium as sf
from sklearn.cluster import KMeans


# LECTURE DE LA BASE DE DONNEES 
df_json1=pd.read_json(r"./streamlit_dashboard/booking.json", lines=True)
df_json2 = pd.read_json(r"./streamlit_dashboard/booking_1.json", lines=True)

# MERGE DES DEUX FICHIERS JSON
df = pd.concat([df_json1, df_json2], axis=0)


# PAGE PRINCIPALE DU SITE 
st.title('Bienvenues à Milan! :hotel: ')
st.write('Vous souhaitez vous rendre à Milan du 4 au 20 Août avec la personne de votre choix mais vous ne savez pas pour quels logements optés. Nous vous proposons une recommandation de logement selon votre budget.')


rad=st.sidebar.radio("Navigation", ["Guide", "Map", "Statistiques", "Recommandation", "Clustering"])


### GUIDE DES ENDROITS OU ALLER A MILAN 
if rad == "Guide":
    image = Image.open(r"./streamlit_dashboard/Milano.jpg")
    st.image(image, caption='Duomo de Milan')

    st.header("Quoi faire à Milan?")
    st.markdown("<div style='text-align: justify'><p>Nous vous avons préparé un petit guide afin que vous découvriez les endroits emblématiques à Milan. Nous vous dressons une panoplie de musées, de monuments. Pour passer un moment de détente, nous vous avons également répertorier les rues du shopping et une liste des plats typiques à déguster de la cuisine italienne!</p></div>", unsafe_allow_html=True)
    
    st.subheader("Musées :art: ")
    st.subheader("Brera Pinacoteca")
    st.markdown("<div style='text-align: justify'><p>Le bâtiment, construit sur un ancien couvent du XIVe siècle de l'ordre des Umiliati et ensuite passé aux Jésuites qui y établirent une école, a connu sa structure actuelle, solide et austère, à partir du début du XVIIe siècle. En 1773 le Collège de Brera devient propriété de l'État et il devient le siège de certains des instituts culturels les plus avancés de la ville. Cet endroit est très connu pour l'oeuvre d'art de Francesco Haynes : Il Bacio.</p></div>", unsafe_allow_html=True)
    url_brera = "https://pinacotecadibrera.eventim-inhouse.de/webshop/webticket/timeslot"
    loc_brera="https://www.google.com/maps/dir/48.8866182,2.3357255/Brera+Pinacoteca+milano/@46.8969954,1.2413364,6z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x4786ee11587e4e1f:0x1b367a8e2cb13736!2m2!1d9.1878145!2d45.4719545"
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_brera)
    
    st.write("Cliquez ici pour acheter les billets : [link](%s)" % url_brera)
    
    st.markdown("""---""")

    st.subheader("Chiesa Santa Maria delle Grazie Corso Magenta ")
    st.markdown("<div style='text-align: justify'><p>L'église et le monastère ont été fondés vers 1463 par des Dominicains et elle est achevée entre 1472 et 1482. On trouve dans le réfectoire La Cène de Léonard de Vinci (ainsi que la Crucifixion de Giovanni Donato Montorfano). L'ensemble est inscrit à la liste du patrimoine mondial de l'humanité établie par l'UNESCO.</div>", unsafe_allow_html=True)
    loc_chiesa="https://www.google.fr/maps/place/%C3%89glise+Santa+Maria+delle+Grazie/@45.4659667,9.1687681,17z/data=!3m1!4b1!4m5!3m4!1s0x4786c15a44bf1c83:0xed5bcdc4d3c75a59!8m2!3d45.465963!4d9.1709621"
    url_chiesa="https://cenacolovinciano.vivaticket.it/?qubsq=50cf60a5-57bc-4b55-ac37-1d24a68c1dca&qubsp=e5e9bf89-9a9b-42f4-a9c9-30980b937e88&qubsts=1674479091&qubsc=bestunion&qubse=vivaticketoperator&qubsrt=Safetynet&qubsh=2be74c678fdbcbfaa14a7f5f1c6e7aa0"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_chiesa)
    
    st.write("Cliquez ici pour acheter les billets : [link](%s)" % url_chiesa)
    
    st.markdown("""---""")

    st.subheader("Il Teatro della Scala")
    st.markdown("<div style='text-align: justify'><p>Lorsque dans la nuit du 25 février 1776, dans des circonstances mystérieuses, un incendie détruisit le Teatro Regio Ducale, Milan se retrouva sans opéra. L'impératrice Marie-Thérèse d'Autriche en commanda une autre à construire, cette fois dans la zone de l'église délabrée de Santa Maria della Scala. Après seulement deux ans, de 1776 à 1778, les travaux sont terminés. Ainsi est né le Teatro Grande alla Scala, destiné à devenir l'un des principaux points de référence culturels en Italie et en Europe.</p></div>", unsafe_allow_html=True)
    loc_teatro="https://www.google.com/maps/dir/48.8866182,2.3357255/La+Scala,+Via+Filodrammatici,+Milan,+Italie/@46.9665968,3.4859459,7z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x4786c6ad891a5757:0x1bade948102e834f!2m2!1d9.1895512!2d45.4674021"
    url_scala="https://museoscala.vivaticket.it/it/event/ingresso-museo/195053"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_teatro)
    
    st.write("Cliquez ici pour acheter les billets : [link](%s)" % url_scala)
    
    st.markdown("""---""")
    
    
    st.subheader("Monuments :european_castle: ")
    st.subheader("Palazzo Reale")
    st.markdown("<div style='text-align: justify'><p>Palazzo Reale est le cœur des expositions du centre de Milan, une structure de la municipalité de Milan qui planifie, conçoit et gère depuis des années de grandes expositions d'art pour le grand public. Sur une tradition riche et forte, qui a commencé dans les années 1950, un travail se poursuit aujourd'hui qui, au cours des dix dernières années, a positionné Palazzo Reale à un niveau d'excellence tant pour la qualité des projets scientifiques que pour la variété des propositions, avec de millions de visiteurs par an.</p></div>", unsafe_allow_html=True)
    loc_palazzo="https://www.google.com/maps/dir//Il+palazzo+reale+milano/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x4786c6aec57575a1:0xdd579e63ba086381?sa=X&ved=2ahUKEwiR8LGAvN78AhUZTKQEHYCZBG4Q9Rd6BAh8EAU"
    url_palazzo = "https://www.palazzorealemilano.it/index.php/la-tua-visita/biglietti-e-prenotazioni"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_brera)
    
    st.write("Cliquez ici pour acheter les billets : [link](%s)" % url_palazzo)
    
    st.markdown("""---""")
    
    st.subheader("Galleria Vittorio Emanuele II")
    st.markdown("<div style='text-align: justify'><p>Construite en 1877, la splendide Galleria Vittorio Emanuele II est représentative de Milan. Il forme une immense croix sous un dôme en acier émaillé de 50 m de haut et abrite d'élégantes boutiques, cafés et restaurants.. Au sol de l'octogone central, quatre mosaïques représentant les armoiries des trois capitales du Royaume d'Italie (Turin, Florence et Rome) et de Milan. La tradition dit que si une personne se retourne trois fois avec un talon sur les testicules du taureau des armoiries de Turin, cela lui portera chance.</p></div>", unsafe_allow_html=True)
    loc_galleria="https://www.google.com/maps/dir//Galleria+Vittorio+Emanuele+II/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x47793506fd86b6c3:0x270b9ca95809d416?sa=X&ved=2ahUKEwiayPiNvN78AhWhVqQEHS5gBkEQ9Rd6BAh2EAQ"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_galleria)
    
    st.markdown("""---""")
    
    st.subheader("Il Duomo")
    st.markdown("<div style='text-align: justify'><p>Les travaux pour la construction de la cathédrale de Milan ont commencé lorsque le gothique des cathédrales avait maintenant atteint sa floraison maximale, en 1386, avec la décision de la fonder là où se trouvaient les anciennes basiliques de Santa Maria Maggiore et Santa Tecla. A l'initiative de Napoléon, à la veille de son sacre comme roi d'Italie, des travaux sont entrepris pour achever la façade (1807-1813).</p></div>", unsafe_allow_html=True)
    loc_duomo="https://www.google.com/maps/dir/48.8866182,2.3357255/Il+duomo+milano/@46.8969954,1.2413364,6z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x4786c6aec34636a1:0xab7f4e27101a2e13!2m2!1d9.1919265!2d45.4640976"
    url_duomo = "https://ticket.duomomilano.it/"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_duomo)
    
    st.write("Cliquez ici pour acheter les billets : [link](%s)" % url_duomo)
    
    st.markdown("""---""")
    
    st.subheader("Castello Sforzesco")
    st.markdown("<div style='text-align: justify'><p>Le château Sforzesco, l'un des monuments les plus importants de Milan, a connu, au cours de son histoire, de longues vicissitudes constructives, des démolitions brutales, des reconstructions, des embellissements et des restaurations, devenant un symbole des moments historiques heureux et dramatiques de la ville. Il a été construit comme forteresse défensive entre 1360 et 1370. Le Castello dei Visconti a un plan carré, avec un côté de 180 mètres et quatre tours d'angle. Aujourd'hui le Château est destiné à abriter musées et bibliothèques, assumant la fonction culturelle et publique.</p></div>", unsafe_allow_html=True)
    loc_castello="https://www.google.com/maps/dir/48.8866182,2.3357255/Castello+Sforzesco/@46.8969954,1.2413364,6z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x4786fcb60ea97b3d:0x6556dd66c472c29b!2m2!1d9.1793325!2d45.4704762"
    url_castello = "https://www.milanocastello.it/it/content/orari-e-biglietteria"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_castello)
    
    st.write("Cliquez ici pour acheter les billets : [link](%s)" % url_castello)
    
    st.markdown("""---""")
    
    st.subheader("I Navigli")
    st.write("<div style='text-align: justify'><p>Les Navigli de Milan sont un système de canaux navigables qui traverse la capitale lombarde. Autrefois carrefour pour le transport de marchandises, les Navigli s'étendent sur des kilomètres reliant Milan au lac Majeur, au lac de Côme, au fleuve Pô (et donc au débouché sur l'Adriatique) et à la région du Tessin, qui à son tour reliait l'Italie au voie navigable vers l'Europe du Nord.</p></div>", unsafe_allow_html=True)
    loc_navigli="https://www.google.com/maps/d/viewer?mid=1y1jkzabLqULL8L2QGcQP5ANvdOU&hl=en&ll=45.45812883271766%2C9.184355500000011&z=15"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_navigli)
    
    st.markdown("""---""")
    
    
    
    st.subheader("Les rues du shopping :handbag: ")
    st.subheader("Corso Venezia ")
    st.markdown("<div style='text-align: justify'><p>Corso Venezia est l'ancien Corso di Porta Orientale, un axe routier qui reliait le centre-ville au port du même nom (l'actuelle Porta Venezia), d'où partaient les routes vers Bergame et Monza. Actuellement, la rue abrite diverses boutiques de mode, ainsi que des banques et diverses assurences.</p></div>", unsafe_allow_html=True)
    loc_corso = "https://www.google.fr/maps/place/Corso+Venezia,+Milano+MI,+Italie/@45.4709597,9.1992754,17z/data=!3m1!4b1!4m5!3m4!1s0x4786c6bbc46abb41:0xf3cc7c4d05d2a2d4!8m2!3d45.470956!4d9.2014694"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_corso)
    
    st.markdown("""---""")
    
    
    st.subheader("Corso Buenos Aires ")
    st.markdown("<div style='text-align: justify'><p>Corso Buenos Aires est une importante rue commerçante de Milan et l'une des plus longues promenades commerçantes d'Europe.</p></div>", unsafe_allow_html=True)
    loc_buenos = "https://www.google.fr/maps/place/Corso+Buenos+Aires,+Milano+MI,+Italie/@45.4745284,9.2029516,17z/data=!3m1!4b1!4m5!3m4!1s0x4786c6c21f782a6d:0x5cd188c1c1213502!8m2!3d45.4745247!4d9.2051456"
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_buenos)
    
    st.markdown("""---""")
    
    
    st.subheader("Via Monte Napoleaone ")
    st.markdown("<div style='text-align: justify'><p>Via Monte Napoleone est une rue du centre de Milan, considérée comme l'un des quartiers les plus luxueux de la ville et l'un des principaux centres commerciaux de prêt-à-porter. Elle se caractérise aujourd'hui par un grand nombre de boutiques et de salons gérés par les maisons de mode les plus importantes et les plus luxueuses. Il forme le soi-disant quartier de la mode avec Via della Spiga, via Manzoni et Corso Venezia.</p></div>", unsafe_allow_html=True)
    loc_monte="https://www.google.fr/maps/place/Via+Monte+Napoleone,+20121+Milano+MI,+Italie/@45.4683375,9.1929391,17z/data=!3m1!4b1!4m5!3m4!1s0x4786c6b046e886ed:0x30dd2847bfbfd4b4!8m2!3d45.4683338!4d9.1951331"
    
    st.write("Cliquez ici pour voir la localisation : [link](%s)" % loc_monte)
    
    st.markdown("""---""")
    
    
    st.subheader("Quoi manger? :spaghetti: ")
    st.write("L’Italie est l’un des pays européen le plus connu pour sa gastronomie. Nous vous présenterons ici quelques plats typiques de la ville de Milan :  " 
             )
    st.markdown("- Colazione all'italiana : c'est un petit déjeuner qui se fait avec un croissaint fourré avec des crèmes (crème patissière, chocolat, pistanche) et bon capuccino.")
    st.markdown("- Cotoletta alla milanese.")
    st.markdown("- Ossobuco.")
    st.markdown("- Risotto alla milanese (en italien allo zafferano). ")
    st.markdown("- Des très gourmandes pâtisseries. ")
    
    
 ### CARTE DES HEBERGEMENTS DE LA BASE DE DONNEES    
    # Carte répertoriant les hébergements de la base de données selon leur localisation 
elif rad == "Map":
    ### MAP GENERAL POUR TOUS LES HEBERGEMENTS
    st.header('Map des hotels à Milan :globe_with_meridians: ')
    st.markdown('Pour ne pas vous y perdre, nous vous offrons une carte répertoriant tous les hôtels disponibles pour votre séjour.')
    fig = px.scatter_mapbox(data_frame=df, 
                        lat='lat', 
                        lon='long', 
                        color='prix', 
                        size='prix',
                        hover_name='prix',
                        zoom=11,
                        color_continuous_scale=px.colors.sequential.Plasma)
    fig.update_layout(mapbox_style="open-street-map", width=800, height=700)
    st.plotly_chart(fig)
    
   
 
### STATISTIQUES DESCRIPTIVES 
 # Présentation de la base de données consolidée    
elif rad == "Statistiques":
    st.subheader("La base de données")
    st.write('Voici les données récupérées à travers le web scrapping de la page booking.com . Le dataset contenait initialement 814 lignes et 14 colonnes. Les colonnes représentent les variables que nous avons choisi :  ')
    st.markdown("- Nom de l'hotel")
    st.markdown("- Type d'hébergement")
    st.markdown("- Emplacement")
    st.markdown("- Accessibilité")
    st.markdown("- Nombre des étoiles (sur 5) ")
    st.markdown("- Note (sur 10)")
    st.markdown("- Prix en euros")
    st.markdown("- Si le petit-déjeuner est compris ou pas")
    st.markdown("- Si l'annulation gratuite est disponible ou pas")
    st.markdown("- Adresse")
    st.markdown("- Latitude et longitude")
    st.markdown("- Lien qui ridige vers la page de l'hotel")
    
    st.write(" A l'issue d'une étape de traitement des données, il nous a paru pertinent d'ajouter les variables suivantes en se basant sur les variables déjà existantes : ")
    st.markdown("- Latitude")
    st.markdown("- Longitude")
    st.markdown("- Près du centre : une variable qui nous indique si l'hotel est près du centre")
    # Affichage de la base de données 
    st.write(df.head())
    
    
    # Réoartition du nombre d'étoiles des hébergements 
    st.subheader("Représentation du nombre d'étoiles")
    st.markdown("<div style='text-align: justify'> Ce type de variable est disponible seulement pour les hotels. Le nombre d'étoile le plus fréquant est 3, ce qui répresente le nombre d'étoile moyen des nos hébergements.</div>", unsafe_allow_html=True)
    counts = df["nb_etoiles"].value_counts().sort_values(ascending=False)
    fig = px.bar(counts, x=counts.index, y=counts.values)
    fig.update_layout(xaxis_title="Nombre d'étoiles", yaxis_title="Fréquence")
    fig.update_layout(showlegend=True, legend=dict(title="Fréquence"))
    fig.for_each_trace(lambda trace: trace.update(text=counts))
    fig.update_traces(
    textposition='outside')
    st.plotly_chart(fig)

    # Répartition des notes des hébergements
    st.subheader("Représentation de la notation")
    st.write("Nous pouvons constater que les hébergement sont plutot bien notés. De plus, nous pouvons voir que la plupart des hébergement ont des notes qui sont comprises entre 8 et 10. La note la plus fréquente est 0 car ces logements sont nouveaux sur Booking et ils ne se sont pas encore vu attribué de note.")
    counts = df["note"].value_counts().sort_values(ascending=False)
    fig = px.bar(counts, x=counts.index, y=counts.values, color=counts.values)
    fig.update_layout(xaxis_title="Note", yaxis_title="Counts of Rating")
    fig.update_layout(showlegend=True, legend=dict(title="Counts of Rating"))
    st.plotly_chart(fig)

    
    # Répartition des types d'hébergements dans la base de données 
    st.subheader("Représentation des différents type d'hébergement")
    st.markdown("<div style='text-align: justify'>Nous pouvons constater que le type d'hébergement le plus fréquent dans la base de donnée est l'appartement :  535 hébergements sur 801 sont des appartements.</div>", unsafe_allow_html=True)
    counts = df["type_hebergement"].value_counts().sort_values(ascending=False)
    fig = px.bar(counts, x=counts.index, y=counts.values)
    fig.update_layout(xaxis_title="Type d'hébergement", yaxis_title="Fréquence")
    fig.update_layout(showlegend=True, legend=dict(title="Fréquence"))
    fig.for_each_trace(lambda trace: trace.update(text=counts))
    fig.update_traces(
    textposition='outside')
    st.plotly_chart(fig)
    
    
    # Distribution du prix des logements 
    st.subheader("Distribution des prix")
    st.markdown("<div style='text-align: justify'>Nous pouvons constater que la distribution est centrée sur 3000 euros mais il y a des observations qui tirent la distribution car leur prix est largement supérieur à la moyenne. Cela s'explique par leur localisation et leur standing.</div>", unsafe_allow_html=True)
    fig = go.Figure(data=[go.Histogram(x=df["prix"], histnorm='probability')])
    fig.update_layout(xaxis_title='Price', yaxis_title='Frequency')
    st.plotly_chart(fig)
    
    
    # Boxplot de la distribution du prix par type d'hébergement 
    st.subheader("Représentation du boxplot pour afficher le prix par type d'hébergement")
    st.markdown("<div style='text-align: justify'>Le box plot nous permet de voir la distribution du prix par rapport à chaque type d'hébergement. Nous pouvons que le type d'hébergement qui ont plus de valeurs aberrantes sont chambre double, appartement et surtout suite. La distribution du prix par rapport au type d'hébergement *suite* est très écartés à cause d'une observation pour laquelle le prix est de  32084 euros. </div>", unsafe_allow_html=True)
    fig = px.box(df, x='type_hebergement', y='prix', labels={'type_hebergement':"Type d'hébergement",'prix':'Prix'})
    st.plotly_chart(fig)
    
    
    

### RECOMMANDATION DE LOGEMENTS SELON LE BUDGET DE L'UTILISATEUR 
elif rad == "Recommandation":
    @st.cache
    # On définit une fonction qui va recommander des hôtels  selon le budget entré par l'utilisateur
    def filter_by_price(df, min_budget, max_budget):
        return df.query("prix >= @min_budget and prix <= @max_budget")
    st.header('Voici la recommandation parfaite pour votre budget!')
    min_budget, max_budget = st.slider("Ton budget est compris entre : ", min(df["prix"]), max(df["prix"]), (min(df["prix"]), max(df["prix"])), step=20)
    st.write('Votre budget est entre :', min_budget, 'et', max_budget)
    hotel_filtered_by_price = filter_by_price(df, min_budget, max_budget)[['nom', 'adresse', 'nb_etoiles', 'prix','note','description', 'lien', 'annulation_gratuite', 'breakfast_inclus', 'pres_du_centre']].sort_values(by=['note', 'prix'], ascending=[False, True])
    
    #Creation des checkbox et des conditions 
    include_annulation = st.checkbox("Annulation gratuite")
    include_petitdej = st.checkbox("Petit-déjeuner inclus")
    pres_centre = st.checkbox("Près du centre")
    
    #Definition des conditions pour l'affichage des résultats 
    if include_annulation and include_petitdej and pres_centre:
        hotel_filtered_by_price = hotel_filtered_by_price[(hotel_filtered_by_price["annulation_gratuite"] == "annulation gratuite") & (hotel_filtered_by_price["breakfast_inclus"] == "petit-déjeuner compris") & (hotel_filtered_by_price["pres_du_centre"] == 1)]
        st.write("Les résultats affichés incluent uniquement les hébergement avec annulation gratuite, petit déjeuner et avec une proximité au centre de Milan.")
    else:
        if include_annulation:
            hotel_filtered_by_price = hotel_filtered_by_price[hotel_filtered_by_price["annulation_gratuite"] == "annulation gratuite"]
        if include_petitdej:
            hotel_filtered_by_price = hotel_filtered_by_price[hotel_filtered_by_price["breakfast_inclus"] == "petit-déjeuner compris"]
        if pres_centre:
            hotel_filtered_by_price = hotel_filtered_by_price[hotel_filtered_by_price["pres_du_centre"] == 1]

        conditions = []
        if include_annulation:
            conditions.append("annulation gratuite")
        if include_petitdej:
            conditions.append("petit déjeuner")
        if pres_centre:
            conditions.append("proximité au centre de Milan")

        if conditions:
            st.write("Les résultats affichés incluent uniquement les hébergement avec: " + " et ".join(conditions) + ".")
        else:
            st.write("Aucune condition supplémentaire n'a été sélectionnée.")
            
    #AFFICHAGE du nombre des logements disponibles sous les conditions choisies par l'utilisateur  
    nb_hotels_filtered = str(hotel_filtered_by_price.shape[0])    
    st.write(" :hotel: Le nombre de logement disponible pour ce budget est : ", nb_hotels_filtered)
    st.write("Les résultats seront affichés par ordre croissant par rapport à la note et par ordre décroissant par rapport au prix. ")
    st.write("---")
    
    
    
    # On définit une fonction qui va afficher sur notre interface les informations des hôtels correspond au budget de l'utilisateur 
    def print_hotel_info(row):
        st.write('**Nom :** ', row["nom"])
        st.write('**Adresse :**', row["adresse"])
        st.write('**Prix :** ', row["prix"])
        st.write('**Note :** ', row["note"])
        st.write('**Nombre étoiles :** ', row["nb_etoiles"])
        st.write(f'<div style="text-align: justify; margin-bottom: 0px"> <p><b>Description:</b> {row["description"]}</p></div>', unsafe_allow_html=True)
        #st.markdown(f'**Description:** <div style="text-align: justify">{row["description"]}</div>', unsafe_allow_html=True)
        lien=row["lien"]
        st.write("Cliquez ici pour voir accès à la page de l'hotel: [link](%s)" % lien)
        st.write("---")
    # Affichage des informations sur les hôtels sélectionnées selon le budget 
    hotel_recommended = hotel_filtered_by_price.apply(print_hotel_info, axis=1)
    
    
# CLUSTERING K-MEANS
else :
    #Creation du datafrme qui contient les variables numériques que nous allons utiliser pour le clustering
    df_clustering = df.loc[:,["prix", "note", "nb_etoiles", "lat", "long"]]
    #constructeur K-Means et entrainement de l'algorithme
    km = KMeans(n_clusters=5,random_state=0).fit(df_clustering)
    #predictions K-Means
    preds = km.predict(df_clustering)
    #création d'une nouvelle colonne dans le dataframe df_clustering qui contient le numero de cluster pour chaque observation
    df_clustering["cluster"] = preds
    
    #CONSTRUCTION DE LA MAP: chaque point est un hotel, la couleur répresente le cluster auquel il est attribue
    cluster_colors = {0: 'red', 1: 'green', 2: 'blue', 3: 'orange', 4:'purple'}
    data = []
    for cluster, color in cluster_colors.items():
        df_cluster = df_clustering[df_clustering['cluster'] == cluster]
        data.append(go.Scattermapbox(
        lat=df_cluster['lat'],
        lon=df_cluster['long'],
        mode='markers',
        marker=dict(size=8, color=color),
        text=df_cluster['cluster'],
        name=f'Cluster {cluster}'
    ))

    layout = go.Layout(
    mapbox_style="open-street-map",
    mapbox=dict(
        zoom=11,
        center=dict(
            lat=df_clustering['lat'].mean(),
            lon=df_clustering['long'].mean()), 
            pitch=0,
            bearing=0
    ),
    showlegend=True, width=800, height=700
)
    #Visualisation de la map  
    fig = go.Figure(data=data, layout=layout)
    st.header("Visualisation des clusters : ")
    st.plotly_chart(fig)
    st.write("---")
    
    #Construction du dataframe qui nous permet d'afficher les nombre d'occurrences et les caracteristiques moyennes pour chaque cluster 
    df_1=df_clustering["cluster"].value_counts()
    df_2=df_clustering["prix"].groupby(df_clustering["cluster"]).mean().round(2)
    df_3=df_clustering["note"].groupby(df_clustering["cluster"]).mean().round(2)
    df_4=df_clustering["nb_etoiles"].groupby(df_clustering["cluster"]).mean().round(2)
    merged_df = pd.concat([df_1, df_2, df_3, df_4], axis=1).sort_index(ascending=True)
    #Affichage du dataframe ci-dessus
    st.table(merged_df)
    
    #INTERPRETATION DES CLUSTERS 
    st.header("Interprétation des clusters : ")
    st.markdown("<div style='text-align: justify'><p>Afin de trouver le nombre optimal de cluster, nous avon utilisé la méthode Elbow qui est aboutit à la conclusion de former 5 clusters. En voulant prendre connaissance des caractéristiques de chaque cluster, nous sommes abouti à la description des profils types suivants : </p></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'><p>- <b>Cluster 0</b> contient 547 observations. Il contient les logements qui ont des prix moyens et les notes moyennes les plus faibles comparé aux autres clusters. Nous pouvons caractériser ces logements comme des logements médiocres.</p></div>",
    unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'><p>- <b>Cluster 1</b> contient 4 observations. Ce clusters contient des logements de luxe avec des prix qui sont compris entre 15000 et 20000 euros mais qui ont également la note moyenne et le nombre d'étoile les plus élevées parmis tous les clusters. Les logements contenus dans le cluster 1 peuvent être considérés comme les meilleurs logements de la base de données par leur haut standing.</p></div> ",
    unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'><p>- <b>Cluster 2</b> contient 29 observations. Il contient des logements qui ont un prix moyen largement supérieur à la moyenne et la note moyenne convenable. Nous pouvons ainsi les classifier comme des logements qui sont relativement agréables, en moyenne.</p></div>",
    unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'><p>- <b>Cluster 3</b> contient 219 observations. Il contient des logements qui ont un prix moyen et une note moyenne d'un bon standing. Nous pouvons caractériser les logements du cluster 3 comme des logements d'une gamme moyenne de par leurs prix et leurs notes respectives.</p></div>",
    unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'><p>- <b>Cluster 4</b> ne contient que 2 observations. Nous pouvons constater que les logements présents qui dans ce cluster sont les logements qui sont les plus chers avec un prix moyen de plus de 22000 euros mais également un nombre d'étoile de 5. Ils sont donc pour les plus fortunées une aubaine en cette haute saison d'été.</p></div>",
    unsafe_allow_html=True)
    st.markdown("Pour conclure, nous pouvons constater que la majorité des hébergements présents dans la carte ci-dessus appartiennent au cluster 0 contrairement au cluster 4 qui ne compte que deux hébergements.")
    
    
    
    



    
    







