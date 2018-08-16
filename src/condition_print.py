# What should be the if condition in below code snippet, so that output would be
# "Hello World".
#
# if "condition"
#     printf("Hello");
# else
#     printf("World");

import sys

def condition_print(output=sys.stdout):
    if not output.write('Hello '):
        output.write('Hello ')
    else:
        output.write('World')

'''
if print('Hello', end=' '):
    print('Hello', end=' ')
else:
    print('World')
'''
