class Queue():

	def __init__(self, limit = 10):
		self.queue = []
		self.front = None
		self.rear = None
		self.limit = limit

	def is_empty(self):
		return len(self.queue)<=0

	def enqueue(self, data):
		if len(self.queue) >= self.limit:
			return print("queue is at limit")
		else:
			self.queue.append(data)

		# assign the rear as size of the queue and front as 0
		if self.front is None:
			self.front = self.rear = 0
		else:
			self.rear = len(self.queue)-1


	# to pop an element from the front end of the queue
	def dequeue(self):
		if self.is_empty():
			return print("queue is empty")	# queue underflow
		else:
			self.queue.pop(0)
			if len(self.queue) == 0:
				self.front = self.rear = None
			else:
				self.rear = len(self.queue)-1

	def peek(self):
		return self.front


class DoubleEndedQueue(Queue):

	def __init__(self, limit=10):
		super().__init__(limit)

	def enqueue_front(self, data):
		if len(self.queue) >= self.limit:
			return print("Queue is at limit")
		else:
			if self.is_empty():
				self.front = self.rear = 0
				self.queue.append(data)

			else:
				self.queue.insert(0, data)
				self.rear += 1


	def dequeue_rear(self):
		if self.is_empty():
			return print("Queue is empty")
		else:
			self.queue.pop()
			if self.is_empty():
				self.front = self.rear = None
			else:
				self.rear -= 1



	def find_index(self, value):
		if self.is_empty():
			return

		for i in range(len(self.queue)):
			if self.queue[i]== value:
				return i

		return print("Not in queue")

# Example Usage:
deque = DoubleEndedQueue()
deque.enqueue(10)
deque.enqueue(20)
deque.enqueue(30)
deque.enqueue(40)

print(deque.find_index(40))
# deque.enqueue_front(5)
# deque.enqueue_front(1)
# deque.dequeue_rear()

print(deque.queue)
