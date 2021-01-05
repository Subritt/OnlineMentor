document.addEventListener("DOMContentLoaded", (event) => {
  setTimeout(() => {
    const richTestEditor = document.getElementById("cke_id_content");
    console.log(richTestEditor);
    richTestEditor.style.width = 'auto';
    console.log("width re-adjusted");
  }, 500);
});
