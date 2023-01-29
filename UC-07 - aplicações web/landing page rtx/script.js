// parte do MATHEUS

// Nav Bar Burguer Menu
const burguer = document.querySelector(".burguer")
const navMenu = document.querySelector(".nav-menu")

burguer.addEventListener("click", () => {
    burguer.classList.toggle('active')
    navMenu.classList.toggle('active')

})
// Fim do burguer menu

// Slider Carousel automático
var slideIndex = 0;
var slides = document.getElementsByClassName("slide");
var indicators = document.getElementsByClassName("indicator");

//Função para mostrar o slide atual e esconder os outros
function showSlides() {
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    indicators[i].className = indicators[i].className.replace(" active", "");
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex-1].style.display = "block";
  indicators[slideIndex-1].className += " active";
  setTimeout(showSlides, 3000);
}

showSlides();
// fim do sleider carousel

// parte do EDUARDO
$(document).ready(function(){
  $("#whatsapp").mask("(00) 00000-0000");
});

