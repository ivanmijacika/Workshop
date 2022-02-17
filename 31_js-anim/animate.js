// Team Momentous M's:: Ivan Mijacika, Justin Morrill
// SoftDev pd2
// K31 -- canvas based JS animation
// 2022-02-16

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "#FF00FF"; //magenta

var requestID = null;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.width, c.height);
};


var radius = 0;
var growing = true;

var ifRunning = () => {
  console.log("ifRunning invoked...");
  if (!requestID){
   requestID = requestAnimationFrame(drawDot);
  }
};

//var drawDot = function() {
var drawDot = () => {
  clear();
  console.log("drawDot invoked...");
  ctx.beginPath();
  ctx.arc(c.clientWidth/2, c.clientHeight/2, radius, 0, 2*Math.PI);
  ctx.fill();
  ctx.stroke();
  if (growing) {
    radius ++;
    if (radius === c.clientWidth/2) growing = false;
  }else{
    radius --;
    if (radius === 0) growing = true;
  }
  requestID = requestAnimationFrame(drawDot);
};


//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );

  window.cancelAnimationFrame(requestID);
  requestID = null;
};


dotButton.addEventListener( "click", ifRunning );
stopButton.addEventListener( "click",  stopIt );
