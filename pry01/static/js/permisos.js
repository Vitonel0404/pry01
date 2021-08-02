function docuementCargado(){
    var a = document.getElementById('usu').textContent;

    if(a == 'True'){
        $("#mant").show()
    }else{
        $("#mant").hide()
    }
}

document.addEventListener('DOMContentLoaded', docuementCargado, false);


function cargarDatos(){
    $(document).on("click", ".btn-editar", function(){
        fila = $(this).closest("tr");                 
        dni = fila.find('td:eq(0)').text(); //capturo el ID
        nom = fila.find('td:eq(1)').text();
        ape = fila.find('td:eq(2)').text();
        em = fila.find('td:eq(3)').text();
        tel = parseInt(fila.find('td:eq(4)').text());
        dir = fila.find('td:eq(5)').text();
        rol=fila.find('td:eq(6)').text();
        
        document.getElementById('dni_up').value=dni;
        document.getElementById('nombres_up').value=nom;
        document.getElementById('apellidos_up').value=ape;
        document.getElementById('email_up').value=em;
        document.getElementById('telefono_up').value=tel;
        document.getElementById('direccion_up').value=dir;
        document.getElementById('rol_up').value=rol;
        
    })
}

