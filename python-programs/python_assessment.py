# This is Python problems practice.

# Reverse String
def reverse_string(s):
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string
print(reverse_string('python'))


# # Find the first non-repeating character in a string
def first_non_repeating_char(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print(counts)

    for char in s:
        if counts[char] == 1:
            return char
print(first_non_repeating_char("programming"))

# Check if a string is a palindrome - a string that reads the same forward and backward
def is_palindrome(s):
    # define two pointers
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome("madam"))

# Calculate the frequency of each character in a string
def calculate_freq(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

print(calculate_freq("hello"))

# Remove duplicate characters from a string
string = "programming"
counts = {}
removed_duplicates = ""

for char in string:
    if char not in counts:
        counts[char] = True
        removed_duplicates += char
print(removed_duplicates)

# Remove duplicates from a list without using set()
num_list = [1,2,2,3,4,4]
counts = {}
removed_duplicates_list = []
for num in num_list:
    if num not in counts:
        counts[num] = True
        removed_duplicates_list.append(num)
print(removed_duplicates_list)

# Find the second largest number in a list.
num_list = [10, 20, 5, 30, 25]

first_max = num_list[0]
second_max = num_list[0]

# first find correct first_max
for num in num_list:
    if num > first_max:
        first_max = num

# then find second max
for num in num_list:
    if num != first_max and num > second_max:
        second_max = num

print(second_max)

# Find all duplicates in a list
num_list = [1,2,3,2,4,5,1]
count = {}
duplicates = []

for num in num_list:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for num in count:
    if count[num] > 1:
        duplicates.append(num)
print(duplicates)

# Q. Rotate a list by K positions.
arr = [1, 2, 3, 4, 5]
k = 2

n = len(arr)
k = k % n # reduce full rotations (n steps = same array)

# reverse whole array first
l = 0
r = n - 1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

print("Reversed whole array:", arr)
# reverse first k
l = 0
r = k - 1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

print("Reversed first k:", arr)

# reverse remaining
l = k
r = n - 1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

print("Rotated array output", arr)


# Q. Find the intersection of two lists
def list_intersection(lst1, lst2):
    # Step 1: Map all elements of lst1 into a dictionary lookup table in O(N)
    lookup = {}
    for item in lst1:
        lookup[item] = True

    intersection=[]
    found_in_intersection = {}

    # Step 2: Scan lst2 in O(M) time
    for item in lst2:
        if item in lookup:
            if item not in found_in_intersection:
                intersection.append(item)
                found_in_intersection[item] = True
    return intersection

print(list_intersection([1,2,3,4],[3,4,5,6]))

# Q. Count frequency of elements in a list using a dictionary
def count_frequency(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

print(count_frequency([1,2,2,3,3,3]))

# Q. Find the key having the maximum value.
# Example: {“A”:100,“B”:500,“C”:300}
def find_max_value(d):
    max_val = 0
    max_key = ''

    for key in d:
        if d[key] > max_val:
            max_val = d[key]
            max_key = key
    return max_key
print(find_max_value({'A':100,'B':500,'C':300}))

# Q. Reverse a dictionary.
# Example: {“a”:1,“b”:2}
# Output: {1:“a”,2:“b”}
def reverse_dict(d):
    reversed = {}
    for key in d:
        value = d[key]
        reversed[value] = key
    return reversed
print(reverse_dict({'a':1,'b':2}))

# Merge two dictionaries.
# Example: d1={“a”:1} d2={“b”:2}
# Output: {“a”:1,“b”:2}
def merge_dict(d1, d2):
    merged = {}
    for key in d1:
        merged[key] = d1[key]
    for key in d2:
        merged[key] = d2[key]
    return merged
print(merge_dict({'a': 1}, {'b': 2}))

# Count word frequency in a sentence using dictionary.
# Example: Input: “python is good python is easy”
# Output: { “python”:2, “is”:2, “good”:1, “easy”:1 }
def count_word_freq(sentence):
    words = []
    current_word = ""
    for char in sentence:
        if char == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word != "":
        words.append(current_word)

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

print(count_word_freq("python is good python is easy"))

# Q.Print the following pattern:
#    **
rows = 1
cols = 2

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()

# Q. Multiplication Table
n=5
for i in range(1, 11):
        print(str(n) + " x " + str(i) + " = " + str(n * i))

# Factorial
n = 5
result = 1
for i in range(1, n + 1):
    result *= i
print(result)

# Prime Numbers
def find_primes():
    primes = []
    for num in range(2, 101):
        is_prime = True

        # Optimization: We only need to check up to i * i <= num
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            primes.append(num)
    return primes

print(find_primes())

# Fibonacci series
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]
    for i in range(2, n):
        next_term = series[i - 1] + series[i - 2]
        series.append(next_term)
    return series

print(fibonacci(8))

# Q21
# Find the first non-repeating number in a list.
# Input: [1,2,3,4,5,1,2,3]
def first_non_repeating_num(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num in lst:
        if counts[num] == 1:
            return num
    return None

print(first_non_repeating_num([1,2,3,4,5,1,2,3]))

# Q22
# Find the Nth non-repeating number in a list.
# Input: [1,2,3,4,5,1,2,3] N = 2

def nth_non_repeating_num(lst, n):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    non_repeating = []
    for num in lst:
        if counts[num] == 1:
            non_repeating.append(num)

    unique_count = 0
    for _ in non_repeating:
        unique_count += 1

    if unique_count >= n:
        return non_repeating[n - 1]
    return None

print(nth_non_repeating_num([1,2,3,4,5,1,2,3], 2))


def are_anagrams(s1, s2):
    # O(N) frequency calculation
    counts1 = {}
    for char in s1:
        if char in counts1:
            counts1[char] += 1
        else:
            counts1[char] = 1

    # O(M) frequency calculation
    counts2 = {}
    for char in s2:
        if char in counts2:
            counts2[char] += 1
        else:
            counts2[char] = 1

    # O(1) character validation dictionary checks
    for key in counts1:
        if key not in counts2 or counts1[key] != counts2[key]:
            return False

    for key in counts2:
        if key not in counts1:
            return False

    return True

print(are_anagrams('listen','silent'))


def find_missing_number(lst):
    max_val = 0
    for num in lst:
        if num > max_val:
            max_val = num

    # expected sum formula
    expected_sum = (max_val * (max_val + 1)) // 2

    # actual sum pass
    actual_sum = 0
    for num in lst:
        actual_sum += num

    return expected_sum - actual_sum

print(find_missing_number([1,2,3,5]))

# Q25
# Find top occurring element in a list.
# Input: [1,2,2,3,3,3,4]
# Output: 3
def top_occurring(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    max_key = None
    max_val = 0
    for key in counts:
        if counts[key] > max_val:
            max_val = counts[key]
            max_key = key

    return max_key

print(top_occurring([1,2,2,3,3,3,4]))