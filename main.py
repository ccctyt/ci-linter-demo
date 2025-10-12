# main.py - 修复后的版本

def say_hello(name):
    """Greet the user."""
    print("Hello, " + name)
    if True:
        print("This is good indentation")


def long_function():
    """A long line that we break."""
    x = (
        "This is a very long line that exceeds the 79 character limit "
        "recommended by PEP8, so it should trigger a warning or error "
        "when flake8 runs"
    )
    return x


say_hello("World")
