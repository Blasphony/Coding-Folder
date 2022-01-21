function pushToFront(arr,val){
    var temp1 = arr[0], temp2 =arr[1];
    for(var i = 0; i < arr.length && temp1 !=undefined; i++){
        arr[i+1]=temp1;
        temp1 = temp2;
        temp2 = arr[i+2];
    }
    arr[0]=val;
}


function push(arr, val){
    // arr temporrary points to 135
    // arr2 brand new array at address 147
    var arr2= [0,0,0];
    for(var i = 0; i < arr.length; i++){
        arr2[i+1]=arr[i];
        console.log(arr2)
    }
    arr2[0]=val;
    return arr2;
}

// address 135
// var myArr = [3,8,3,7,5];
// secondArr =push(myArr,2);
// // address 147
// console.log(secondArr);

var myArr = [4,8,3,7,5,9];
// pushToFront(myArr,2);
// // address 147
// console.log(myArr);

function popFront(arr){
    var temp1 = arr[1], temp2 =arr[2], temp3=arr[0];
    for(var i = 0; i < arr.length && temp1 !=undefined; i++){
        arr[i]=temp1;
        temp1 = temp2;
        temp2 = arr[i+3];
    }
    arr[arr.length-1]=temp3;
    arr.pop()

}
popFront(myArr);
console.log(myArr);

function poptest(arr){
    var temp1 = arr[0]
    
}