fetch("menu2.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(text => document.getElementById("portfolio-code2").innerText = text)
  .catch(errror => document.getElementById("portfolio-code2").innerText = "Unable to fetch portfolio, try again later")
fetch("athletics4.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(text => document.getElementById("portfolio-code3").innerText = text)
  .catch(errror => document.getElementById("portfolio-code3").innerText = "Unable to fetch portfolio, try again later")
fetch("calendar2.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(text => document.getElementById("portfolio-code4").innerText = text)
  .catch(errror => document.getElementById("portfolio-code4").innerText = "Unable to fetch portfolio, try again later")
fetch("weather.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(function(text){
    document.getElementById("portfolio-code5temp").innerText = text.split("\n")[0]
    document.getElementById("portfolio-code5").innerText = text.substring(text.split("\n")[0].length+1)
  })
  .catch(error => document.getElementById("portfolio-code5").innerText = "Unable to fetch portfolio, try again later")
fetch("score.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(function(text){document.getElementById("portfolio-code6p").innerText = text.split("-")[0];document.getElementById("portfolio-code6b").innerText = text.split("-")[1];})
  .catch(error => document.getElementById("portfolio-code6p").innerText = "6", document.getElementById("portfolio-code6b").innerText = "6")

function currentTime() {
  let date = new Date();
  let hh = date.getHours();
  let mm = date.getMinutes();
  let session = "AM";

  if (hh == 0) {
    hh = 12;
  }
  if (hh > 12) {
    hh = hh - 12;
    session = "PM";
  }
  
  hh = (hh < 10) ?  hh : hh;
  mm = (mm < 10) ? "0" + mm : mm;

  let time = hh + ":" + mm + " " + session;

  document.getElementById("clock").innerText = time;
  let t = setTimeout(function () { currentTime() }, 1000);
}
currentTime();