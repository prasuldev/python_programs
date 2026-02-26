#create a list
my_list = [1,2,0,9,7,6,4,2,1]
#Create an empty dictionary to store the frequency of elements
frequency ={}
#Iterate through the list and count the frequency of each element
for element in my_list:
    if element in frequency:
        frequency[element] +=1
    else:
        frequency[element] = 1
#Print the frequency of each element
for key, value in frequency.items():
    print(f"{key}: {value}")   

         
 #Check if a string is a pangram
#input string
input_string="the quick brown fox jumps over the lazy dog"
#Create a set of all the letters in the input string
letters = set(input_string)
#Create a set of all the letters in the English alphabet
alphabet = set("abcdefghijklmnopqrstuvwxyz")
#Check if the set of letters in the input string is a superset of the alphabet
if letters.issuperset(alphabet):
    print("The input string is a pangram.")
else:    print("The input string is not a pangram.")    