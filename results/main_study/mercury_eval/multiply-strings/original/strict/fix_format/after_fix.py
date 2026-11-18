class Solution:

    def take_out_zeros(self, num):
        # if not int(num[len(num)-1]):
        #     return "0"

        i = 0

        while i < len(num) and num[i] == "0" :
            i += 1

        return num[i:] if i != len(num) else "0"


    def multiply(self, num1: str, num2: str) -> str:

        res = "0"
        min_num = num1 if len(num1) <= len(num2) else num2
        max_num = num1 if len(num1) >= len(num2) and num1 != min_num else num2

        def sum_digits(x, y):

            res = ""
            carr = 0
            max_len = max(len(x), len(y))
            x, y = "0" * (max_len - len(x)) + x, "0" * (max_len - len(y)) + y

            min_len = min(len(x), len(y))
            for i in range(min_len - 1, -1, -1):
                first_digit = int(x[i])
                second_digit = int(y[i])
                sum_res = first_digit + second_digit + carr
                if sum_res >= 10:
                    carr = 1
                else:
                    carr = 0
                res = str(sum_res % 10) + res

            if len(x) > min_len:
                res = res + sum_digits(x[min_len:], str(carr))
            elif len(y) > min_len:
                res = res + sum_digits(y[min_len:], str(carr))
            elif carr:
                res  = str(carr) + res
            return res

        def multiply_digits(min_num, max_num, z):
            res = ""
            # print("min_num: " + min_num)
            # print("max_num: " + max_num)
            # print("z: " + str(z))

            carr = 0
            num = int(min_num)
            for i in range(len(max_num) - 1, -1, -1):
                digit = int(max_num[i])
                # print("digit: " + str(digit))
                mult = (digit * num) + carr
                # print("mult: " + str(mult))
                res = str(mult % 10) + res
                carr = (mult // 10) % 10

            if carr:
                res = str(carr) + res

            return res + "0" * z



        for i in range(len(min_num)):
            mult_res = multiply_digits(min_num[i], max_num, len(min_num) - i - 1)
            # print("mult_res: " + mult_res)
            # print("prev_res: " + res)

            sum_res = sum_digits(mult_res, res)

            # print("sum_res: " + sum_res)
            res = sum_res

            # self.take_out_zeros(res)


        return self.take_out_zeros(res)

