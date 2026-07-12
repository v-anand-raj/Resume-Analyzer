const startBtn = document.getElementById("startBtn");
startBtn.addEventListener("click", () => {
  document.getElementById("upload").scrollIntoView({
    behavior: "smooth",
  });
});
