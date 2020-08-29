let qouteText = document.getElementById("qoute-text");
let qouteAuthor = document.getElementById("qoute-author");

function fetchQoute() {
  fetch("https://type.fit/api/quotes")
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data);
      //   console.log(qouteText.innerHTML = ran.text)
      let initialQoute = data[Math.floor(Math.random() * data.length)];
      qouteText.innerHTML = initialQoute.text;

      qouteAuthor.innerHTML = `"${initialQoute.author}"`;
      qouteAuthor.innerHTML =
        initialQoute.author === null ? "" : `"${initialQoute.author}"`;
      //   setInterval(() => {
      //     let newQoute = newQoute + initialQoute
      //     qouteText.innerHTML = newQoute.text
      //     qouteAuthor.innerHTML = `${newQoute.author}`
      //     console.log(ran)
      // }, 1000)
    })
    .catch((err) => {
      console.log("there was an error fetching" + err);
    });
}

fetchQoute();
