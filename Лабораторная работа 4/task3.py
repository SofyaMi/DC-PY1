def delete(list_, index=None):
    if index is not None:
        one = list_[:index]
        two = list_[index+1:]
        result_ = one + two
        return result_
    else:
        return list_[:-1]

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
