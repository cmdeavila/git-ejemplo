function consultarEst(){
    document.getElementById("formulario").action="/estudiante/get";
}

function guardarEst(){
    document.getElementById("formulario").action="/estudiante/save";
}

function listarEst(){
    document.getElementById("formulario").action="/estudiante/list";
}

function eliminarEst(){
    document.getElementById("formulario").action="/estudiante/delete";
}

function actualizarEst(){
    document.getElementById("formulario").action="/estudiante/update";
}

function insertar(){
    document.getElementById("formulariologin").action="/login/save";
}