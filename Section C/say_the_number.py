def read_number(input_number):
    """Read the number given from the argument passed into the function's parameter
    
    :param int input_number: The number given to read out in text
    
    :returns: The number in words
    :rtype: str"""
    # Create arrays to store the numbers values as words based on the index
    single_numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teen_numbers = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_numbers = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Convert the numeral to an integer
    number = int(input_number)

    # Handle the case when the number is zero
    if number == 0:
        return "zero"

    # Variable to store the words for the number
    words = ""

    # Handle negative numbers
    if number < 0:
        words += "negative "
        number = abs(number)

    # Handle billions
    if number >= 1000000000:
        words += read_number(str(number // 1000000000)) + " billion, "
        number %= 1000000000

    # Handle millions
    if number >= 1000000:
        words += read_number(str(number // 1000000)) + " million, "
        number %= 1000000

    # Handle thousands
    if number >= 1000:
        words += read_number(str(number // 1000)) + " thousand, "
        number %= 1000

    # Handle hundreds
    if number >= 100:
        words += single_numbers[number // 100] + " hundred "
        if number % 100 > 0:
            words += " and "
        number %= 100

    # Handle numbers between 10 and 19
    if number >= 10 and number <= 19:
        words += teen_numbers[number - 10]
        number = 0

    # Handle tens
    if number >= 20:
        words += tens_numbers[number // 10]
        number %= 10

        if number > 0:
            words += "-" + single_numbers[number]
            number = 0

    # Handle single digits
    if number > 0:
        words += single_numbers[number]

    return words.replace("  ", " ")


#In order to see the script in action all one must do is change what number is being given to the
#read_number() function here
print(read_number(10205417))