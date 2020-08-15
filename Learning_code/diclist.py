in_list = {'a':[0,1,2,3], 'b':[0,1,2,3], 'c':[0,1,2,3], 'd':[0,1,2,3]}

#print the first element of each key list in a list------
lis_a = []
i = 0
for key in in_list:
        lis_a.append(in_list[key][i])
        i += 1

print(lis_a)

#smallest number from the list;

in_list1 = [2, -1, -4, 8, 6]
small = None
lis_b = []
for num in in_list1:
    if small == None or num < small:
        small = num
print(small)

# This exercise uses a data structure that stores course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


courses = {
    'spring2020': {'cs101': {'name': 'Building a Search Engine',
                             'teacher': 'Dave',
                             'assistant': 'Peter C.'},
                   'cs373': {'name': 'Programming a Robotic Car',
                             'teacher': 'Sebastian',
                             'assistant': 'Andy'}},
    'fall2020': {'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {
                     'name': 'Web Application Engineering - Building a Blog',
                     'teacher': 'Steve',
                     'prereq': 'cs101'},
                 'cs262': {
                     'name': 'Programming Languages - Building a Web Browser',
                     'teacher': 'Wes',
                     'assistant': 'Peter C.',
                     'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                             'teacher': 'Dorina'},
                   'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                             'teacher': 'Jasper'},
                   }
}


def when_offered(courses, course):
    ad = []
    for a in courses:
        if course in courses[a]:
            ad.append(a)
    return ad


print(when_offered(courses, 'cs101'))
# Correct result:
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result:
# []
