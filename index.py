import http.client
from importer import Importer

baseUrl = 'api.ocs.fr'
params = "https://api.ocs.fr/web/v2/rubriques/films?sort=new"

ocs_importer = Importer('ocs')
print(ocs_importer.execute(params))
