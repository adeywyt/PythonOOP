class ZH_INT:
    def __init__(self, num):
        self.num = num

    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            zh = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
                  "壹": 1, "贰": 2, "参": 3, "肆": 4, "伍": 5, "陆": 6, "柒": 7, "捌": 8, "玖": 9}
            result = 0
            for each in self.num:
                if each in zh:
                    result += zh[each] # result  = result +zh[each]
                else:
                    result += int(each) # 0 = 0+ 1
                result *= 10 # result = result * 10
            return result // 10   # result // 10

n = ZH_INT("五二零1314")
a = int(n)
print(a)
