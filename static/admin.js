function admin() {
  // ADMIN PAGE

  let yesadmin = document.querySelector(".yeslistadmin").childElementCount;
  let noadmin = document.querySelector(".nolistadmin").childElementCount;
  let totaladmin = yesadmin + noadmin;
  let yesadminpercent = (yesadmin / totaladmin) * 100;
  let noadminpercent = (noadmin / totaladmin) * 100;

  document.querySelector(
    ".yesnumber"
  ).innerHTML = `${yesadmin}  (${yesadminpercent.toFixed(2)}%)`;
  document.querySelector(
    ".nonumber"
  ).innerHTML = `${noadmin}  (${noadminpercent.toFixed(2)}%)`;
  document.querySelector(".totaladmin").innerHTML = totaladmin;
}

window.addEventListener("load", function () {
  admin();
});
