# 2.1   Should use a linked list because inserts have O(1) time complexity.  Once a month, you'll read every item in the collection.  This means that the linked list read time will be comparable to the array read time, too.
# 2.2   Linked list again.  Lots of insertions and deletions.  Never needs random access reads because it's a FIFO queue.
# 2.3   Use a sorted array.  Arrays have fast reads.
# 2.4   Inserts on traditional arrays have O(n) time complexity because they require contiguous memory allocation, and because inserts into the middle or beginning of the array require reindexing of other elements.  Regarding binary search, when you add new users, their ID numbers have to be inserted in a way that keeps the user list sorted.  Potentially expensive, but if new users always had a higher ID than prior users, then they could always be pushed onto the end of the array.  If instead they are storing only by username and not hidden user IDs, then this would create lots of middle inserts.
# 2.5   Speed depends on the size of the linked lists.  For reads, it will be slower than a single array, but faster than a linked list.  For inserts, it will be neglibly slower than a linked list and significantly faster than an array.