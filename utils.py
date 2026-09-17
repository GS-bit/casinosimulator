import os
import time

def clearscreen() -> None:
    """
    It cleans the screen.
    """
    
    os.system("cls" if os.name == "nt" else "clear")

def write(txt: str, endline: bool = True) -> None:
    """
    It writes a text on the screen. The writing follows a typewriter visual effect.

    Arguments:
        txt: the text
        endline: if True, the text will have an automatic end of line. If False, it won't have it.
    """

    for ch in txt:
        print(ch, end="", flush=True)
        time.sleep(0.025)

    if endline:
        print("")

def read(txt: str = "", _type: str = "STR") -> str:
    """
    It reads a text from the user.

    Arguments:
        txt: a prompt message (optional)
        _type: the type to read ("UINT" for positive integers; otherwise, strings). If it is "UINT", the function will
        persist prompting the user while he/she does not enter something valid.

    Return:
        the text given by the user
    """

    write(txt, False)

    input_value = input()

    if _type == "UINT":
        try:
            input_value = int(input_value)

            if input_value < 0:
                raise Exception
        except:
            write("Invalid format!")

            return read(txt, _type)

    return input_value

def menu(options: list[str]) -> int:
    """
    A menu in which the options are displayed along with a number, asking the user which to select.

    Arguments:
        options: a list of the possible options

    Return:
        int: the chosen option (1, 2, 3...)
    """

    for _id, element in enumerate(options):
        write(f"({_id+1}) {element}")

    op = read("> ")

    try:
        op = int(op)

        if op <= 0 or op > len(options):
            raise Exception
        else:
            return op
    except:
        write("Invalid option!")

        return menu(options)
