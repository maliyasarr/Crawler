class Store:

    def __init__(self, data):
        self.data = data

    def storingData(self):
        import json
        with open('data.txt', 'w') as outfile:
            json.dump(self.data, outfile, sort_keys=True, indent=4,
                      ensure_ascii=False)
