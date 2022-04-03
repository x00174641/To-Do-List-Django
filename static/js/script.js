let getExpiryTime = document.getElementById('nextexpiryDate').innerHTML
let countDownDate = new Date(getExpiryTime).getTime();

let timeout = setInterval(function() {
let today = new Date().getTime();
let ms = countDownDate - today;
  
let days = Math.floor(ms/ (1000 * 60 * 60 * 24));
let hours = Math.floor((ms % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
let minutes = Math.floor((ms % (1000 * 60 * 60)) / (1000 * 60));
let seconds = Math.floor((ms % (1000 * 60)) / 1000);
  
document.getElementById("nextdueTime").innerHTML =  "(" + days + "D " + hours + "H "+ minutes + "M " + seconds + "S " + "Remaining)";
  
if (ms < 0) {
    clearInterval(timeout);
    document.getElementById("nextdueTime").innerHTML = "Time is up!";
    window.location.reload();
  }
}, 1000);