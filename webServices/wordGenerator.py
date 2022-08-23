from nltk.corpus import wordnet2021

class Generator:
    words = set()

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def generateSynonyms(key: str) -> set:
        synonyms = {key}

        for syn in wordnet2021.synsets(key):
            for lm in syn.lemmas():
                synonyms.add(lm.name())

        return synonyms


    def generateWords(self, keys:set) -> None:
        for el in keys:
            self.words |= Generator.generateSynonyms(el)
        self.words |= keys

    def addKey(self, key: str) -> None:
        self.words |= Generator.generateSynonyms(key)

    def removeKey(self, key: str) -> None:
        synonyms = Generator.generateSynonyms(key)
        self.words = [word for word in self.words if word not in synonyms]

    def generateCSV(self, path: str) -> None:
        try:
            with open(path, "w") as f:
                f.write("words" + ";\n")
                f.write(";\n".join(self.words))
                f.close()
                return True
        except:
            return False



