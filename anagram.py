wrd1 = "Race"
wrd2 = "Care"

# convert both the strings into lowercase
wrd1 = wrd1.lower()
wrd2 = wrd2.lower()

# check if length is same
if(len(wrd1) == len(wrd2)):

    # sort the strings
    sorted_str1 = sorted(wrd1)
    sorted_str2 = sorted(wrd2)

    # if sorted char arrays are same
    if(sorted_wrd1 == sorted_wrd2):
        print(wrd1 + " and " + wrd2 + " are anagram.")
    else:
        print(wrd1 + " and " + wrd2 + " are not anagram.")

else:
    print(wrd1 + " and " + wrd2 + " are not anagram.")