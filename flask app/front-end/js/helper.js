const actionButton = document.querySelector("#action-btn");
const parentDiv = document.querySelector("#render-area");

// ===================== ui ======================//
function fillTemplate(templateHml, data) {
  Object.keys(data).forEach(function (key) {
    let placeHolder = "{{" + key + "}}";
    let val = data[key];
    while (templateHml.indexOf(placeHolder) !== -1) {
      templateHml = templateHml.replace(placeHolder, val);
    }
  });
  const div = document.createElement("div");
  div.innerHTML = templateHml;
  return div;
}

function renderDiv(selector, data, callBack) {
  if (actionButton) actionButton.setAttribute("disabled", true);
  const temp = document.querySelector(selector).innerHTML;
  const newDiv = document.createElement("div");
  data.forEach((interest, index) => {
    newDiv.appendChild(
      fillTemplate(temp, {
        interestId: interest.id,
        interestName: interest.name,
        index: index,
      })
    );
  });
  parentDiv.appendChild(newDiv);
  if (actionButton) {
    actionButton.removeAttribute("disabled");
    actionButton.addEventListener("click", (e) => callBack(e, data));
  }
}
//======================= ui =================//

// ============requests ===========================//
async function getInterests() {
  const data = await fetch("http://localhost:5000/interests");
  const interests = await data.json();
  return interests;
}

async function getData(interests) {
  const data = await fetch("http://localhost:5000/products", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(interests),
  })
    .then((res) => {
      return res.json();
    })
    .catch((err) => {
      return err;
    });

  return data;
}
//========================== requests =======================//

export { renderDiv, getData, getInterests, fillTemplate };
