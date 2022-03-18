from GnatScript.gs import run
from colorama import Fore


##
# gShell
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.1


print(Fore.GREEN + "GnatScript 0.1.0\n")
print(Fore.RESET)

while True:
    text = input('>>> ')
    result, error = run("gShell", text)

    if error:
        print(Fore.RED + error.toString())
        print(Fore.RESET)
    else:
        print(result)