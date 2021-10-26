function alwaysHungry(arr) {
    for (let index = 0; index < arr.length; index++) {
        if (arr[index]==="food") {
            console.log("yummy")
        }
    }
    if (!arr.includes('food')) {
        console.log("I'm hungry")
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"]);
// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"
