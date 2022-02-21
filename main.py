from hashcode_parser.parse_description import *
from hashcode_parser.parse_hashcode_input import *


def solve_ignore_dislikers(description_file, input_file, output_file):
    print(f'Solving input {input_file} to {output_file}... ', end='')

    # Parse input
    description = parse_description(description_file)
    input_parsed = parse_hashcode_input(input_file, description)

    # Dumb solving :
    # Put on pizza all ingredients required by the clients that don't dislike anything.
    # Ignore all other clients.
    ingredients_to_use = set()
    for client in input_parsed["clients"]:
        if int(client["nb_dislikes"]) == 0:
            for like in client["likes"]:
                ingredients_to_use.add(like["ingredient"])

    f = open(output_file, "w")
    f.write(str(len(ingredients_to_use)))
    f.write(' ')
    f.write(' '.join(ingredients_to_use))
    f.write('\n')
    f.close()

    print("Done")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve_ignore_dislikers("hashcode_parser/descriptions/2022_practice.desc",
                           "inputs/a_an_example.in",
                           "outputs/a_an_example.out")
    solve_ignore_dislikers("hashcode_parser/descriptions/2022_practice.desc",
                           "inputs/b_basic.in",
                           "outputs/b_basic.out")
    solve_ignore_dislikers("hashcode_parser/descriptions/2022_practice.desc",
                           "inputs/c_coarse.in",
                           "outputs/c_coarse.out")
    solve_ignore_dislikers("hashcode_parser/descriptions/2022_practice.desc",
                           "inputs/d_difficult.in",
                           "outputs/d_difficult.out")
    solve_ignore_dislikers("hashcode_parser/descriptions/2022_practice.desc",
                           "inputs/e_elaborate.in",
                           "outputs/e_elaborate.out")



