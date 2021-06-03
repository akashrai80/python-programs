file = input("enter file name :")

# function for word count
def count_word(file_name):
    # open file
    f = open(file_name, "r")
    total_words = 0

    # reterive lines from file
    for line in f:
        word = True

        # reterive letters from line
        for letter in line:
            # count words
            if (letter != " " and letter != "," and letter != ", ") and word == True:
                total_words+=1
                word = False

            # check for spaces, commas in line
            elif letter == " " or letter == "," or letter == ", ":
                word = True
    return ("Total words in {} : {}".format(file_name, total_words))


print(count_word(file))
