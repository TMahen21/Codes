# Python Coding Challenge 1 Control Flow
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


large_power(5, 10)

# Python Coding Challenge 2 Control Flow
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < electricity_bill + internet_bill + rent + food_bill):
        return "True"
    else:
        return "False"

print(over_budget(100, 30, 20, 10, 5))

# Python Coding Challenge 3 Control Flow
def twice_as_large(num1, num2):
    if num1 > (2 * num2):
        return True
    else:
        return False

# Python Coding Challenge 4 Control Flow
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


# Python Coding Challenge 5 Control Flow
def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False

# Python Coding Challenge 1 Control Flow Advanced
def in_range(num, lower, upper):
    if lower <= num <= upper:
        return True
    else:
        return False


# Python Coding Challenge 2 Control Flow Advanced
def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


# Python Coding Challenge 3 Control Flow Advanced
def always_false(num):
    if num > 0 > num:
        return True
    else:
        return False


# Python Coding Challenge 4 Control Flow Advanced
def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif 5 < rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"



# Python Coding Challenge 5 Control Flow Advanced
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num2 and num3 > num1:
        return num3
    else:
        return "It's a tie!"

# Python Coding Challenge 1 Lists
def append_size(lst):
    lst.append(len(lst))
    return lst

# Python Coding Challenge 2 Lists
def append_sum(lst):
    for i in range(0, 3):
        lst.append(lst[-1] + lst[-2])
    return lst

# Python Coding Challenge 3 Lists
def larger_list(lst1, lst2):
    if len(lst2) > len(lst1):
        return lst2[-1]
    else:
        return lst1[-1]

# Python Coding Challenge 4 Lists
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False


# Python Coding Challenge 5 Lists
# Method 1
def combine_sort(lst1, lst2):
    lst = lst1 + lst2
    lst.sort()
    return lst

# Method 2
def combine_sort(lst1, lst2):
    unsorted_list = lst1 + lst2
    sorted_list = sorted(unsorted_list)
    return sorted_list


# Python Coding Challenge 1 Lists Advanced
def every_three_nums(start):
  return list(range(start, 101, 3))


# Python Coding Challenge 2 Lists Advanced
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]


# Python Coding Challenge 3 Lists Advanced
# Method 1 (less efficient)
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) > lst.count(item2) or lst.count(item1) == lst.count(item2):
        return item1
    else:
        return item2

# Method 2 (More Efficient)
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

# Python Coding Challenge 4 Lists Advanced

def double_index(lst, index):
# Method 1
    if index > len(lst):
        return lst
    else:
        num = lst[index]*2
        lst.pop(index) and lst.insert(index, num)
        return lst

# Method 2 (Slicing)
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

# Python Coding Challenge 5 Lists Advanced
def middle_element(lst):
    if len(lst) % 2 == 0:
        summa = lst[int(len(lst)/2)] + lst[int(len(lst)/2 - 1)]
        return summa/2
    else:
        return lst[int(len(lst)/2)]


# Python Coding Challenge 1 Loops
def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count += 1
    return count

# Python Coding Challenge 2 Loops
def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append("Hello, " + name)
    return greetings

# Python Coding Challenge 3 Loops
def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst

# Python Coding Challenge 4 Loops
def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst


# Python Coding Challenge 5 Loops
def exponents(bases, powers):
    answers = []
    for base in bases:
        for power in powers:
            answers.append(base ** power)
    return answers

# Python Coding Challenge 1 Loops Advanced
def larger_sum(lst1, lst2):
    sum1 = sum2 = 0
    for num in lst1:
        sum1 += num
    for num in lst2:
        sum2 += num
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

# Python Coding Challenge 2 Loops Advanced
def over_nine_thousand(lst):
  summa = 0
  for number in lst:
    summa += number
    if summa > 9000:
      break
  return summ


# Python Coding Challenge 3 Loops Advanced
def max_num(nums):
    maxi_num = max(nums)
    return maxi_num

# Python Coding Challenge 4 Loops Advanced
def same_values(lst1, lst2):
    lst = []
    for index in range(len(lst1)):
      if lst1[index] == lst2[index]:
        lst.append(index)
    return lst

# Python Coding Challenge 5 Loops Advanced
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(-1 - index)]:
      return False
  return True

# Python Coding Challenge 1 Functions
def tenth_power(num):
    return num ** 10

# Python Coding Challenge 2 Functions
# Method 1
def square_root(num):
    return num ** 0.5

# Method 2
import math
def square_root(num):
    return math.sqrt(num)

# # Python Coding Challenge 3 Functions
# Method 1
def win_percentage(wins, losses):
    total_games = wins + losses
    ratio_wins = wins / total_games
    return  ratio_wins * 100

# Method 2
def win_percentage(wins, losses)
    return (wins/(wins + losses)) * 100


# # Python Coding Challenge 4 Functions
# Method 1
def average(num1, num2):
    total = num1 + num2
    average = total/2
    return average

# Method 2
def average(num1, num2):
    return (num1 + num2)/2

# Python Coding Challenge 5 Functions
# Method 1
def remainder(num1, num2):
    num1 = num1 * 2
    num2 = num2 / 2
    return num1 % num2

# Method 2
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

# Python Coding Challenge 1 Functions Advanced
# Method 1
def first_three_multiples(num):
    for i in range (1, 4):
        print(num * i)
    return num * 3

# Method 2
def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

#  Python Coding Challenge 2 Functions Advanced
def tip(total, percentage):
    tip_amount =  (total * percentage)/100
    return tip_amount


# Python Coding Challenge 3 Functions Advanced
def introduction(first_name, last_name):
    return str(last_name) + ", " + str(first_name) + " " + str(last_name)


# Python Coding Challenge 4 Functions Advanced
# Method 1
def dog_years(name, age):
    age = age * 7
    return str(name) + ", you are " + str(age) + " years in dog years"

# Method 2
def dog_years(name, age):
    return str(name) + ", you are " + str(age * 7) + " years in dog years"

# Python Coding Challenge 5 Functions Advanced
def lots_of_math(a, b, c, d):
    num1 = a + b
    num2 = c - d
    num3 = num2 * num1
    num4 = num3 % a
    print(num1)
    print(num2)
    print(num3)
    return num4


# Introduction to Strings

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)
print(new_account)


first_name = "Reiko"
last_name = "Matsuki"

#
def password_generator(first_name, last_name):
    password = first_name[-3:] + last_name[-3:]
    return password

temp_password = password_generator(first_name, last_name)
print(temp_password)

#
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)

#
def get_length(string):
    return len(string)

#
def letter_check(word, letter):
    for character in word:
        if letter == character:
            return "True"
    return "False"

#
def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

#
def username_generator(first_name, last_name):
    if len(first_name) < 3 or len(last_name) < 4:
        user_name = first_name + last_name
        return user_name
    user_name = first_name[:3] + last_name[:4]
    return user_name

def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

#
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

#































