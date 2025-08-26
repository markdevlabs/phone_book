import random
import string



def create_and_add_values():
    code_list = []
    all_letters = string.ascii_letters
    for i in range(0, 5):
        generate_num = random.randint(0, 10)
        generate_letter = random.choice(all_letters)
        code_list.append(generate_num)
        code_list.append(generate_letter)

    print(code_list)


create_and_add_values()

