import { renderDiv } from "./helper.js";

function onSubmitClicked(e, interests) {
  e.target.setAttribute("disabled", true);
  interests = getOrders(interests);
  localStorage.setItem("sendData", JSON.stringify(interests));
  location.href = "show.html";
}
function getOrders(interests) {
  const orderInputs = document.querySelectorAll(".order-inputs");
  const budgetInput = document.querySelector("#budget");
  let budget = 0;
  if (budgetInput && budgetInput.value) {
    budget = budgetInput.value;
  }
  orderInputs.forEach((orderInput) => {
    if (interests[+orderInput.getAttribute("index")] && orderInput.value)
      interests[+orderInput.getAttribute("index")].order = orderInput.value;
  });
  interests = interests.map((el) => {
    return { id: +el.id, level: +el.level, order: +el.order };
  });
  return { interests: interests, budget: +budget };
}

function renderOrders() {
  const interests = JSON.parse(localStorage.getItem("interests"));
  if (interests) {
    renderDiv("#orders", interests, onSubmitClicked);
  }
}

renderOrders();
