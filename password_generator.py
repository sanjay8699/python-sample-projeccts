import random
char = int(input('how many characters do you want'))
num = int(input("how many numbers do you want"))
sym = int(input("how many symbols do you want"))
if char <= 26:
    if num <= 9:
        if sym <= 12:
            alpha = "abcdefghijklmnopqrstuvwxyz"
            pass_char = random.sample(alpha, k=char)
            char_password = ""
            for i in range(0, char):
                char_password += pass_char[i]

            numbers = "0123456789"

            pass_num = random.sample(numbers, k=num)
            num_password = ""
            for i in range(0, num):
                num_password += pass_num[i]

            symbols = "!@#$%^&*()_-"
            pass_sym = random.sample(symbols, k=sym)
            sym_password = ""
            for i in range(0, sym):
                sym_password += pass_sym[i]
            password = char_password + num_password + sym_password
            print("".join(random.sample(password, k=len(password))))

        else:
            print("enter valid num")
    else:
        print("enter valid num")
else:
    print("enter valid num")
