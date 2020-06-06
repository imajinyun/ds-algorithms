def decimal_to_any(num, base) -> str:
    """
    将整数转换成以 2～16 为进制基数的字符串

    思路：
    str(769//10) 的商将做为下一步的 f(x)，并在每一步中将余数拼接起来。

    f(769) -> str(769//10) + '9'
    f(76)  -> str(769//10) + '6'
    f(7)   -> str(769//10) + '7'
    """
    s = '0123456789ABCDEF'
    if num < base:
        return s[num]
    else:
        return decimal_to_any(num // base, base) + s[num % base]
