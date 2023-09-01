# This is a sample Python script.
import biased_flipper
import unbiased_flipper

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gameMode = input("Biased or Unbiased")
    num = input("How many times?")

    if gameMode == "Unbiased":
        unbiased_flipper.coinFlip(int(num))
    else:
        biased_flipper.coinFlip(int(num))


