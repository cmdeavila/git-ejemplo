function validar_formulario(){
    var usuario = document.formulario.nomusuario;
    var clave = document.formulario.pass;

    var usuario_len = usuario.value.length;
    if (usuario_len == 0 || usuario_len<8){
        alert("Debe ingresar un usuario con mínimo 8 caracteres");
    }

    var pass_len = clave.value.length;
    if(pass_len == 0 || pass_len < 8){
        alert("Debe ingresar una clave con mínimo 8 caracteres");
    }
}

function mostrarPassword(obj) {
    var obj = document.getElementById('pass');
    obj.type = "text";
  }
  function ocultarPassword(obj) {
    var obj = document.getElementById('pass');
    obj.type = "password";
  }
  function showForm(){
      document.getElementById('loginForm').style.display = "block";
  }
  
  function hideForm(){
      document.getElementById('loginForm').style.display = "none";
  }