arr=[4,2,1,3,5]

function minToFront(arr){
    var temp4 = arr[0]
    for(i = 1; i < arr.length; i++){
        if (temp1 > arr[i+1]){
            temp1 = arr[i+1];
        }
    }
    var temp1 = arr[1], temp2 =arr[2], temp3=arr[0];
    for(var i = 0; i < arr.length && temp1 !=undefined; i++){
        arr[i]=temp1;
        temp1 = temp2;
        temp2 = arr[i+3];
    }
    arr[0]=temp4;

}

minToFront(arr);
console.log(arr);