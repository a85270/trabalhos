$(document).ready(function() {
    // Adicione interatividade ao seu menu aqui
    $('.menu-item').hover(
        function() {
            $(this).css('background-color', '#ddd');
            // Mostrar submenu
            $(this).find('.submenu').stop(true, true).slideDown();
        }, 
        function() {
            $(this).css('background-color', 'transparent');
            // Esconder submenu
            $(this).find('.submenu').stop(true, true).slideUp();
        }
    );

    // Abrir janela pop-up com imagem ampliada ao clicar
    $('.gallery img').click(function() {
        var imgUrl = $(this).attr('src');
        window.open(imgUrl, '_blank', 'width=800,height=600');
    });

    let slideIndex = 0;
    showSlides();

    function showSlides() {
let i;
let slides = document.getElementsByClassName("mySlides");
let dots = document.getElementsByClassName("dot");
for (i = 0; i < slides.length; i++) {
slides[i].style.display = "none";  
}
slideIndex++;
if (slideIndex > slides.length) {slideIndex = 1}    
for (i = 0; i < dots.length; i++) {
dots[i].className = dots[i].className.replace(" active", "");
}
slides[slideIndex-1].style.display = "block";  
dots[slideIndex-1].className += " active";
setTimeout(showSlides, 2000); // Change image every 2 seconds
}
});
$(document).ready(function() {
    // Função para definir um cookie e enviar para o servidor
    function setCookieAndSendToServer(name, value, days) {
        setCookie(name, value, days); // Função setCookie definida anteriormente
        // Envia os dados do cookie para o servidor
        $.ajax({
            url: 'store_cookies.php',
            method: 'POST',
            data: { name: name, value: value },
            success: function(response) {
                console.log('Cookie enviado para o servidor com sucesso.');
            },
            error: function(xhr, status, error) {
                console.error('Erro ao enviar cookie para o servidor:', error);
            }
        });
    }

    
    $('.menu-item').hover(
        function() {
            $(this).css('background-color', '#ddd');
            // Mostrar submenu
            $(this).find('.submenu').stop(true, true).slideDown();
        }, 
        function() {
            $(this).css('background-color', 'transparent');
            // Esconder submenu
            $(this).find('.submenu').stop(true, true).slideUp();
        }
    );

});

function loadDoc() {
const xhttp = new XMLHttpRequest();
xhttp.onload = function() {
document.getElementById("demo").innerHTML =
this.responseText;
}
xhttp.open("GET", "ajax_info.txt");
xhttp.send();
}