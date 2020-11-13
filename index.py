import http.client
from importer import Importer
from parser import Parser
from datetime import date
import os

baseUrl = 'api.ocs.fr'
params = "https://api.ocs.fr/web/v2/rubriques/films?sort=new"

projectPath = os.getcwd()
savePath = projectPath + "/save/"

if not os.path.exists(savePath):
    os.mkdir(savePath)

today = date.today()
now = today.strftime("%Y-%m-%d")

completePath = savePath + now + '/'
if not os.path.exists(completePath):
    os.mkdir(completePath)

rawOutputFilename = completePath + 'ocs_raw_output_' + now + '.csv'
open(rawOutputFilename, "w")

# # import data from ocs API
ocs_importer = Importer('ocs')
print(ocs_importer.execute(rawOutputFilename, params))

# # format result
outputFilename = completePath + 'ocs_' + now
open(outputFilename, "w")
parser = Parser(rawOutputFilename, outputFilename)
parser.execute()
