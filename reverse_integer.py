class Solution:
    def reverse(self, x: int) -> int:
        sign = ""

        if x < 0:
            x_str = str(x)

            sign = x_str[0:1]

        abs_x = abs(int(x))
        x_rev = str(abs_x)[::-1]

        max_base = 2 ** 31
        max_num = max_base - 1
        min_num = -(max_base)

        x_rev_int = int(x_rev)
        if x_rev_int >= max_num:
            return 0
        elif x_rev_int <= min_num:
            return 0

        with_sign = sign + str(x_rev_int)
        x_rev_int = int(with_sign)

        return x_rev_int
