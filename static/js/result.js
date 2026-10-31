document.addEventListener("DOMContentLoaded", () => {
  console.log("Resume Analysis Results Loaded");

  const scoreElement = document.getElementById("score");

  if (!scoreElement) return;

  const finalScore = parseInt(scoreElement.textContent.trim(), 10);

  if (isNaN(finalScore)) return;

  scoreElement.textContent = "0";

  let currentScore = 0;

  const interval = setInterval(() => {
    currentScore += 1;

    if (currentScore >= finalScore) {
      currentScore = finalScore;
      clearInterval(interval);
    }

    scoreElement.textContent = currentScore;
  }, 15);
});
