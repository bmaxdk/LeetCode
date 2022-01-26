# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/
# class MyHashSet:

#     def __init__(self):
#         self.arr[1000]

#     def add(self, key: int) -> None:
        

#     def remove(self, key: int) -> None:
        

#     def contains(self, key: int) -> bool:
        


# # Your MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)

print([0 for _ in range(4)])
a = [i for i in range(4)]
print(a)
di = 3
a = a[0:di]+a[di+1::]
print(a)

a = {}
a[1] = 2
a[2] =4
print(a)
print(a[2])
print([[] for _ in range(1<<3)])
print(1<<3)
print(6>>2)