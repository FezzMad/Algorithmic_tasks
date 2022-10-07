def hasTwoNearZero(seq):
    for i in range(0, len(seq)):
        if seq[i] == 0:
            if i + 1 < len(seq):
                if seq[i + 1] == 0:
                    return True
    return False


def num_to_letter(num):
    if num == 10:
        return 'A'
    if num == 11:
        return 'B'
    if num == 12:
        return 'C'
    if num == 13:
        return 'D'
    if num == 14:
        return 'E'
    if num == 15:
        return 'F'


def dec_to_another(num, k):
    ans = []
    while num // k > 0:
        num_tmp = num
        num = num // k
        ost = num_tmp - num * k
        if ost in range(10, 16):
            ost = num_to_letter(ost)
        ans.append(ost)
    else:
        if num in range(10, 16):
            num = num_to_letter(num)
        ans.append(num)
    return ans


def another_to_dec(num, k):
    ans = 0
    pow = 0
    while num > 0:
        ost = num % 10
        ans += ost * k ** pow
        pow +=1
        num = num // 10
    return ans


def end(N, K):
    ans = K - 1
    for i in range(0, N - 1):
        ans = ans * 10 + (K - 1)
    return ans


def No_2Zero(N, K):
    start_num = another_to_dec(10 ** (N) // 10, K)
    end_num = another_to_dec(end(N, K), K)
    sum = 0
    for num in range(start_num, end_num + 1):
        cur_num = dec_to_another(num, K)
        if not hasTwoNearZero(cur_num):
            sum += 1
    return sum