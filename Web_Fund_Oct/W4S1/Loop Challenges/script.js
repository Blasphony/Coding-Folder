for (let index = 1; index <= 20; index++) {
    if (index % 2 !==0) {
        console.log(index)
    }
}

for (let index = 100; index > 0; index--) {
    if (index % 3 === 0) {
        console.log(index)
    }
}

for (let index = 4; index >= -3.5; index-=1.5) {
    console.log(index)
}

var sum = 0;
for ( let index = 1; index <= 100; index++) {
    sum+=index
}
console.log(sum)

var product = 1;
for (let index = 1; index <= 12; index++) {
    product*=index
}
console.log(product)