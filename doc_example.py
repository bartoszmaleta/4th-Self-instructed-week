
def word_lengths(sentence):
    '''
    Returns a list with lengths of all words in a stence.

    >>> word_lengths('Hello world')
    [5, 5]
    >>> word_lengths('Once upon a midnight dreary')
    [4, 4, 1, 8, 6]
    '''

    words = sentence.split()
    return [len(word) for word in words]


def count_negative(numbers):
    '''
    Count how many numbers in the given sequence are negative.

    >>> count_negative([])
    0
    >>> count_negative([1, 2, 3])
    0
    >>> count_negative([-1, -2, -3])
    3
    >>> count_negative([10, -10, -10, 10, 10, -20, -30, 0])
    4
    '''
    count = 0
    zero = 0
    if len(numbers) < 0:
        return zero
    else:
        for element in numbers:
            if element < 0:
                count += 1
    
    return count


empty_list = []
print(count_negative(empty_list))

numbers = [1, 2, 3]
print(count_negative(numbers))

numbers2 = [-1, -2, -3]
print(count_negative(numbers2))