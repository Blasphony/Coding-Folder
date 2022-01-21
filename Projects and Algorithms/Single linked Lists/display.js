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
    addFront(value) {
        var newNode = new SLLNode(value); // Create a new node containing the value passed into the method
        newNode.next = this.head; // Connect the new node to the list
        this.head = newNode; // Move the head of the list to this new node
        return this.head; // OR you can say "return this"
    }

    // Remove a node from the front of the list
    removeFront() {
        if (this.head == null) { // Edge case: If the list is empty, nothing to remove
            return this.head;
        }
        var removedNode = this.head; // Have a variable hold the node we'll remove
        this.head = removedNode.next; // Moves the head of the list to the 2nd node, which will become the new head when we're done
        removedNode.next = null;
        return this.head;
    }

    // Return the value at the front (head) of the list
    front() {
        // Edge case: list is empty
        if (this.head == null) {
            return null;
        } else { // List is not empty
            return this.head.value;
        }
        // // Ternary operator: condition ? value_if_true : value_if_false
        // return this.head ? this.head.value : null;
        // // return this.head == null ? null : this.head.value;
    }
    display(){
        //We first have to tell our train attendant that we want them to start at the front of the train
        let runner=this.head;
        let list = [];
        let counter = 0;
        //Since a Linked List does not know how many nodes is within it, we will not be able to use a for loop to             iterate, instead we'll use a while
        //Also we need to tell them when to stop otherwise they will just run off the end of the train
        while(runner !== null){
            list[counter]=runner.value
            counter++
            runner=runner.next
        }
        return list
    }
}
var mySLL = new SLL();
mySLL.addFront(5);
mySLL.addFront(4);
mySLL.addFront(10);
console.log(mySLL.display());

