class Normalizer:

    def normalize(self, input_data):
        return dict((item["name"], item[list(filter(lambda i: "Val" in i, item.keys()))[0]]) for item in input_data)