function guardarEst(){
    document.getElementById("formulario").action="/estudiante/save";
}

function consultarEst(){
    document.getElementById("formulario").action="/estudiante/get";
}

function listarEst(){
    document.getElementById("formulario").action="/estudiante/list";
}