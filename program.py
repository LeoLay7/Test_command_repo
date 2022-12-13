# I'm author of this program
print("Hello world!!!")


def f():
    string = "!" + "1" * 30 + "2" * 50

    while "!1" in string or "!2" in string:
        if "!1" in string:
            string = string.replace("!1", "221!", 1)
        elif "!2" in string:
            string = string.replace("!2", "22!")

    return sum([int(x) for x in string if x.isdigit()])


def main():

    def func(n):
        bin_num = bin(n)[2:]

        if n % 2 == 0:
            bin_num = '1' + bin_num + '00'
        elif n % 2 == 1:
            bin_num = '10' + bin_num + '1'

        return bin_num

    def to_des(bin_num):
        res = 0
        for i in range(1, len(bin_num) + 1):
            res += int(bin_num[-i]) * 2 ** (i - 1)

        return res

    for i in range(1000):
        a = to_des(func(i))
        if a > 320:
            print(i, '-', a)

