class SLLNode { // Singly-linked list node class
    constructor(val) {
        this.value = val; // Holds value for this node
        this.next = null; // Pointer to next node
    }
}
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;              
    }
}

class SLL { // The singly-linked list class itself
    constructor() { // Will start with no nodes
        this.head = null; // Head points to first node
    }
    length(){
        //We first have to tell our train attendant that we want them to start at the front of the train
        let runner=this.head;
        let count=0
        //Since a Linked List does not know how many nodes is within it, we will not be able to use a for loop to             iterate, instead we'll use a while
        //Also we need to tell them when to stop otherwise they will just run off the end of the train
        while(runner !== null){
            count++
            runner=runner.next
            }
        return count
    }
}

