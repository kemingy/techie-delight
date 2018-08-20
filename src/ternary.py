# In this post, we will see how to implement ternary-like operator without using
# conditional expression like ternary operator, if-else expression or 
# switch-case statements.

def ternary(condition, option_x, option_y):
    # return option_x if condition is True
    ans = [option_y, option_x]
    return ans[condition]
