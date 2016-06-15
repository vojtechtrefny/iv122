def read_file(fname):
    string = ""
    with open("cv9/" + fname, "r") as f:
        for line in f:
            string += line

    string = string.replace(" ", "")[:-1]

    return string


def frequency(string):
    """ Basec frequency of numbers """
    res = {}

    for char in string:
        if char not in res.keys():
            res[char] = 1
        else:
            res[char] += 1

    return res


def chi_squared(string):
    """ Chi-squared test: https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test """
    measured = frequency(string)
    expected = len(string) / 6

    return sum([((measured[i] - expected)**2 / expected) for i in measured.keys()])


def pattern_repeating(string):
    """ Are there some repeating patterns? """

    for i in range(2, len(string) // 2):  # substring lenght from 2 to half string length
        for j in range(1, len(string) - i):  # form all substrings of lenght i
            substring = string[j: j + i]
            cnt = string.count(substring)  # count number of substrigs in string

            if cnt * i >= (len(string) // 2):  # repeating pattern takes more than 50 % of the string
                return (substring, cnt)

    return ("", 0)


def permutations(string):
    """ Test if the file is just a sequence of repeating "123456" permutations """

    num_perms = 0

    for i in range(0, len(string) - 6, 6):
        if sorted(string[i:i + 6]) == ["1", "2", "3", "4", "5", "6"]:
            num_perms += 1

    return num_perms


# run tests for all files
for i in range(1, 8):
    string = read_file("random%d.txt" % i)
    print(frequency(string))
    print(chi_squared(string))
    print(pattern_repeating(string))
    print(permutations(string))
