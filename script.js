fetch("/Blair-Day/menu2.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(text => document.getElementById("portfolio-code2").innerText = text)
  .catch(errror => document.getElementById("portfolio-code2").innerText = "Unable to fetch portfolio, try again later")
fetch("/Blair-Day/athletics4.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(text => document.getElementById("portfolio-code3").innerText = text)
  .catch(errror => document.getElementById("portfolio-code3").innerText = "Unable to fetch portfolio, try again later")
fetch("/Blair-Day/calendar2.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(text => document.getElementById("portfolio-code4").innerText = text)
  .catch(errror => document.getElementById("portfolio-code4").innerText = "Unable to fetch portfolio, try again later")
fetch("/Blair-Day/weather.txt")
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Response")
    }
    return response.text()
  })
  .then(text => document.getElementById("portfolio-code5").innerText = text + ' \u2109')
  .catch(errror => document.getElementById("portfolio-code5").innerText = "Unable to fetch portfolio, try again later")

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