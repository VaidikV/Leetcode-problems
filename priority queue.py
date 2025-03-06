class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def __get_index_of_high_priority_item(self):
        highest_priority_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][1] > self.queue[highest_priority_index][1]:
                highest_priority_index = i
        return highest_priority_index

    def remove(self):
        if not self.queue:
            return
        else:
            highest_priority_index = self.__get_index_of_high_priority_item()
            return self.queue.pop(highest_priority_index)

    def peek(self):
        if not self.queue:
            return
        else:
            highest_priority_index = self.__get_index_of_high_priority_item()
            return self.queue[highest_priority_index][0]

    def update_priority(self, target_value, new_priority):
        if not self.queue:
            return
        for i in self.queue:
            if i[0] == target_value:
                i[1] = new_priority
                return
        return print("item not found")


pq = PriorityQueue()
pq.insert(["t1", 10])
pq.insert(["t2", 5])
pq.insert(["t3", 20])

pq.update_priority("t3", 30)
print(pq.queue)