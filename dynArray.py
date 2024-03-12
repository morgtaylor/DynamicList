import csv
import ctypes

class DynArray(object):
    def __init__(self): #intialize array w/ default vals
        self.numEle = 0 #number of elements in array
        self.capacity = 10 #capacity of array at initialization
        self.array = self.make_array(self.capacity) #creation of the array
        
    def __getitem__(self, index): #gets elements of specific index by using []
        if not 0 <= index < self.numEle: #checks if index is with in array bounds
            raise IndexError("Index out of bounds")
        return self.array[index]
       
    def append(self, ele): #adds an element to array
        if self.numEle == self.capacity: #check if at capacity
            self._resize(2 * self.capacity) #doubles capacity if needed by calling resize method
        self.array[self.numEle] = ele
        self.numEle += 1

    def _resize(self, new_cap):
        arrayTwo = self.make_array(new_cap)  # creates new bigger array
 
        for k in range(self.numEle):  # copies existing values into bigger array
            arrayTwo[k] = self.array[k]
 
        self.array = arrayTwo  # updates array attribute for bigger array
        self.capacity = new_cap  # reset the capacity

    def make_array(self, new_cap): #creates new array with give capacity, used by resize
        return (new_cap * ctypes.py_object)()

class Iter: #creates a class called fiftyIter
    def __init__(self, data, start_index=49): #initializes iteration data
        self.data = data
        self.index = start_index
    def __iter__(self): #returns iteraiton object
        return self
    def __next__(self): #gets next iteration element
        if self.index < len(self.data): #checks if the current iteration is within the bounds of the list
            result = self.data[self.index] #gets data at current index
            #print(self.index) #index testing to ensure starting at index 49 and increase by 50
            self.index += 50 #iterates through the list by 50
            
            return result #returns the contacts row for the current iteration
        else:
            raise StopIteration #if the iteration is out of bounds of the list (no more entries in the list) it calls the StopIteration and exits the iteration
            
csvFile = open('us-contacts.csv', 'r') #opens the file to read
read = csv.reader(csvFile, delimiter=',') #creates a reader object

contacts = DynArray()  # creates an instance of DynArray

for row in read:
    contacts.append(tuple(row)) #reads each row from the list and appends to contact list
 
sortedContacts = sorted(contacts, key=lambda x: x[1]) #sorts the contact list by col 1 (last name) stores in sortedContacts list
''' #test print
for i in range(0, 50, 2):
    print(contacts[i])
'''


print("First Name,  Last Name,     Street,        City,   State,   Zip,       Phone,         Email")

for element in Iter(sortedContacts): #uses the fiftyIter class to iterate through the sortedContacts list and then prints the current row.
    print(element)

