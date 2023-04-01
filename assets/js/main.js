// @ts-nocheck

$(function () {
  $("[data-toggle='tooltip']").tooltip();
  $("#enviar").click(function () {
    alert("Enviado correctamente");
  });
});

$("h4").dblclick(function(){
  $(this).addClass("red");
});

$("#ct").click(function(){
  $( "#cx" ).toggle(800);
});

$("#ctdos").click(function(){
  $( "#cxdos" ).toggle(800);
});

$("#cttres").click(function(){
  $( "#cxtres" ).toggle(800);
});

function crearUsuario() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  localStorage.setItem('username', username);
  localStorage.setItem('password', password);
  alert('Credenciales guardadas.');
  // Envia a login.
  window.location.href = "login.html";
}

function iniciarSesion() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const storedUsername = localStorage.getItem('username');
  const storedPassword = localStorage.getItem('password');

  if (username === storedUsername && password === storedPassword) {
    alert('Inicio de sesión exitoso.');
    // Envia a página principal
    window.location.href = "index.html";
  } else {
    alert('Error vuelve a intentarlo.');
  }
}