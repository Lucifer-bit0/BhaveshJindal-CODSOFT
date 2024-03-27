import random
def random_pass_generator(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVLXYZ1234567890!@$%&)(-_=+?/><}]{[|]}"
    passw = ''.join(random.choice(chars) for i in range(length))
    return passw

def main():
    try:
        passw_leng = int(input("Enter the length for your password: "))
        new_generated_pass = random_pass_generator(passw_leng)
        print("Your password is: ", new_generated_pass)
    except ValueError:
        print("Enter a valid number")
main()
