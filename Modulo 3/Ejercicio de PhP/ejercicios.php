<?php
$pares = 0;
$impares = 0;

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}

echo "Cantidad de pares: $pares\n";
echo "Cantidad de impares: $impares\n";
?>

<?php
for ($i = 1; $i <= 10; $i++) {
    echo "8 x " . $i . " = " . (8 * $i) . "\n";
}
echo "\n";
?>

<?php
$suma = 0;

for ($i = 1; $i <= 100; $i += 2) {
    $suma += $i;
}

echo "Suma de impares del 1 al 100: $suma\n";
?>

<?php






