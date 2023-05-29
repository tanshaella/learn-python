grade = int(input('Please enter a grade: '))

if(0 <= grade <60):
        print(grade, 'is F')
else:
        if(60 <= grade < 70):
                print(grade, 'is D')
        else:
                if(70 <= grade < 80):
                        print(grade, 'is C')
                else:
                        if(80 <= grade < 90):
                                print(grade, 'is B')
                        else:
                                if(90 <= grade < 100):
                                        print(grade, 'is A')
                                else:
                                        print(grade, 'is an invalid grade')
