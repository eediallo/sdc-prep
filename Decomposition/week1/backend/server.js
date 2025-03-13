import express from "express";

const app = express();
const port = 3000;

const quotes = [
  {
    quote: "Either write something worth reading or do something worth writing.",
    author: "Benjamin Franklin",
  },
  {
    quote: "I should have been more kind.",
    author: "Clive James",
  },
];

function randomQuote() {
  const index = Math.floor(Math.random() * quotes.length);
  return quotes[index];
}

app.get("/", (req, res) => {
    console.error('Request received from the client.')
  const quote = randomQuote();
  res.send(`"${quote.quote}" -${quote.author}`);
});

app.post("/", (req, res) => {
  const bodyBytes = [];
  req.on("data", chunk => bodyBytes.push(...chunk));
  req.on("end", () => {
    const bodyString = String.fromCharCode(...bodyBytes);
    console.log(bodyString, 'body string =====>')
    let body;
    try {
      body = JSON.parse(bodyString);
    } catch (error) {
      console.error(`Failed to parse body ${bodyString} as JSON: ${error}`);
      res.status(400).send("Expected body to be JSON.");
      return;
    }
    if (typeof body != "object" || !("quote" in body) || !("author" in body)) {
      console.error(`Failed to extract quote and author from post body: ${bodyString}`);
      res.status(400).send("Expected body to be a JSON object containing keys quote and author.");
      return;
    }
    quotes.push({
      quote: body.quote,
      author: body.author,
    });
    console.log(quotes)
    res.send("ok");
  });
});

app.listen(port, () => {
  console.error(`Quote server listening on port ${port}`);
});