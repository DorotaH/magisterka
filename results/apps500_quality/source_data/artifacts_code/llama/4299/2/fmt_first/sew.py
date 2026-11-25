# Read the number of pencils from standard input
N = int(input())

# Convert the number to a string to easily access the digit in the one's place
N_str = str(N)

# Determine the pronunciation of "本" based on the digit in the one's place
if  N_str[-1] in  ["2", "4", "5", "7", "9"]:
    print("hon")
elif  N_str[-1] in  ("0", "1", "6", "8"):
    print("pon")
elif  N_str[-1]=="3":
    print("bon")