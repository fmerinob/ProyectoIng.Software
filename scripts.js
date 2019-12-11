function activeModal(accion) {
	var modal = document.getElementById(accion);
	if (!modal.classList.contains("is-active")) {
		modal.classList.add("is-active");
	} else {
		modal.classList.remove("is-active");
	}
}

function login() {
	var email = document.getElementById("email");
	if (email.value === "user@gmail.com") {
		document.location.href = "home.html";
	} else {
		document.location.href = "index.html";
	}

}

function edita() {
	var texto = document.getElementById("input_soft");
	var titulo = document.getElementById("titulo_soft");
	var caja = document.getElementById("caja_soft");
	titulo.innerText = texto.value;
	caja.innerHTML = '<a class="calendar-event is-danger" style="color:white" >' + texto.value + '</a>';

	activeModal('editaActividad');
}

function elimina() {
	var caja = document.getElementById("caja_graduacion");
	caja.remove();
	activeModal('editaActividad2');
}

function agrega() {
	var fecha = document.getElementById("fin_ano");
	fecha.innerHTML = '<button class="date-item" >31</button> <div class="calendar-events"><a class="calendar-event is-warning" onclick="activeModal(' + 'verActividad'+')" style="color:white" id="caja_ano_nuevo">Cena año nuevo</a></div >';
	activeModal('altaActividad');
}
