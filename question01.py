# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring
# of s. For example: if s = "udacity" and t = "ad", then the function returns
# True. Your function definition should look like: question1(s, t) and return a
# boolean True or False.


def question1(s, t):
    # Get the lengths of strings s and t
    lenT = len(t)
    lenS = len(s)
    # Store values of t inside of a list
    sortT = list(t)
    # Sort list alphabetically
    sortT.sort()

    for i in range(lenS - lenT + 1):
        # Store values of s1 inside of a list
        s1 = list(s[i: i+lenT])
        # Sort list alphabetically
        s1.sort()
        # Compares s1 to s2 and returns the result
        if s1 == sortT:
            return True
    return False


def main():
    print question1("udacity", "ad")
    print question1("udacity", " ")
    print question1("udacity", "so")


if __name__ == '__main__':
    main()
