def strings_to_list(string, substring):
    string_list = [x for x in string.split(", ")]
    substring_list = [x for x in substring.split(", ")]
    result = []

    def iterate_over_lists(indx):
        while indx < len(string_list):
            iterate_over_sublists(indx, 0)
            indx += 1
            iterate_over_lists(indx)

    def iterate_over_sublists(indx, secindx):
        while secindx < len(substring_list):
            if string_list[indx] in result:
                return
            if string_list[indx] in substring_list[secindx]:
                result.append(string_list[indx])
            secindx += 1
            iterate_over_sublists(indx, secindx)
            return

    iterate_over_lists(0)
    return result


inp1 = input()
inp2 = input()


res = strings_to_list(inp1, inp2)
print(res)
