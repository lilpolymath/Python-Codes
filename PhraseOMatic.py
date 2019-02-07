from random import randint
WordListOne = ["24/7", "multi-Tier", "30,000 foot", "B-to-B",
                "win-win", "front-end", "web-based", "pervasive", "smart", "six-sigma",
                "critical-path", "dynamic"]
WordListTwo = ["empowered", "sticky", "value-added", "oriented", "centric", 
                "distributed", "clustered", "branded", "outside-the-box", "positioned", "networked", 
                "focused", "leveraged", "aligned", "targeted", "shared", "cooperative", "accelerated"]
WordListThree = ["process", "tipping-point", "solution", "architecture", "core competency",
                "strategy", "mindshare", "portal", "space", "vision", "paradigm", "mission"]
len1 = len(WordListOne)
len2 = len(WordListTwo)
len3 = len(WordListThree)
rand1 = randint(0,len1)
rand2 = randint(0,len2)
rand3 = randint(0,len3)
phrase = WordListOne[rand1] + " " + WordListTwo[rand2] + " " + WordListThree[rand3]
print("What we need is a " + phrase)