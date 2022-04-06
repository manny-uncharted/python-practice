## Arrays
An array is a collection of items stored at contiguous memory locations. The idea behind arrays is to store many items of the same type together thereby making it easier to calculate the position of each element by simply adding an offset to a base value, i.e the memory loaction of the first element of the array.

### Array's size 
Basically in the array has a fixed size meaning once the size is given to it, it cannot be changed, therefore you can't shrink or expand it.

The reason was that for expanding, if we change the size we can’t be sure ( it’s not possible every time) that we get the next memory location to us as free. The shrinking will not work because the array, when declared, gets memory statically allocated, and thus compiler is the only one can destroy it.

### Advantages of using arrays:
- Arrays allow random access to elements which makes accessing elements by position faster

- Arrays have better cache locality that makes a pretty big difference in performance.

- Arrays represent multiple data items of the same type using a single name

### Disadvantages of using arrays:
- Arrays are not dynamic, meaning they are not resizable.

- Arrays are not thread-safe.

### Applications of Array
- When you need to store a large number of similar items of the same data type

- Used to implement other data structures like stacks, queues,heaps, hash tables, linked lists, trees, graphs, etc.