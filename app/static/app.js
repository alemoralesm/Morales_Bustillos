const nombre = document.getElementById("nombre")
const apellidop = document.getElementById("apellidop")
const apellidom = document.getElementById("apellidom")
const rut = document.getElementById("rut")
const direccion = document.getElementById("direccion")
const email = document.getElementById("email")
const telefono = document.getElementById("telefono")
const form = document.getElementById("form")
const parrafo= document.getElementById("warnings")

form.addEventListener("submit", function(event) {
    event.preventDefault(); // Evita que se envíe el formulario automáticamente
  
    var warnings = []; // Array para almacenar los mensajes de advertencia
  
    // Validación del campo "nombre"
    if (nombre.value.trim() === "") {
      warnings.push("El campo Nombre es obligatorio");
    } else if (!validarSoloPalabras(nombre.value)) {
      warnings.push("El campo Nombre solo debe contener palabras, sin números");
    }
  
    // Validación del campo "apellidop"
    if (apellidop.value.trim() === "") {
      warnings.push("El campo Apellido Paterno es obligatorio");
    }
  
    // Validación del campo "apellidom"
    if (apellidom.value.trim() === "") {
      warnings.push("El campo Apellido Materno es obligatorio");
    }
  
    // Validación del campo "rut"
    if (rut.value.trim() === "") {
      warnings.push("El campo RUT es obligatorio");
    }
  
    // Validación del campo "direccion"
    if (direccion.value.trim() === "") {
      warnings.push("El campo Dirección es obligatorio");
    }
  
    // Validación del campo "email"
    if (email.value.trim() === "") {
      warnings.push("El campo Email es obligatorio");
    } else if (!validarEmail(email.value)) {
      warnings.push("El campo Email no tiene un formato válido");
    }
  
    // Validación del campo "telefono"
    if (telefono.value.trim() === "") {
      warnings.push("El campo Teléfono es obligatorio");
    }
  
    // Mostrar los mensajes de advertencia
    if (warnings.length > 0) {
      parrafo.innerHTML = warnings.join("<br>");
    } else {
      form.submit(); // Enviar el formulario si no hay advertencias
    }
  });
  
  // Función para validar que solo se ingresen palabras (sin números)
  function validarSoloPalabras(texto) {
    var re = /^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$/;
    return re.test(texto);
  }
  
  // Función para validar el formato de un email
  function validarEmail(email) {
    var re = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    return re.test(email);
  }
  
  