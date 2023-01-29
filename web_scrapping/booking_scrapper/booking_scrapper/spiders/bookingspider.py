# Importation des librairies standards
import scrapy


# Création d'une classe donnant les méthodes et attributs de notre webscrapping
class BookingSpider(scrapy.Spider):
    url: str
    name = 'booking'
    # On précise le lien à scrapper
    base_url = "https://www.booking.com/searchresults.fr.html?dest_id=-121726;offset={" \
               "offset};dest_type=city&checkin=2023-08-04&checkout=2023-08-20 "

    def start_requests(self):
        # On installe un user-agent pour essayer de pouvoir scrapper librement
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.82 Safari/537.36'}
        # Gestion des erreurs de redirections
        meta = {'dont_redirect': True, 'handle_httpstatus_list': [302], 'exception': False}

        # On itère sur chaque page de notre url
        for offset in range(0, 1000, 25):
            url = self.base_url.format(offset=offset)
            yield scrapy.Request(url=url, headers=headers, meta=meta, callback=self.parse)

    # Création de la fonction parse qui va aller extraire des elements du site booking.com de la page de resultat
    def parse(self, response):
        hotels = response.xpath(".//div[@class='d20f4628d0']")
        # Création d'un dictionnaire qui va contenir les informations de chaque hotel
        hotel_data = {}
        # On recupere les informations relatives à chaque hôtel present sur la page principale
        for hotel in hotels:
            hotel_data['nom'] = hotel.xpath(
                ".//div[@class='fcab3ed991 a23c043802'][@data-testid='title']/text()").get()
            hotel_data['type_hebergement'] = hotel.xpath(".//span[@class='df597226dd']/text()").get()
            hotel_data['emplacement'] = hotel.xpath(
                ".//span[@class='f4bd0794db b4273d69aa'][@data-testid='address']/text()").get()
            hotel_data['accessibilite'] = hotel.xpath(
                ".//span[@class='f4bd0794db']/span/span[@data-testid='distance']/text()").get()
            hotel_data['nb_etoiles'] = hotel.xpath(".//div[@class='e4755bbd60']/@aria-label").get()
            hotel_data['note'] = hotel.xpath(".//div[@class='b5cd09854e d10a6220b4']/text()").get()
            hotel_data['prix'] = hotel.xpath(".//span[@class='fcab3ed991 fbd1d3018c e729ed5ab6']/text()").get()
            hotel_data['breakfast_inclus'] = hotel.xpath(".//span[@class='e05969d63d']/text()").get()
            hotel_data['annulation_gratuite'] = hotel.xpath(".//div[@class='d506630cf3']//text()").get()
            hotel_data['lien'] = hotel.xpath(".//a[@class='e13098a59f']/@href").get()

            # On récupère les liens de chaque hôtels afin de les parcourir et y extraire des informations
            current_hotel_page = hotel.xpath(".//a[@class='e13098a59f']/@href").get()
            yield scrapy.Request(current_hotel_page, self.parse_hotel, meta={'hotel_data': dict(hotel_data)})

    # # On va récupérer des éléments spécifiques à chaque hôtel sur leurs pages respectives
    def parse_hotel(self, response):
        hotel_data = response.meta.get('hotel_data')
        hotel_data['adresse'] = response.xpath('.//*[@id="showMap2"]/span[1]/text()').get()
        hotel_data['description'] = response.xpath('.//*[@id="property_description_content"]').get()
        hotel_data['long_lat'] = response.xpath('.//*[@id="hotel_address"]').get()
        # On récupère l'ensemble des informations de chaque hôtel dans le dictionnaire hotel_data
        yield hotel_data
