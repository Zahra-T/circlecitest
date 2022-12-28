# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Test:
    def t1(self):
        pass


class ChildTest(Test):
    def t1(self):
        super().t1()


def print_by(name):
    print(f"By, {name}")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == "__main__":
    print_hi("PyCharm")
    print_by("PyCharm")
