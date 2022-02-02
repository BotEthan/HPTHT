# HyperionDev Marketplace Reviewer Take-Home Test

## Welcome

We’re excited to get to know you and your skills better. The next step of the interview process with HyperionDev’s Marketplace Reviewer Network is to complete a
take-home exercise. Please complete this exercise within 2 days of receiving it and make sure your responses are all sent through to the talent@hyperiondev.com
from which you received this assessment unless otherwise specified. 

## Who Are We?

HyperionDev is the largest provider of software development education in Southern Africa, and one of the largest globally. Founded by Riaz Moola in 2012, 
HyperionDev is counted among the top education technology startups in EMEA with headquarters in Cape Town and London. We were originally launched from the 
University of Cambridge, and our leadership team consists of world-leading talent from companies such as Google, Amazon, 2U/GetSmarter, Yoco, Zando and PwC.

HyperionDev was funded by both Facebook and Google in 2017 for its mission. We won first prize in Facebook's Africa Innovation Challenge Award as the top 
edtech startup on the African continent, and in 2020 won the UK government’s Tech Nation top startups award. In 2021, we closed one of the largest Series
 A fundraises in South Africa with nearly 1500 investors backing us in the biggest crowdfunding round in history for an Africa-linked startup. 

We have built an online course platform that allows human code review to be scaled, applying this methodology to help thousands of students from over 40
 countries learn how to code in a novel way. We pioneer effective and affordable software development education with this code review model, lowering 
 the cost of access to tech careers around the world to shrink the tech skills gap and inequality in the tech space. Please ensure you have reviewed our 
 about us page as well. 

## Being a Reviewer

In this role, you will be joining our team of specialist reviewers. Our reviewers are elite, world-leading programming experts with a skill set that is at 
the intersection of technical coding skills. Reviewers work with leading tech partners from around the world in fields as diverse as technical education, 
developer assessment, and tech team peer reviews.

Pursuing reviewing as an opportunity provides a fulfilling way of specializing yourself further while garnering international work experience. It promises a 
promising career path with a trajectory similar to that of a traditional educator and compensation/benefits rivalling those in the software & IT industry. 
Please complete the tasks below to help us understand how your skills may best fit the requirements of our team. 

## Instructions

- Please attempt every section.
- Please select exactly one option for each of Section A and Section C.
- The languages for the options you pick or use for Section A and C should be different.
- Please submit a link to a single publicly accessible GitHub repository that contains your solutions with a folder for each section.
- Please validate user input and handle all errors gracefully.
- No runtime errors or exceptions should be encountered while running your solutions.
- Please provide a README.md file in each section’s folder describing setup and usage where applicable.
- If you deployed or published a solution, please include information about it in the corresponding README.md file, e.g. how to access the running application.
- Please include project files that would automate the installation of your dependencies.
- Please exclude any binaries or generated files, e.g. node_modules.
- Please include tests where possible.
- Please containerise your solutions where possible.
- We will assess your submission based on:
    - The thoroughness of your submission
    - Use of the data provided
    - Creativity
    - Research efforts
    - Presentation
    - Completion within the allocated time

Best wishes!

## Section A: Code Review

This section simulates a typical interaction that you might have with
a student. You will be given a question that a hypothetical student
asks and the student’s submitted code. You will be required to answer 
the question and review their code’s correctness, efficiency, style and
documentation.

### Instructions

- Please present your review in a Markdown file.
- Please refer to line numbers in your review.
- Please review the hypothetical student sumbissions by commenting on
    - Correctness
    - Efficiency
    - Style
    - Documentation
- Please comment on the postive aspects and improvements that are necessary while being encouraging.

### Option 1: Python Task

Compulsory Task 1
Follow these steps:

- In a file called anagram.py, create:

- Given an array of strings strs, group the anagrams together. 
- An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    - You can return the answer in any order.
    - Strings consists of lowercase English letters.
      
- Example input
- Input: strs = ["eat","tea","tan","ate","nat","bat"]
- Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

```Python
class Solution:
       def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted())
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

```

### Option 2: Java Task

Compulsory Task 1
Follow these steps:

- In a file called recursion.java, create:
    - recursive function that reverses a string 
    - a recursive function that, given a number n, prints out the first n Fibonacci numbers (Fibonacci numbers are a sequence where each number is the sum of the previous two - 0 1 1 2 3 5 8...)
    

