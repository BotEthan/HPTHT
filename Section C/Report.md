# Worst-case **space** complexity
In the recursive calls, additional space is required to store the intermediate results of the recursive calls on the call stack. The amount of space used on the call stack depends on the depth of the recursion, which is determined by the number of digits in the input number.

Let's consider the worst-case scenario where the input number has n digits. In this case, the depth of recursion would be n, as each recursive call processes one digit of the number.

At each level of recursion, additional space is used to store local variables, including the words variable. The maximum space required on the call stack occurs when the recursion reaches the smallest unit (single-digit numbers) before returning back to the original call.

Therefore, the worst-case space complexity of the read_number function is O(n), where n represents the number of digits in the input number. This space complexity accounts for the space used by the arrays (single_numbers, teen_numbers, tens_numbers), the words variable, and the call stack during the recursive calls.