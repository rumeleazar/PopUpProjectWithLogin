// //FUNCTIONS
// function closeModal() {
//   document.querySelector(".table input[type ='button']").style.display =
//     "block";
//   document.querySelector(".modal").style.display = "none";
//   document.querySelector("body").style.backgroundColor = "rgba(0,0,0,0)";
// }

// function openModal() {
//   document.querySelector(".modal").style.opacity = "1";
//   document.querySelector(".modal").style.display = "block";
//   document.querySelector("body").style.backgroundColor = "rgba(0,0,0,0.7)";
//   document.querySelector(".table input[type ='button']").style.display = "none";
// }

// // USERS PAGE
// function user() {
//   let yes = document.querySelector(".yeslist").childElementCount;
//   let no = document.querySelector(".nolist").childElementCount;
//   let total = yes + no;
//   let yespercent = (yes / total) * 100;
//   let nopercent = (no / total) * 100;

//   document.querySelector(".totalnumber").innerHTML = total;
//   document.querySelector(".yespercent").innerHTML = yespercent.toFixed(2) + "%";
//   document.querySelector(".nopercent").innerHTML = nopercent.toFixed(2) + "%";
// }

// //OPENING THE POP UP MODAL AT PAGE LOAD

// window.addEventListener("load", function () {
//   let list = [];
//   let x = document.querySelectorAll("p");

//   for (var i = 0; i < x.length; i++) {
//     list.push(x[i].textContent);
//   }
//   let y = "{{username}}";

//   if (!list.includes(y)) {
//     setTimeout(function () {
//       openModal();
//     }, 2000);
//   }

//   user();
// });

// //CLOSING THE POP UP MODAL WITH THE CLOSE BUTTON

// document.querySelector(".close").addEventListener("click", function () {
//   closeModal();
// });

// //OPENING MODAL USING THE OPEN SURVEY BUTTON

// document.querySelector(".openModal").addEventListener("click", function () {
//   openModal();
// });

// document.querySelector(".submit").addEventListener("click", function () {
//   closeModal();
// });
