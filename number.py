import statistics
class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return True if number.get_number()%2==0 else False

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return True if number.get_number()%2==1 else False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        return True if number.get_number()%1==0 and number.get_number()%number.get_number()==0 and number.get_number()%2 !=0 else False

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        lst = []
        for i in range(1,number.get_number()+1):
            if number.get_number()%i == 0:
                lst.append(i)

        return lst
    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(number.get_number()))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        lst = []
        for i in str(number.get_number()):
            lst.append(int(i))
        return sum(lst)
       
    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(number.get_number())[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return True if number.get_number() == int(str(number.get_number())[::-1]) else False

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        lst = []
        for i in str(number.get_number() ):
            lst.append(int(i))
        return lst

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(number.get_digits())

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(number.get_digits())

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return sum(number.get_digits()) // number.get_length()

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
       
        return statistics.median(number.get_digits())

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return 

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        total = {}
        for i in set(number.get_digits()):
            total[i] = self.get_digits().count(i)
        
        
        return total

# Create a new instance of Number
number = Number(652134)

print(number.get_number())
print(number.is_odd())
print(number.is_even())
print(number.is_prime())
print(number.get_divisors())
print(number.get_length())
print(number.get_sum())
print(number.get_reverse())
print(number.is_palindrome())
print(number.get_digits())
print(number.get_max())
print(number.get_min())
print(number.get_average())
print(number.get_median())
print(number.get_frequency())