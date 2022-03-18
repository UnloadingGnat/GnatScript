from gnatScript.gs import run

##
# gShell
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.1


print("GnatScript 0.1.0\n")

while True:
    text = input('>>> ')
    result, error = run("System.input", text)

    if error:
        print(error.toString())
    else:
        print(result)