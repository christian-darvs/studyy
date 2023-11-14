from math import e
from tkinter import NO, W


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        x = int(input("Enter element to be added: "))
        new = Node(x)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is None")
        elif self.top.next is None:
            print(f"Popped Element: {self.top.data}")
            print("-----------------------")
            self.top = None
        else:
            temp = self.top
            print(f"Popped Element: {self.top.data}")
            print("-----------------------")
            self.top = temp.next
            temp = None

    def display(self):
        if self.top is None:
            print("Stack is empty")
            print("-----------------------")
        else:
            print("Elements of the stack: ")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print(f"Top of the stack: {self.top.data}")


def display_menu():
    print("Enter the option below")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit\n")


def main():
    stack = Stack()
    while True:
        display_menu()
        option = int(input("Enter Option: "))
        if option == 1:
            print("PUSH")
            print("----------")
            stack.push()
        elif option == 2:
            print("POP")
            print("----------")
            stack.pop()
        elif option == 3:
            print("DISPLAY")
            print("----------")
            stack.display()
        else:
            break


if __name__ == "__main__":
    main()
