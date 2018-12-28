# Array and Strings 
This section contains a discussion of solutions to interview questions on arrays and strings. 

## Questions One
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

### Approaches:
1. The most abvious approach is to campare each character in the string with every other character in the string. This will take O(n\*\*2) time and and O(1) space. This approach in implemented as *isUniqueChars1(string)* in the file **question1.py**. 

2. Another approach is to check the if the number of all unique characters is equal the length of the string. This will take O(n\*\*2) time and O(n) space. This approach in implemented as *isUniqueChars2(string)* in the file **question1.py**. 

3. Another approach is to assuming that the string is in ascii and therefore there are 256 unique characters in the alphabet. Therefore is the length of the string is greater than 256 the string definitely has duplicate characters. In the case where the length is less than 256, create a list of 256 0's. If you encounter a character in that position, check whether the value is 1. If the value is 1 return true otherwise place 1 in that position. This will have a time complexity of O(n) and a space complexity of O(1). This approach in implemented as *isUniqueChars3(string)* in the file **question1.py**. 


## Question Two
Implement a function void reverse(char* str) in C/C++ which reverses the a null-terminated string.

### Approach:
If you have never used C/C++ it might come as a surprise to you that the strings you are fond of using in java, python and other high level programming languages are implemented using arrays. Strings are arrays of characters.

Steps:
1. Get a pointer of the last character of the string before the null-pointer.
2. Swap character from start of the string with end of the string

Checkout the implementation in the file **question2.h**.

## Question Three
Given two strings, write a method to decide if one is a permutation of the other.

### Approach:
This definitely has more than one approach - try to figure out other approaches :stuck_out_tongue_closed_eyes:

The basic knowledge we have of this question is that a permutation of a word will have the same exact characters and character counts. The difference is that the characters are in different orders.

1. The most abvious approach is to sort the characters of the two strings. The resulting sorted lists should be identical including the length. Checkout the implementation in file **question3.py**.


## Question Four
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the 'true' length of the string. (Note: if implementing in Java/Python, please use a character array so that you can perform this operation in place)

### Approach:
Python strings are iimmutale so we will use a list of characters to implement this:
Steps:
1. Scan the list of characters to get the number of spaces we have. This is useful so that we can calculate the length of the final string. Remember, each space character will be replaced by three characters: '%', '2', '0'.
2. Scan the list again this time replacing the space with three characters


## Question Five