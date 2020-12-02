function validar_formulario(){
 var usuario = document.formulario.usuario;
 var correo = document.formulario.email;
 var clave = document.formulario.password;
  
 var usuario_len = usuario.value.length;
 if(usuario_len == 0 || usuario_len < 8)
 {
	alert("Debes ingresar un usuario con mínimo 8 caracteres");
	passid.focus();
	//return false; //Para la parte dos, que los datos se conserven
 }
 
 var formatoCorreo = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
 if(!correo.value.match(formatoCorreo))
 {
	alert("Debes ingresar un correo electronico valido!");
	correo.focus();
	//return false; //Para la parte dos, que los datos se conserven
 }
  var passid_len = clave.value.length;

 if (passid_len == 0 || passid_len < 8)
 {
	alert("Debes ingresar una clave con mas de 8 caracteres");
	passid.focus();
 }
 
}