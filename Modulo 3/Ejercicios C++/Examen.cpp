#include <iostream>
#include <cmath>
#define LIMITE 10
using namespace std;

void calcularPerimetro(double radio);
float calcularAreaRectangulo(float base, float altura);
void modificarPorValor(int numero);
void modificarPorReferencia(int &numero);

int main() {
    cout << "¡Hola, Mundo!" << endl;

    int entero = 10;
    float flotante = 3.14;
    char caracter = 'A';
    bool booleano = true;

    cout << entero << endl;
    cout << flotante << endl;
    cout << caracter << endl;
    cout << booleano << endl;

    double num1, num2;
    cout << "Ingresa el primer número: ";
    cin >> num1;
    cout << "Ingresa el segundo número: ";
    cin >> num2;

    cout << num1 + num2 << endl;
    cout << num1 - num2 << endl;
    cout << num1 * num2 << endl;
    if (num2 != 0)
        cout << num1 / num2 << endl;
    else
        cout << "Error" << endl;

    cout << pow(num1, num2) << endl;
    if (num1 >= 0)
        cout << sqrt(num1) << endl;
    else
        cout << "Error" << endl;

    int edad;
    cout << "Ingresa tu edad: ";
    cin >> edad;
    if (edad >= 18)
        cout << "Eres mayor de edad." << endl;
    else
        cout << "Eres menor de edad." << endl;

    int numero;
    cout << "Ingresa un número: ";
    cin >> numero;
    for (int i = 1; i <= LIMITE; i++) {
        cout << numero << " x " << i << " = " << numero * i << endl;
    }

    int intento;
    int numeroSecreto = 42;
    cout << "Adivina el número secreto: ";
    cin >> intento;
    while (intento != numeroSecreto) {
        if (intento < numeroSecreto)
            cout << "Más alto. Intenta de nuevo: ";
        else
            cout << "Más bajo. Intenta de nuevo: ";
        cin >> intento;
    }
    cout << "¡Correcto!" << endl;

    int opcion;
    do {
        cout << "1. Saludar\n2. Despedirse\n3. Salir\nSelecciona una opción: ";
        cin >> opcion;
        switch (opcion) {
            case 1:
                cout << "¡Hola!" << endl;
                break;
            case 2:
                cout << "¡Adiós!" << endl;
                break;
            case 3:
                cout << "Saliendo..." << endl;
                break;
            default:
                cout << "Opción inválida." << endl;
        }
    } while (opcion != 3);

    float base, altura;
    cout << "Ingresa la base del rectángulo: ";
    cin >> base;
    cout << "Ingresa la altura del rectángulo: ";
    cin >> altura;
    float area = calcularAreaRectangulo(base, altura);
    cout << "Área del rectángulo: " << area << endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}
