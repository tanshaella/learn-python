# Write a program that reads a line of text from the user and prints the number of words in that text.

print("Please enter a line of text:")
line=input()
spaces_count=0
ind=0
while(ind<len(line)):
    curr_char=line[ind]
    if(curr_char==' '):
        spaces_count+=1
    ind+=1
number_of_words=spaces_count+1
print("You typed", number_of_words, "words")
