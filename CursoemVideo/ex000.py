"""def print_aplha(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return

print_aplha(['a', 'b', 'c'], [1, 2, 3])

"""
#Encontrar quantas vezes uma sub string aparece em uma string
def count_substring(string, sub_string):
    cont = 0
    for i in range(len(string)):
        if string[i: (i + len(sub_string))] == sub_string:
            cont += 1
    return cont

my = "abcdcdc"
sub = 'cdc'
con= count_substring(my, sub)
print(con)