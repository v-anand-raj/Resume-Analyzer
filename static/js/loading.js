const progressBar = document.getElementById("progressBar");
const percent = document.getElementById("percent");
const steps = ["step1", "step2", "step3", "step4", "step5", "step6"];
let progress = 0;
let currentStep = 0;
const interval = setInterval(() => {
  progress += 2;
  progressBar.style.width = progress + "%";
  percent.innerHTML = progress + "%";
  if (progress % 16 === 0 && currentStep < steps.length) {
    const item = document.getElementById(steps[currentStep]);
    item.innerHTML = "✅ " + item.innerHTML.substring(2);
    currentStep++;
  }
  if (progress >= 100) {
    clearInterval(interval);
    setTimeout(() => {
      window.location.href = "result.html";
    }, 1000);
  }
}, 100);