``` java
public class recursion {
 
	public static void main(String[] args) {
 
		// Saves the string that would be reversed
		String myStr = "emosewA si avaJ";
 
 
		//create Method and pass and input parameter string 
		String reversed = reverse_string(myStr);
		System.out.println("The reversed string is: " + reversed + "\nFibonacci Series of 10 numbers:0 1 1 2 3 5 8 13 21 34 ");
	

	}
 
 
	//Method take string parameter and check string is empty or not
	public static String reverse_string(String myStr)
	{
		if (myStr.isEmpty()){
		 System.out.println("String in now Empty");
		 return myStr;
		}
		//Calling Function Recursively
		System.out.println("String to be passed in Recursive Function: "+myStr.substring(1));
		return reverseString(myStr.substring(1)) + myStr.charAt(0);}

	public static <T> void function(T maxNumber) {
		// Set it to the number of elements you want in the Fibonacci Series
		int maxNumber = 10; 
		int previousNumber = 0;
		int nextNumber = 1;
		 
	    System.out.print("Fibonacci Series of "+maxNumber+" numbers:");
 
	for (int i = 1; i <= maxNumber; ++i){
	    System.out.print(previousNumber+" ");
	    // On each iteration, we are assigning second number
	    // to the first number and assigning the sum of last two
	    // numbers to the second number
	    int sum = previousNumber + nextNumber;
	    previousNumber = nextNumber;
	    nextNumber = sum;
	    }
 
	}
 
}
```

### Option 3: Ruby Task

Compulsory Task 2
Follow these steps:

- Write an algorithm to determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backwards and forwards.
    - The number 121 is a palindrome. From left to right, it reads 121. From right to left, it reads 121.
    - The number -121 is not a palindrome. From left to right, it reads -121. From right to left, it reads 121-.
    -The number 10 is not a palindrome. From left to right, it reads 10. From right to left, it reads 01.

```Ruby
#set a variable reversed to 0 and number to a variable called num to pass into while loop
def is_palindrome(x)
    if x < 0
    false
#the number to reverse does not equal 0 (completely extracted)
#continue extracting the ones value and adding it to the reversed number 
#multiplied by 10 (to move it into the tens value)
# if it’s not in the ones value, since the reversed originally is set to 0, 
# it would place that extracted number in the ones value. thus reversing the integer.
    else 
        reversd = 0
        num = x
        while num != x
            extracted = num%10
#set variable num to num divided by 10, thus getting rid of the ones value since when you just use 
#the division operator in ruby, it does not return the remainder.
            reversed = reversed*10 + extracted
            num=num/10
        end
#Once num value hits 0, the while loop extracted everything and the integer is reversed.
#check the condition. If my reversed integer, does not equal my original integer, the original integer is NOT a palindrome.
        if reversed != x
            false
        else
            true
        end
    end

```


### Option 4: TypeScript Task

Compulsory Task 2
Follow these steps:

- In a file named caesar.ts, please create a function that implements the Caesar Cypher by taking 2 arguments, the string that is to be encoded and the shidt value used for the encryption.
- For more information on what a Cypher Cipher is, please look at the following [resource](https://en.wikipedia.org/wiki/Caesar_cipher)
- The function should return "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX." When the following are passed as arguments:
    - The string to be encoded: "GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."
    - The shift value: 39


``` typescript
//TypeScript Type: Alphabet
type Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

// Function: Caesar Cipher
const caesar_cipher<T> = (string: T, shift: string) => {
  // Alphabet
  const alphabet: Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  // Encoded Text
  let encodedText: string = '';


  if (shift > 26) {
    
    shift = shift % 26; }

 
  let i: number = 0;
  while (i < string.length) {
    // Valid Alphabet Characters
    if (alphabet.indexOf(string[i]) !== -1) {
      // Find Alphabet Index
      const alphabetIndex: number = alphabet.indexOf((string[i]).toUpperCase());

      // Alphabet Index Is In Alphabet Range
      if (alphabet[alphabetIndex + shift]) {
        // Append To String
        encodedText += alphabet[alphabetIndex + shift];
      }
      // Alphabet Index Out Of Range (Adjust Alphabet By 26 Characters)
      else {
        // Append To String
        encodedText += alphabet[alphabetIndex + shift - 26];
      }
    }
    // Special Characters
    else {
      // Append To String
      encodedText += string[i];
    }

    // Increase I
    i++;
  }

  return encodedText;
};

//printing the output to terminal to test for correct output
//should print THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX.
print(caesar_cipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39));

```

## Section B: Projects

### Instructions

- Please share a GitHub URL to a project you're most proud of.
- You may include the link in the repository you are submitting for the test.
- You may have completed it in the past or it may be freshly completed for this test.
- The project could be in any domain using any technology stack.

## Section C: Code Challenge

### Instructions

- We suggest that you implement your solution in either Python, Java, Ruby or TypeScript.
- You're more than welcome to use any programming language and paradigm that you fancy as long as your solution is idiomatic.
- You are required to include a test suite for your solution.
- Please include all instructions and scripts necessary to build, test and run your solution on Linux, macOS and Windows operating systems.
- Please include a Markdown report that specifies and justifies the _worst-case **space** complexity_ of your solution.
- Please attempt any one option of the alternatives available from below:

### Option 1: Say the Number

- https://edabit.com/challenge/4E9gTrRWErpTCA2FQ

### Option 2: Road Navigation

- https://edabit.com/challenge/qQu4kxTEHapogmCgE

### Option 3: Resistor Networks

- https://edabit.com/challenge/eWXL8Jz78hP5tW644

### Option 4: International Standard Book Numbers

- https://edabit.com/challenge/C5mooK3wfdhoooeLw
