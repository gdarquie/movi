import json

class Parser:
    def __init__(self, rawfile, output):
        self.rawfile = rawfile
        self.output = output

    def execute(self):
        input = open(self.rawfile, "r")
        content = input.read()

        output = open(self.output, 'w')
        # get file content
        result = json.loads(content)
        contents = result['contents']
        for film in contents:
            title = film['title'][0]['value']
            genre = film['subtitle']
            image = film['imageurl']
            line = title + ';' + genre + ';' + image + ';' + '\n'
            print(line)
            output.write(line)

        output.close()
