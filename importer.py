import http.client

class Importer:
    def __init__(self, service):
        self.service = service

    def execute(self, file, params):
        url = ''
        if self.service == "ocs":
            url = 'api.ocs.fr'

        conn = http.client.HTTPSConnection(url)
        conn.request("GET", params)
        response = conn.getresponse()
        content = response.read()

        file = open(file, 'w')
        file.write(content.decode("utf-8"))
        file.close()

        return "Import has been successfully created."
