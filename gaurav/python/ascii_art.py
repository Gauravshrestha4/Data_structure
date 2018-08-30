import pyfiglet
import termcolor

msg=input("enter the lovely name: ")
color=input("enter the color: ")

print(termcolor.colored(pyfiglet.figlet_format(msg),color=color))