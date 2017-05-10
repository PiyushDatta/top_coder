class Substitute:
    def getValue(self, key, code):
        my_dict = {}
        j = 1
        return_array = []
        for i in key:
            my_dict[i] = j
            if j < 9:
                j += 1
            elif j == 9:
                j = 0
        for p in code:
            for keys in my_dict:
                if p == keys:
                    return_array.append(my_dict[keys])

        fin_ans = map(str, return_array)
        fin_ans = ''.join(fin_ans)
        fin_ans = int(fin_ans)
        return fin_ans

if __name__ == '__main__':
    key1 = "TRADINGFEW"
    code1 = "LGXWEV"

    c = Substitute()
    print(c.getValue(key1, code1))
    