const analyzeForm = document.getElementById("analyzeForm");
const startBtn = document.getElementById("startBtn");
const analyzeBtn = document.getElementById("analyzeBtn");
const loadingOverlay = document.getElementById("loadingOverlay");

// Scroll to upload section
startBtn.addEventListener("click", () => {
  document.getElementById("upload").scrollIntoView({
    behavior: "smooth",
  });
});

// Handle resume submission
analyzeForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const resume = document.getElementById("resume").files[0];
  const role = document.getElementById("role").value;

  if (!resume) {
    alert("Please upload your resume.");
    return;
  }

  if (!resume.name.toLowerCase().endsWith(".pdf")) {
    alert("Please upload a PDF file.");
    return;
  }

  if (!role) {
    alert("Please select a job role.");
    return;
  }

  const formData = new FormData(analyzeForm);

  loadingOverlay.style.display = "flex";
  analyzeBtn.disabled = true;
  analyzeBtn.textContent = "Analyzing...";

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      body: formData,
    });

    const contentType = response.headers.get("content-type") || "";

    if (!response.ok) {
      if (contentType.includes("application/json")) {
        const errorData = await response.json();
        throw new Error(errorData.error || "Analysis failed.");
      }

      throw new Error("Analysis failed. Please try again.");
    }

    const resultHTML = await response.text();

    // Display the results page returned by Flask
    document.open();
    document.write(resultHTML);
    document.close();
  } catch (error) {
    loadingOverlay.style.display = "none";

    analyzeBtn.disabled = false;
    analyzeBtn.textContent = "Analyze";

    alert(error.message);
  }
});
