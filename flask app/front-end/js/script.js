import { renderDiv, getInterests } from "./helper.js";

function onNextInterestClicked(e) {
  e.target.setAttribute("disabled", true);
  const interests = getSelectedInterests();
  localStorage.setItem("interests", JSON.stringify(interests));
  location.href = "levels.html";
}

function getSelectedInterests() {
  const checkBoxes = document.querySelectorAll(".checkbox-input");
  const selectedBoxes = [];
  checkBoxes.forEach((box) => {
    if (box.checked) {
      selectedBoxes.push({ id: box.value, name: box.getAttribute("nombre") });
    }
  });
  return selectedBoxes;
}
async function renderInterests() {
  const interests = await getInterests();
  renderDiv("#interests", interests, onNextInterestClicked);
}
renderInterests();
