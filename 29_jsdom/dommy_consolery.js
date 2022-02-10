// Team ____ :: Ivan Mijacika, Qina Liu
// SoftDev pd2
// k29 -- DOMfoolery++
// 2022-02-08
// --------------------------------------------------



//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

///////

var gcd = function(a, b){
  if (a == 0) return b;
  if (b == 0) return a;
  if (a >= b) {
    return gcd(a - b, b);
  }
  return gcd(b - a, a);
}

var fib = function(n){
    if (n==0 || n==1) return n
    else return (fib(n-2) + fib(n-1))
}

var fact = function(n){
    if (n == 0) return 1
    else return (n * fact(n-1))
}

let b1 = document.getElementById("b1");
let b2 = doucment.getElementById("b2");
let b3 = document.getElementById("b3");


let p3 = function(){
        addItem("fib" + fib(2));
}

let p2 = function(){
	addItem("gcd" + gcd(2, 4));
}

let p1 = function(){
	addItem("fact" + fact(2));
}

b.addEventListener('click', p1);
b.addEventListener('click', p2);
b.addEventListener('click', p3);

