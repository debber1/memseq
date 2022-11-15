# A script by Robbe Decapmaker
# Find this script on github: https://github.com/debber1/memseq
# This file produces a memory sequence for the DDC course in GroupT based on a given string.
# Every character gets mapped to a binary address which points to the base address of a 16x32 space in memory.
# Just run this file and enter the characters you want.
# Replace the adresses stored in hello_world.mem with the output of this script
# NOTE: There is a bug in vivado! If you change the contents of hello_world.mem, it will not change the mapping on the actual FPGA. You have to load a new file e.g. 'test.mem' and point your screenbuffermemory to it :)
# If you have a problem, just submit an issue!

character= {
        " ":0,
        "!":1,
        "\"":2,
        "#":3,
        "$":4,
        "%":5,
        "&":6,
        "'":7,
        "(":8,
        ")":9,
        "*":10,
        "+":11,
        ",":12,
        "-":13,
        ".":14,
        "/":15,
        "0":16,
        "1":17,
        "2":18,
        "3":19,
        "4":20,
        "5":21,
        "6":22,
        "7":23,
        "8":24,
        "9":25,
        ":":26,
        ";":27,
        "<":28,
        "=":29,
        ">":30, 
        "?":31, 
        "@":32, 
        "A":33, 
        "B":34, 
        "C":35, 
        "D":36, 
        "E":37, 
        "F":38, 
        "G":39, 
        "H":40, 
        "I":41, 
        "J":42, 
        "K":43, 
        "L":44, 
        "M":45, 
        "N":46, 
        "O":47, 
        "P":48, 
        "Q":49, 
        "R":50, 
        "S":51, 
        "T":52, 
        "U":53, 
        "V":54, 
        "W":55, 
        "X":56, 
        "Y":57, 
        "Z":58, 
        "[":59, 
        "\\":60, 
        "]":61, 
        "^":62, 
        "_":63, 
        "`":64, 
        "a":65, 
        "b":66, 
        "c":67, 
        "d":68, 
        "e":69, 
        "f":70, 
        "g":71, 
        "h":72, 
        "i":73, 
        "j":74, 
        "k":75, 
        "l":76, 
        "m":77, 
        "n":78, 
        "o":79, 
        "p":80, 
        "q":81, 
        "r":82, 
        "s":83, 
        "t":84, 
        "u":85, 
        "v":86, 
        "w":87, 
        "x":88, 
        "y":89, 
        "z":90, 
        "{":91, 
        "|":92, 
        "}":93, 
        "~":94 
        }

string = input('Give a sentence: ')
charlist = list(string.strip())
numberlist = []
for char in charlist:
    numberlist.append(character[char]*32)
print("Length of your sencence: " + str(len(numberlist)))
print("binary encoding:")
output = ""
for number in numberlist:
    output = output + format(number, "b").zfill(12) + "\n" 
print(output)

