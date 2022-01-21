//Reverse
var arr = [8,7,6,5,4,3,2,1]

function reverse(arr){
    for(var i = 0; i < arr.length / 2 ; i++){
        temp1 = arr[i];
        arr[i] = arr[arr.length-i-1];
        arr[arr.length-i-1] = temp1;
    }
}

// reverse(arr);
// console.log(arr);

function rotate(arr,move){
    for (var i = 0; i < move; i ++){
        var temp = arr[arr.length-1];
        for (var k = arr.length -2; k >= 0; k--){
            arr[k+1]= arr[k];
        }
        arr[0] = temp;
    }
}
// rotate(arr,2);
// console.log(arr);

function filterRange(arr, minVal, maxVal){
    for (var i = 0; i < arr.length; i++){
        if(arr[i] < minVal || arr[i] > maxVal){
            for(k = i+1; k < arr.length; k++){
                arr[k-1]=arr[k]
            }
            arr.length--; //Decrease the length of the array by one
            i--;
        }
    }
}

var arr1 = [5,7,2,4], arr2 = ['b','n'];

function concatArr(arr1,arr2){
    var newArr = [];
    for (var i = 0; i < arr1.length; i++){
        newArr[i] = arr1[i]
    }
    for (var j = 0; j < arr2.length; j++){
        newArr[i+j] = arr2[j]
    }
    return newArr;
}

console.log(concatArr(arr1,arr2));
