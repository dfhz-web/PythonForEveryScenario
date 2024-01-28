def hello(name, lang):
    greetings ={
        "English" : "Hello",
        "Spanish" : "Hola",
        "French"  : "Bonjour",
        "German"  : "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == "__main__":
    import argparse 
    parser = argparse.ArgumentParser(
                        prog='Code Pulse innovations ',
                        description='software development',
                        epilog='Support 24/7'

    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="acknowledging company growing forward"
    )
    parser.add_argument(
        "-l", "--lang", metavar='Language',
        required=True, choices=["English","Spanish","French","German"],
        help="language for the greeting"
    )

    args = parser.parse_args()

    hello(args.name, args.lang)