// Momentous M's :: Ivan Mijacika, Justin Morrill
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-03
// --------------------------------------------------


var fib = function(n){
    if (n==0 || n==1) return n
    else return (fib(n-2) + fib(n-1))
}



var fact = function(n){
    if (n == 0) return 1
    else return (n * fact(n-1))
}
