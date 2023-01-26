#Fenwick tree 
#Binary indexed tree

class FenwickTree:

	def __init__(self,nums):
		#original array of numbers (integers)
		self.nums = nums
		#the constructed Fenwick tree (first item is 0 always so the size is greater)
		#initialize the values to be 0s
		self.fenwick_tree = [0 for _ in range(len(nums)+1)]
		
	#the sum of numbers in the interval [start:end]
	#O(logN) running time complexity
	def range_sum(self,start,end):
		return self.sum(end)-self.sum(start-1)
		
	#sum of the integers in the range [0:index]
	#O(logN) running time complexity
	def sum(self,index):
	
		#indexes start with 0 but in the theory/implementation we start with 1
		index = index + 1
		#the final result (so the sum of the integers)
		sum = 0
		
		#we may consider the sum of multiple ranges so we have to iterate until index>0
		while index>0:
			#binary index tree contains the sums of given ranges
			sum = sum + self.fenwick_tree[index]
			#go to the parent and keep going (basically the items on the left)
			index = self.parent(index)
			
		return sum

	#constructing the Fenwick tree from the original array of integers
	#O(NlogN) running time complexity
	def construct(self):

		#consider all the items in the original array
		for index in range(1,len(self.nums)+1):
			self.update(index,self.nums[index-1])

	#update an existing item in the tree with index and value accordingly
	#O(logN) running time complexity
	def update(self,index,num):
		
		#have to check all the ranges that include the index
		while index<len(nums)+1:
			self.fenwick_tree[index] += num
			#index of the items on the right
			index = self.next(index)
	
	#index of the item on the left
	#O(1) running time complexity
	def next(self,index):
		return index + (index&-index)

	#index of the item on the right (so the parent)
	#O(1) running time complexity
	def parent(self,index):
		return index - (index&-index)
		
if __name__ == "__main__":
	
	nums = [3,2,-1,6,5,4,-3,3,7,2,3]
	
	fenwick_tree = FenwickTree(nums)
	fenwick_tree.construct()
	
	print(fenwick_tree.range_sum(2,5))
	