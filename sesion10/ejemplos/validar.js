function validarExtension(){
    let arh = document.getElementById("archivo");
    let ext = ["jgp","png"];
    nomArchivo = arh.value;
    extension = nomArchivo.split(".")[1];
    let permitido = false;
    for(i in ext){
        if (ext[i]==extension){
            permitido=true;
        }
    }
    if (permitido){
        alert("Documento permitido");
    } else{
        alert("Documento no permitido");
    }
}