

def count_five_more(number):
    result = []
    for i in range(number, number + 5):
        result.append(i)
    return result


def print_one_to_twenty():
    count_five_more(1)
    count_five_more(6)
    count_five_more(11)
    count_five_more(16)



if count_five_more(1) == [1,2,3,4,5]:
    print "PASSED TEST 1!!"
else:
    print "BOOOO"



print 3

if count_five_more(-5) == [-5,-4,-3,-2,-1]:
    print "test case 2 passed"
else:
    print "BOOOO"

print 5