def word_count(text):
    """
    This module checks the word count for given text.

    Arguments:
    text - text you want ot analyze.

    Output:
    int - word count for given text.
    """
    count = 1

    for i in text:
        if i == " ": count += 1

    return count

def sentence_count(text):
    """
    This module checks the sentence count for given text.

    Arguments:
    text - text you want to analyze.

    Output:
    int - phrase count for given text.
    """

    count = 0

    for i in text:
        if i == ".": count += 1

    return count

def letter_count(text):
    """
    This module shows you how much you used each letter in a sentence.

    Arguments:
    text - text you want to analyze.

    Output:
    dictionary - number of each letters in given text.
    """

    count = {}

    for i in text:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1

    return count