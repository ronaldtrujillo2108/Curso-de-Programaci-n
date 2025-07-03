const nombreProducto = "Tablet 10 pulgadas";
let precio = 450.99;
let stock = 25;
const envioGratis = true;

console.log("Nombre del producto:", nombreProducto);
console.log("Precio:", precio);
console.log("Stock disponible:", stock);
console.log("¿Envío gratis?:", envioGratis);

let cantidad = 2;
let subtotal = precio * cantidad;
let impuesto = subtotal * 0.07;
let total = subtotal + impuesto;

console.log("Subtotal:", subtotal.toFixed(2));
console.log("Total con impuesto:", total.toFixed(2));

let edadUsuario = 20;
if (edadUsuario >= 18) {
  console.log("Puedes obtener tu licencia de conducir.");
} else {
  console.log("Aún no tienes la edad para obtener la licencia.");
}

let colorSemaforo = "amarillo";
if (colorSemaforo === "verde") {
  console.log("Puede avanzar.");
} else if (colorSemaforo === "amarillo") {
  console.log("Reduzca la velocidad, precaución.");
} else if (colorSemaforo === "rojo") {
  console.log("Debe detenerse.");
} else {
  console.log("Color no válido.");
}

let diaSemana = 3;
switch (diaSemana) {
  case 1:
    console.log("Lunes: Lentejas");
    break;
  case 2:
    console.log("Martes: Pollo al horno");
    break;
  case 3:
    console.log("Miércoles: Pescado a la plancha");
    break;
  case 4:
    console.log("Jueves: Pasta");
    break;
  case 5:
    console.log("Viernes: Paella");
    break;
  default:
    console.log("Día no válido para menú.");
}

for (let i = 2; i <= 20; i += 2) {
  console.log(i);
}

let contador = 10;
while (contador > 0) {
  console.log(contador);
  contador--;
}
console.log("¡Despegue!");

for (let i = 1; i <= 50; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}

let sumaTotal = 0;
for (let i = 1; i <= 100; i++) {
  sumaTotal += i;
}
console.log("Suma total del 1 al 100:", sumaTotal);

let edad = 19;
let tieneEntrada = false;

if (edad >= 18 && tieneEntrada) {
  console.log("Acceso concedido");
} else {
  console.log("Acceso denegado");
}

edad = 22;
tieneEntrada = true;

if (edad >= 18 && tieneEntrada) {
  console.log("Acceso concedido");
} else {
  console.log("Acceso denegado");
}
