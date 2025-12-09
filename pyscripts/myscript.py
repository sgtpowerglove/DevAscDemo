def main():
    print("Hello, World!")
    print("Welcome to DEVASC!")
    """Example runner for the `Greeter` feature.

    Run as a script::

        python -m pyscripts.myscript

    Or directly on Windows PowerShell:

        python .\pyscripts\myscript.py
    """

    from argparse import ArgumentParser
    from Feature.myfeature import Greeter


    def main() -> None:
        parser = ArgumentParser(description="Run the Greeter example")
        parser.add_argument("name", nargs="?", default=None, help="Name to greet")
        parser.add_argument("--greeting", "-g", default="Hello", help="Greeting prefix")
        args = parser.parse_args()

        greeter = Greeter(greeting=args.greeting)
        print(greeter.greet(args.name))
        print("Current time:", greeter.format_time())


    if __name__ == "__main__":
        main()