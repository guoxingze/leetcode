# Given a linked list, determine if it has a cycle in it.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param head, a ListNode
	# @return a boolean
	def hasCycle(self, head):
		if head != None:
			first = head
			second = head.next
			while second!=None:
				if first == second:
					return True
				first = first.next
				if second.next ==None:
					return False
				else:
					second = second.next.next
			return False
		else:
			return False
node0 =  None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node2
node4.next = node5
node5.next = node1

test = Solution()
print test.hasCycle(node1)