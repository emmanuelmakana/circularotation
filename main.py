# Function to find the number of times the list is rotated
def findRotationCount(A):

	# search space is A[left..right]
	(left, right) = (0, len(A) - 1)

	# iterate till search space contains at-least one element
	while left <= right:

		# if the search space is already sorted, we have
		# found the minimum element (at index left)
		if A[left] <= A[right]:
			return left

		mid = (left + right) // 2

		# find next and previous element of the mid element
		# (in circular manner)
		next = (mid + 1) % len(A)
		prev = (mid - 1 + len(A)) % len(A)

		# if mid element is less than both its next and previous
		# neighbor, then it is the minimum element of the list
		if A[mid] <= A[next] and A[mid] <= A[prev]:
			return mid

		# if A[mid..right] is sorted and mid is not the minimum element,
		# then pivot element canbe present not in A[mid..right] and
		# we can discard A[mid..right] and search in the left half
		elif A[mid] <= A[right]:
			right = mid - 1

		# if A[left..mid] is sorted then pivot element canbe present not in
		# it and we can discard A[left..mid] and search in the right half
		elif A[mid] >= A[left]:
			left = mid + 1

	# invalid input
	return -1


if __name__ == '__main__':

	A = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
	print("The list is rotated", findRotationCount(A), "times")
