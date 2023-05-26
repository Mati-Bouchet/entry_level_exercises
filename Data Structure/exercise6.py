from collections import deque
# Write a Python program that uses a queue to simulate a line at a store. 
# The program should allow users to add customers to the line, remove customers from the line, and display the current state of the line.

class Queue:
    def __init__(self):
        self.my_queue = deque()
        
    def is_empty(self):
        return len(self.my_queue) == 0
        
    def add_to_queue(self, person):
        return self.my_queue.append(person)
        
    def remove_from_queue(self):
        if not self.is_empty():
            return self.my_queue.popleft()
        
    def display_qty(self):
        return len(self.my_queue)
        
def create_queue():
    store_queue = Queue()
    
    while True:
        print("Press 1 or 'add' to add customers to the queue")
        print("Press 2 or 'remove' to remove customes from the queue")
        print("Press 3 or 'display' to show the current state of the queue")
        print("Press 4 or 'exit' to quit")
        
        choice = int(input("Select one of the options above: "))
        
        if choice == 1:
            client_name = input("Please enter your name and then press enter: ")
            store_queue.add_to_queue(client_name)
            print(f"{client_name} has been added to the queue")
            print("*****************************")
            
        elif choice == 2:
            if store_queue.is_empty():
                print("You can't remove anybody from the list as it is empty")
            else:  
                removed_client = store_queue.remove_from_queue()
                print(f"Client {removed_client} has been removed from the queue")
                print("*****************************")
            
        elif choice == 3:
            if store_queue.is_empty():
                print("There are no people in this queue")
                print("*****************************")
            else:
                print(f"Here's the current state of the queue: ")
                for client in store_queue.my_queue:
                    print(client)
                print("*****************************")
                    
        elif choice == 4:
            break
        
        else:
            print("Invalid choice")
            
create_queue()
                