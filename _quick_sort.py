"""
以[49, 38 , 65, 97, 76, 13, 27, 49]为例：
一般取第一个元素当做基数(49)
第一轮迭代的过程如下：
    [27, 38, 65, 97, 76, 13, 27 49]
    [27, 38, 65, 97, 76, 13, 65, 49]
    [27, 38, 13, 97, 76, 13, 65, 49]
    [27, 38, 13, 97, 76, 97, 65, 49]
    此时发现i > j, 退出循环
    将基数放入数组中：
    [27, 38, 13, 49, 76, 97, 65, 49]
然后分别对基数两边的子数组进行迭代。
"""


def QuickSort(myList, start, end):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = myList[i]

        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):  # 从右向左找
                j = j - 1
            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            # 同样的方式比较前半区
            while (i < j) and (myList[i] <= base):  # 从左向右找
                i = i + 1
            myList[j] = myList[i]

        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        # 递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList

if __name__ == '__main__':
    li = [49, 38 , 65, 97, 76, 13, 27, 49]
    QuickSort(li, 0, len(li)-1)
