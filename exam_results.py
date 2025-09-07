'''Dolores has prepared 4 versions of a multiple choice exam. She has numbered the versions 111, 333, 555, 777. The class management system that she uses chooses a version randomly for a student. After 
all students have completed their version of the quiz, the system generates a file called reponses.txt that has the student's name, the version number they attempted and the responses to the questions
in the quiz. The format of this file is as follows:

Ron 111 A B A C D
Benjamin 333 B A B D C
Fred 555 A C B D C
Amanda 777 A B C D D
Hermione 111 A B C D E

Dolores has created another file called keys.txt that has the correct answers for all four versions of the exam. The format of this file is as follows:

111 A B C D E
333 D C B A E
555 A A B D E
777 B C D A E

Dolores wants to write a program that uses the two files to generate a version wise report. For each version, the report should list the names of the students who attempted the version, their responses
and the score they received.
+--------------------------+
|Version 111 Key: A B C D E|
+--------------------------+
Ron A B A C D 2/5
Hermione A B C D E 5/5
+--------------------------+
|Version 333 Key: D C B A E|
+--------------------------+
Benjamin B A B D C 1/5
Harry D C B A E 5/5
Andy D C B A E 5/5
+--------------------------+
|Version 555 Key: A A B D E|
+--------------------------+
Fred A C B D C 3/5
James A A B D E 5/5
+--------------------------+
|Version 777 Key: B C D A E|
+--------------------------+
Amanda A B C D D 0/5
Timothy B C D A E 5/5
Parvati B C D A E 5/5
'''
def main():
    filename1 = 'responses.txt'
    filename2 = 'keys.txt'

if __name__ == '__main__':
    main()
