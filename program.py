class Program:
    def __init__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')
        self.n = n
        
    def print_fibonacci_series(self):
        """Prints the Fibonacci Series for Program"""
        # Message
        print(f"\nFibinacci Series for n={self.n}: \n")
        # Set values
        array = [0] * int(self.n + 1)

        # Handle the base cases
        if self.n == 0:
            print(array)
        elif self.n == 1:
            array[1] = 1
            print(array)
        else: 
            array[1] = 1
            for i in range(2, self.n + 1):
                # Compute the next Fibonacci number, remember the previous one
                previous1 = array[i - 1]
                previous2 = array[i - 2]
                array[i] = previous1 + previous2
                
            # We have our arrays - 
            print(array)
            print(f"\nNotice how the 2 preceeding numbers add up to the value at n! ({array[self.n - 2]} + {array[self.n - 1]} = {array[self.n]})")


        # At end, 1 more print
        print(f"\nEnd of Fibinacci Series for n={self.n}: \n")
        
if __name__ == '__main__':
    user_input_int = int(input("What do you want the n value to be for this Fibonacci Series? ")) # wrapping in int() forces the input to be an Integer
    main = Program(n=user_input_int)
    main.print_fibonacci_series()
    
