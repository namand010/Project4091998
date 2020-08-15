def all_even():
    n = 0
    while True:
        yield n
        n += 2

all_gen = all_even()

print(next(all_gen))
# Generate the first 5 even numbers.
for i in range(5):
    print(next(all_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
for i in range(5):
    print(next(all_gen))


def prod(a,b):
#     # TODO change output to the product of a and b
        output = a * b
        return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        n = output
        i += 1
#         # TODO: update i and n
#         # Hint: i is a successive integer and n is the previous product


# # Test block
my_gen = fact_gen()
num = 5
for i in range(num):
     print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
a = [[0,1,2],[0,1,2],[0,1,2]]

print([a[x][x] for x in range(len(a))])