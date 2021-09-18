function guardarEst(){
    document.getElementById("formulario").action="/estudiante/save";
}

function consultarEst(){
    document.getElementById("formulario").action="/estudiante/get";
}

function listarEst(){
    document.getElementById("formulario").action="/estudiante/list";
}

function borrarEst(){
    document.getElementById("formulario").action="/estudiante/delete";
}

function actualizarEst(){
    document.getElementById("formulario").action="/estudiante/update";
}

function enviar(){
    document.getElementById("formulario").action="/login";
}
function insertar(){
    document.getElementById("formulario").action="/login/save";
}
function registrar(){
    document.getElementById("formulario").action="/registrar";
}
