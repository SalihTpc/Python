entry = input("Sentence:")


def letters_count(self):
    counts = dict()
    for i in self:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    return counts


print(letters_count(entry))
