import http.client
conn = http.client.HTTPSConnection("api.ocs.fr")
conn.request("GET", "/web/v2/details/programme/AUNOMDEMAFIW0110779")
response = conn.getresponse()
content = response.read()

print("Welcome to Movie")
print(content)
