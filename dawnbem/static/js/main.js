const fila = document.querySelector('.contenedor-carousel');
const deporte = document.querySelectorAll('.deporte');

const flechaIzquierda = document.getElementById('flecha-izquierda');
const flechaDerecha = document.getElementById('flecha-derecha');

flechaDerecha.addEventListener('click', () => {
fila.scrollLeft += fila.offsetWidth;

const indicadorActivo = document.querySelector('.indicadores .activo');
if(indicadorActivo.nextSibling){
indicadorActivo.nextSibling.classList.add('activo'); 
indicadorActivo.classList.remove('activo');   
}
});
flechaIzquierda.addEventListener('click', () => {
fila.scrollLeft -= fila.offsetWidth;
const indicadorActivo = document.querySelector('.indicadores .activo');
if(indicadorActivo.previousSibling){
indicadorActivo.previousSibling.classList.add('activo'); 
indicadorActivo.classList.remove('activo');   
}
});

const numeroPaginas = Math.ceil(deporte.length / 5);
for(let i = 0; i < numeroPaginas; i++){
const indicador = document.createElement('button');

if(i === 0){
indicador.classList.add('activo');
}
document.querySelector('.indicadores').appendChild(indicador);
indicador.addEventListener('click', (e) => {
fila.scrollLeft = i * fila.offsetWidth;
document.querySelector('.indicadores .activo').classList.remove('activo');
e.target.classList.add('activo');
});

}
deporte.forEach((deporte) => {
deporte.addEventListener('mouseenter', (e) => {
 const elemento = e.currentTarget;
 setTimeout(() => {
    deporte.forEach(deporte => deporte.classList.remove('hover'));
    elemento.classList.add('hover');
 },300);
    });
});
fila.addEventListener('mouseleave', () => {
deporte.forEach(deporte => deporte.classList.remove('hover'));
});


document.querySelector(".scroll-down-btn").addEventListener("click", function (event) {
   event.preventDefault();
   const mainContentElement = document.getElementById("main-content");
   const mainContentOffset = mainContentElement.offsetTop;
   window.scrollTo({
   top: mainContentOffset,
   behavior: "smooth",
   });
});
// Get the HTML body element
const bodyElement = document.querySelector('body');

// Wait for the window to load and then add the 'loaded' class to the body element
window.addEventListener('load', () => {
  bodyElement.classList.add('loaded');
});

$(function() {
	$(".btn").click(function() {
		$(".form-signin").toggleClass("form-signin-left");
    $(".form-signup").toggleClass("form-signup-left");
    $(".frame").toggleClass("frame-long");
    $(".signup-inactive").toggleClass("signup-active");
    $(".signin-active").toggleClass("signin-inactive");
    $(".forgot").toggleClass("forgot-left");   
    $(this).removeClass("idle").addClass("active");
	});
});

$(function() {
	$(".btn-signup").click(function() {
  $(".nav").toggleClass("nav-up");
  $(".form-signup-left").toggleClass("form-signup-down");
  $(".success").toggleClass("success-left"); 
  $(".frame").toggleClass("frame-short");
	});
});

$(function() {
	$(".btn-signin").click(function() {
  $(".btn-animate").toggleClass("btn-animate-grow");
  $(".welcome").toggleClass("welcome-left");
  $(".cover-photo").toggleClass("cover-photo-down");
  $(".frame").toggleClass("frame-short");
  $(".profile-photo").toggleClass("profile-photo-down");
  $(".btn-goback").toggleClass("btn-goback-up");
  $(".forgot").toggleClass("forgot-fade");
	});
});