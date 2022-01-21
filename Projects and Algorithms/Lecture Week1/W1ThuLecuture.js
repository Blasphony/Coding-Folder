class SLLNode {
    constructor(value){
        this.data = value;
        this.next = null;
        // Attributes for a SLL Node
        // 1 Data
        // 2 references to next node
    }
}

//myNode = new SLLNode(5);

class SLL {
    constructor(value) {
        this.head = null; //when first created, SLL is blank
    }

    addToFront(value){
        // emply list or list with values
        if(this.head === null) {
            this.head = new SLLNode(value);
            console.log("Added node to an empty SLL")
        } else{//values exist in the list
            let oldHead = this.head;
            this.head = new SLLNode(value);
            this.head.next = oldHead;
            console.log('added node to non empty SLL')
        }
    }
    printValues(){
        var currNode = this.head;
        while(currNode !== null) {
            console.log(currNode.data);
            currNode=currNode.next;
        }
    }
}

var mySLL = new SLL();
console.log(mySLL);

mySLL.addToFront(3);
console.log(mySLL);
mySLL.addToFront(2);
console.log(mySLL);
mySLL.addToFront(1);
console.log(mySLL);
mySLL.printValues();