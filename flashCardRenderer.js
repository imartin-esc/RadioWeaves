async function readJsonFile(path) {
  try {
    const response = await fetch(path);

    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    const data = await response.json();
    return data;

  }
  catch (error) {
    console.error("Error reading json file", error);
    return null;
  }
}
async function getFlashCardDomElement(question) {
  const fileName = "json files/" + question.slice(0, 3) + ".json";
  const jsonData = await readJsonFile(fileName);
  console.log(jsonData);
  for (let card of jsonData) {
    console.log(`correct answer: ${card}`);
    if (card.id.toLowerCase() === question.toLowerCase()) {
      console.log(`the question is: ${card.question}`);
      let element = document.createElement("div");
      element.style = `
        width: 100px;
        height: 100px;
        background-color: #ff0000;
      `;
      return element;
      break;
    }
  }
}