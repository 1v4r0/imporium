var btn = document.getElementsByClassName("collapse");
for(let i=0;i<btn.length;i++){
btn[i].addEventListener("click", function () {
  this.classList.toggle("active");
  var content = this.nextElementSibling;
  if (content.style.display === "block") {
      content.style.display = "none";
  } else {
      content.style.display = "block";
  }
})};
