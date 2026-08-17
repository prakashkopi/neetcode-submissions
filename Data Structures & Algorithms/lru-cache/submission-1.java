class LRUCache {

    private int capacity; 
    private Map<Integer, LinkedListNode> cache;
    private LinkedList<LinkedListNode> lruList;

    private class LinkedListNode {
        int key;
        int value;
        LinkedListNode(int key, int value) {
            this.key= key;
            this.value= value;
        }
    }

    public LRUCache(int capacity) {
        this.capacity= capacity; 
        cache= new HashMap<>();
        lruList= new LinkedList<>();
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            LinkedListNode node= cache.get(key);
            // remove and add to front (most recently used)
            lruList.remove(node);
            lruList.addFirst(node);
            return node.value;
        }
        return -1; // doesnt exist        
    }
    
    public void put(int key, int value) {
        // if key already exists
        if (cache.containsKey(key)) {
            LinkedListNode node= cache.get(key);
            lruList.remove(node);
            node.value= value;
            lruList.addFirst(node);
        }
        else {
            // if capacity has already been reached
            if (cache.size() >= capacity) {
                LinkedListNode node= lruList.removeLast();
                cache.remove(node.key);
            }
            LinkedListNode node= new LinkedListNode(key, value);
            lruList.addFirst(node);
            cache.put(key, node);
        }

        
    }
}
