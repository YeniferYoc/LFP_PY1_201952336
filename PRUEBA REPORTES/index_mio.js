function form_mio(valor) {
    /*
        document: hace referencia a la pagina web cargada en el navegador
        getElementById(): obtiene el elemento html asociado al id que le pasemos por parametro
        style: accede a la propiedad style de la etiqueta html obtenida y modifica cualquier propiedad 
        perteneciente a este atributo, style es refernte al css de esa etiqueta
    */
    if (valor == 1) { document.getElementById("formulario").style.display = ""; }
    else { document.getElementById("formulario").style.display = "none"; }

}

// async: funcion que puede contener await adentro de ella
async function formulario(){
    // value: Retorna el valor asociado a la etiqueta
    // value: Retorna el valor asociado a la etiqueta
    let num1 = document.getElementById("numero1").value
    let num2 = document.getElementById("numero2").value
    let operr = document.getElementById("operador").value
    $("#numero1_res").text("");
    $("#result").text(num1 + " is valid :)");
    $("#result").css("color", "green");

    
    document.getElementById("Resul").value = document.getElementById("numero1").value
    alert("dddd")

    document.getElementById("numero1").value = ""
    document.getElementById("numero2").value = ""
    document.getElementById("operador").value = ""

}

async function mostrarContactos() {
    let cuerpo = document.getElementById("tbody")
     //innerHTML: modifica el contenido que se encuentra como hijo de la etiqueta especificada
    cuerpo.innerHTML = "";

    let peticion = await fetch("http://localhost:4000/devolver_todo")
    let respuesta = await peticion.json()
    console.log(respuesta)
    respuesta = respuesta.Data_User
    for (let i = 0; i < respuesta.length; i++){
        console.log(respuesta[i].nombre_usuario)
        // createElement(): crea una etiqueta del tipo que es pasado por parametro
        let tr = document.createElement("tr")
        let th = document.createElement("th")
        th.scope = "row" // scope: especifica que esa etiqueta es la cabecera, en este caso de la fila
        th.innerHTML = i + 1
        tr.appendChild(th) //appendChild(): agrega un nuevo hijo a la etiqueta especificada

        let td = document.createElement("td")
        td.innerHTML = respuesta[i].nombre
        tr.appendChild(td)

        td = document.createElement("td")
        td.innerHTML = respuesta[i].nombre_usuario
        tr.appendChild(td)

        td = document.createElement("td")
        td.innerHTML = respuesta[i].correo
        tr.appendChild(td)

        td = document.createElement("td")
        td.innerHTML = respuesta[i].genero
        tr.appendChild(td)

        cuerpo.appendChild(tr);
    }    
}

async function eliminar() {
    let correo = document.getElementById("correo_eliminar").value

    let peticion = await fetch("http://localhost:4000/deleteuser", {
        method: "delete",
        headers: {"Content-Type": 'application/json'},
        body: JSON.stringify({
            correo: correo,
        })
    })
    let respuesta = await peticion.json()
    alert(respuesta.Estado)
    document.getElementById("correo_eliminar").value = ""
}


async function Buscar(){
    let correo = document.getElementById("correo_edit").value

    let peticion = await fetch("http://localhost:4000/buscar_usuario", {
        method: "post",
        headers: {"Content-Type": 'application/json'},
        body: JSON.stringify({
            correo: correo,
        })
    })
    let respuesta = await peticion.json()
    respuesta = respuesta.Data_User
    console.log(respuesta.nombre_usuario)


    document.getElementById("correo_edit").value = respuesta.correo
    document.getElementById("password_edit").value = respuesta.password
    document.getElementById("nombre_edit").value = respuesta.nombre
    document.getElementById("genero_edit").value = respuesta.genero
    document.getElementById("nombre_usuario_edit").value = respuesta.nombre_usuario
}

async function editar() {


    let correo = document.getElementById("correo_edit").value
    let password = document.getElementById("password_edit").value
    let nombre = document.getElementById("nombre_edit").value
    let genero = document.getElementById("genero_edit").value
    let nombreusuario = document.getElementById("nombre_usuario_edit").value

    let peticion = await fetch("http://localhost:4000/actualizar" , {
        method: "post",
        headers: {"Content-Type": 'application/json'},
        body: JSON.stringify({
            correo: correo,
            password: password,
            nombre: nombre,
            Genero: genero,
            Nombre_usuario: nombreusuario
        })
    })
    let respuesta = await peticion.json()
    alert(respuesta.mensaje)

    document.getElementById("correo_edit").value = ""
    document.getElementById("password_edit").value = ""
    document.getElementById("nombre_edit").value = ""
    document.getElementById("genero_edit").value =""
    document.getElementById("nombre_usuario_edit").value = ""
}
