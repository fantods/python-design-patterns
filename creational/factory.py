# Creates objects without having to specify the exact class

# Pros:
# allows you to hide application implementation
# easy to test
# easy to modify design

# Cons:
# code is difficult to read, everything is behind an abstraction
# can be an anti-pattern when used incorrectly

class GreekGetter(object):
    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """ignore entries that do not exist in dict"""
        return self.trans.get(msgid, str(msgid))

class EnglishGetter(object):
    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()

eng, greek = get_localizer(language="English"), get_localizer(language="Greek")

for msgid in "dog parrot cat bear".split():
    print(eng.get(msgid), greek.get(msgid))

# outputs:
# dog σκύλος
# parrot parrot
# cat γάτα
# bear bear
