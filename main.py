from PyInquirer import prompt, Separator

running = True


def c_to_f(t):
    return (t * (9 / 5)) + 32


def abv(og, fg):
    result = (76.08 * (og - fg) / (1.755 - og)) * (fg / 0.794)
    return result


def spgr(r, tr, tc):
    a = 1.00130346
    b = 0.0001347221244
    c = 0.00000204052596
    d = 0.00000000232820948

    tr = c_to_f(tr)
    tc = c_to_f(tc)

    cg = r * (
        (a - (b * tr) + (c * pow(tr, 2)) - (d * pow(tr, 3)))
        / (a - (b * tc) + (c * pow(tc, 2)) - (d * pow(tc, 3)))
    )

    return cg


def calculate_abv():
    print("ABV")
    questions = [
        {
            "type": "input",
            "name": "og",
            "message": "Original gravity reading:",
            "validate": lambda val: len(val) != 0 or "Supply a reading",
        },
        {
            "type": "input",
            "name": "fg",
            "message": "Final gravity reading:",
            "validate": lambda val: len(val) != 0 or "Supply a reading",
        },
    ]

    answers = prompt(questions)

    result = abv(float(answers["og"]), float(answers["fg"]))
    print("Calculated ABV: ", result)


def calculate_spgr():
    print("SPGR")

    questions = [
        {
            "type": "input",
            "name": "r",
            "message": "Hydrometer reading:",
            "validate": lambda val: len(val) != 0 or "Supply a reading",
        },
        {
            "type": "input",
            "name": "tr",
            "message": "Temperture at reading (C):",
            "validate": lambda val: len(val) != 0 or "Supply a reading",
        },
        {
            "type": "input",
            "name": "tc",
            "message": "Calibration temperature (C):",
            "default": "20",
            "validate": lambda val: len(val) != 0 or "Supply a reading",
        },
    ]

    answers = prompt(questions)

    cg = spgr(float(answers["r"]), float(answers["tr"]), float(answers["tc"]))
    print("Corrected reading: ", cg)


def main_menu():
    global running

    questions = [
        {
            "type": "list",
            "name": "opts",
            "message": "Main menu",
            "choices": [
                {"name": "Corrected SPGR", "value": "spgr"},
                {"name": "ABV", "value": "abv"},
                Separator(),
                {"name": "Exit", "value": "exit"},
            ],
        }
    ]

    answers = prompt(questions)

    if answers["opts"] == "exit":
        running = False
    elif answers["opts"] == "spgr":
        calculate_spgr()
    elif answers["opts"] == "abv":
        calculate_abv()


if __name__ == "__main__":
    while running:
        main_menu()
