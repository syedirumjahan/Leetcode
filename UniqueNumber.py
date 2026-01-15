class Solution(object):
    def uniqueOccurrences(self, arr):

        my_dict = dict()
        count = []

        for i in arr:
            if i in my_dict:
                my_dict[i] =my_dict[i]+1
            else:
                my_dict[i] = 1

        for i in my_dict:
            count.append(my_dict[i])

        if len(count) == len(set(count)):
            return True

        return False
