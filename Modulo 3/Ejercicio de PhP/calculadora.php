Calculadora Simple<
    <?php
    
     $numero1 = 100 ;
     $numero2 = 50 ;
     
     echo "Suma: " . ($numero1 + $numero2) . "\n";          
     echo "Resta: " . ($numero1 - $numero2) . "\n";         
     echo "Multiplicación: " . ($numero1 * $numero2) . "\n"; 
     echo "División: " . ($numero1 / $numero2) . "\n";       
     echo "Módulo: " . ($numero1 % $numero2) . "\n\n";      
     
    ?>

<?php
$Metodos_pagos = "Pago movil";


switch ($Metodos_pagosetodos) {
    case "Pago movil":
        echo "Pago movil verifique los datos antes de la operacion";
        break;
        
    case  "Zelle":
        echo "Zelle verifique el correo antes de proceder";
        break;    
         
     case "efectivo":
        echo "Pago en efectivo ";
        break;
}
?>




