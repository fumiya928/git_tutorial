f=open('kadai3.txt')
line = f.readlines()
f.close()
size = len(line)
num_list = []
for i in range(size):
        num_list.append(int(line[i]))
def heap(num_list, n, i):

 root = i
 left = 2*i +1
 right = 2*i +2

 if left < n and num_list[i] < num_list[left]:
    root = left
 if right < n and num_list[root] < num_list[right]:
    root = right
 if root != i:
    num_list[i], num_list[root] = num_list[root], num_list[i]
    heap(num_list, n, root)

def heap_sort(num_list):
  n = len(num_list)
  for i in range(n//2, -1, -1):
        heap(num_list, n, i)

  for i in range(n-1, 0, -1):
     num_list[i], num_list[0] = num_list[0], num_list[i]
     heap(num_list, i, 0)

if __name__ =='__main__':
    print('入力', num_list)
    heap_sort(num_list)
    print('結果', num_list)

    print('Hello world')
