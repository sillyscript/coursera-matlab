#Question: We borrowed $1000 at a 10% annual interest rate. If we did not make a payment for two years, and assuming there is no penalty for 
#non-payment, how much do we owe now? Assign the result to a variable called debt.

borrowed=1000;
first_interest= 0.1*borrowed;
new_borrowed = first_interest + borrowed;
second_interest= 0.1*new_borrowed;
debt = new_borrowed + second_interest;
disp(debt)
