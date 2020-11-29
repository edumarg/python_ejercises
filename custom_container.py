# create a custom container class
class TagCloud:
    def __init__(self):
        self.tags = {}

    def __len__(self):
        return len(self.tags)

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(),0)

    def __setitem__(self, tag, value):
        self.tags[tag.lower()] = value

    def __iter__(self):
        return iter(self.tags)

    def add(self, tag):
        if tag.lower() in self.tags:
            self.tags[tag.lower()] += 1
        else:
            self.tags[tag.lower()] = 1


tags = TagCloud()
tags.add("python")
tags.add("python")
tags.add("python")
tags.add("Python")
tags.add("PYTHON")
tags.add("PyThOn")
tags.add("java")
tags.add("Java")
tags.add("JaVa")
tags.add("JAVA")
print(tags['PYTHON'])
print(tags['JaVa'])
print(tags.tags)
for tag, value in tags.tags.items():
    print(tag, value)
print(len(tags.tags))
tags['java'] = 20
tags['Python'] = 30
print(tags.tags)
tags['JAVA'] = 10
print(tags.tags)
