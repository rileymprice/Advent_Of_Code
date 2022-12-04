given = "LHLRlCCvCLVgHPfCHtVjBGrBDNzWFBsBGBfscGsD"


def num_convert(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


ruck_size = int(len(given) / 2)
first = given[0:ruck_size]
second = given[ruck_size:]
print(len(given), len(first), len(second))
for letter in first:
    if letter in second:
        print(f"Found one: {letter}, {num_convert(letter)}")
