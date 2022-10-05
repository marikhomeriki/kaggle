class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'


santa = Sleigh()
print(santa.authenticate("santa", "claus"))
