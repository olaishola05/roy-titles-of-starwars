star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A new hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

prequel_titles = star_wars_movies[0]
original_titles = star_wars_movies[1]
sequel_titles = star_wars_movies[2]


def prequel_trilogy(opt):
    for idx, title in enumerate(prequel_titles):
        if opt == 1 and idx == 0:
            print(idx + 1, title)

        elif opt == 2 and idx == 1:
            print(idx + 1, title)

        elif opt == 3 and idx == 2:
            print(idx + 1, title)


def orignial_trilogy(opt):
    for idx, title in enumerate(original_titles):
        if opt == 1 and idx == 0:
            print(idx + 1, title)

        elif opt == 2 and idx == 1:
            print(idx + 1, title)

        elif opt == 3 and idx == 2:
            print(idx + 1, title)


def sequel_triloqy(opt):
    for idx, title in enumerate(sequel_titles):
        if opt == 1 and idx == 0:
            print(idx + 1, title)

        elif opt == 2 and idx == 1:
            print(idx + 1, title)

        elif opt == 3 and idx == 2:
            print(idx + 1, title)
            


def app(option, opt_two):
    if option == "1":
        prequel_trilogy(opt_two)

    elif option == "2":
        orignial_trilogy(opt_two)

    elif option == "3":
        sequel_triloqy(opt_two)
    else:
        print("Invalid Option")


app("3", 2)
