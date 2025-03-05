import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function fetchPlayers() {
  try {
    const filePath = path.join(__dirname, "players.json");
    const data = await fs.readFile(filePath);
    return JSON.parse(data);
  } catch (err) {
    console.error(err.message);
    return [];
  }
}

async function listPlayers() {
  const players = await fetchPlayers();
  return players;
}

const players = await listPlayers();

console.log(players);

const firstPlayer = players[0];

const lastPlayer = players.at(-1);

const personWithHScore = players.reduce(
  (max, player) => (player.score > max.score ? player : max),
  players[0]
);

const playersAfterDaniel = [];
for (let i = 0; i < players.length; i++) {
  if (players[i].name === "Daniel") {
    playersAfterDaniel.push(players[i + 1]);
  }
}

console.log(firstPlayer, "<====First Player");
console.log(lastPlayer, "<===Last player");
console.log(personWithHScore, "Player with highest score");

console.log(playersAfterDaniel, "Players after Daniel");
