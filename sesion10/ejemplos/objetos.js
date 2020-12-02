function alerta(){
    var mensaje;
    var opcion = confirm("Clic en Aceptar o Cancelar");
    if (opcion == true){
        mensaje = "Escogiste Aceptar";
    }else{
        mensaje = "Escogiste Cancelar";
    }
    document.getElementById("ejemplo").innerHTML = mensaje;
}