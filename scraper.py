from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "http://www.southampton.gov.uk/geoserver/wms?LAYERS=SCC%3APOLLING_STATIONS&TRANSPARENT=TRUE&STYLES=Polling_Stations_Labelled&HOVER=false&FORMAT=kml&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&SRS=EPSG%3A27700&BBOX=436000.0,108500.0,448000.0,118000.0&WIDTH=867&HEIGHT=426"
districts_url = "http://www.southampton.gov.uk/geoserver/wms?LAYERS=SCC%3APOLLING_DISTRICTS&TRANSPARENT=TRUE&STYLES=Polling_Districts_Labelled&HOVER=false&FORMAT=kml&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&SRS=EPSG%3A27700&BBOX=436000.0,108500.0,448000.0,118000.0&WIDTH=867&HEIGHT=426"
council_id = 'E06000045'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations', 'kml')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts', 'kml')
districts_scraper.scrape()
