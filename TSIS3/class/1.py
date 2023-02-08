class met:

    def getString(self, text):
        return text
    def printSring(self, text):
        print(self.getString(text).upper())
if __name__ == '__main__' :
    som = met()
    som.printSring(som.getString(input()))