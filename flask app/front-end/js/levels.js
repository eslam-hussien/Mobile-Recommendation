import { renderDiv } from "./helper.js";

function onNextLevelClicked(e, interests) {
  e.target.setAttribute("disabled", true);
  getLevels(interests);
  localStorage.setItem("interests", JSON.stringify(interests));
  location.href = "orders.html";
}

function renderLevels() {
  const interests = JSON.parse(localStorage.getItem("interests"));
  if (interests) {
    renderDiv("#levels", interests, onNextLevelClicked);
  }
}

function getLevels(interests) {
  const selectBoxes = document.querySelectorAll(".select-input");
  selectBoxes.forEach((select) => {
    if (interests[+select.getAttribute("index")] && select.value)
      interests[+select.getAttribute("index")].level = select.value;
  });
  return interests;
}

renderLevels();
