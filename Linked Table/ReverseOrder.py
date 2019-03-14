# 如何实现链表的逆序

# 方法一：就地排序
class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

# 方法功能：对单链表进行逆序 输入参数：head：链表头结点

def Reverse(head):
    # 判断链表是否为空
    if head == None or head.next == None:
        return
    pre = None  #前驱结点
    cur = None  #当前结点
    next = None  #后继结点
    # 把链表首结点变为尾结点
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next
    # 使当前遍历道的结点cur指向其前驱结点
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next
    # 链表最后一个结点指向倒数第二个结点
    cur.next = pre
    # 链表的头结点指向原来链表的尾结点
    head.next = cur


# 方法二：递归法
def RecursiveReverse(head):

    if head is None or head.next is None:
        return head
    else:
        newhead = RecursiveReverse(head.next)

        head.next.next=head
        head.next=None
    return newhead

if __name__=="__main__":
    i = 1
    #链表头结点
    head = LNode(i)
    head.next = None
    tmp = None
    cur = head
    #构造单链表
    while i<8:
        tmp = LNode(i)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("逆序前:",)
    cur = head.next
    while cur!=None:
        print(cur.data)
        cur = cur.next
    print("\n逆序后:",)
    Reverse(head)
    cur = head.next
    while cur!=None:
        print(cur.data)
        cur = cur.next
# 时间复杂度为O(N)，其中，N为链表长度，但是需要常数个额外的变量来保存当前结点的前驱结点与后继结点，因此空间复杂度为O(1)

