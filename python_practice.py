#Create a list of 5 numbers, print the leargest number in the list.
numbers = [10, 25, 3, 47, 15]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print("The largest number in the list is:", largest_number)        

#count how many times a word appears in a sentence(dictionary)
sentence ="The quick brown fox jumps over the lazy dog."
word_count = {}
for word in sentence.split():
    word = word.lower().strip('.,!?') 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word count in the sentence:", word_count)

#Reverse a list without using .reverse()
def reverse_list(num):
    rev=[]
    for n in num:
        rev = [n] + rev
    return rev
num =[1, 2, 3, 4, 5]  
print("Reversed list:", reverse_list(num))     

#Merge two dictionaries into one
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

#Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)
print("List with duplicates removed:", unique_numbers)