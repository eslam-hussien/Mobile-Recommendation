import { fillTemplate, getData } from "./helper.js";

const parentDiv = document.querySelector("#render-area");
const temp = document.querySelector("#show").innerHTML;
const newDiv = document.createElement("div");

function display(product) {
  newDiv.appendChild(fillTemplate(temp, product));
  parentDiv.appendChild(newDiv);
}
function displayError(error) {
  newDiv.innerHTML = `<h1>An error happened</h1><br>
                      <h4>seems like ther is a validation error due to incorrect data
                      was sent to server</h4><br><hr>
                      <h4 style="color: red;">error: ${error}</h4>
  `;
  parentDiv.appendChild(newDiv);
}
async function renderProducts() {
  const interests = JSON.parse(localStorage.getItem("sendData"));

  const products = await getData(interests);
  if (products.status === 400) {
    displayError(products.error);
  } else {
    products.forEach((p) => {
      display({ mobile: p.mobile, ram: p.ram, price: p.price_egp });
    });
  }
}

renderProducts();
