# Question 2
# Given a string a, find the longest palindromic subString contained in a.
# Your function definition should look like question2(a), and return a string.


def question2(s):
    # Check for string
    if not s:
        return "No value"
    # get the length of the string
    n = len(s)
    longest = 0
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            subString = s[i:j]
            # Checks if the subString value is the same when reverse and if longest
            if subString == subString[::-1] and len(subString) > longest:
                # Checks the length of the substring to see if its the longest
                longest = len(subString)
                # Store the i, j values to get the subString
                left = i
                right = j
    # Compute the subString using the stored longest left and right values
    LongSubStr = s[left:right]
    # Return the Longest SubString
    return LongSubStr


def main():
    # Test cases
    TC1 = "racecar"
    print "Test case 1: " + '"' + TC1 + '"' + " longest palindromic subString: " + question2(TC1)
    TC2 = ""
    print "Test case 2: " + '"' + TC2 + '"' + " longest palindromic subString: " + question2(TC2)
    TC3 = "udacity"
    print "Test case 3: " + '"' + TC3 + '"' + " longest palindromic subString: " + question2(TC3)


if __name__ == '__main__':
    main()
