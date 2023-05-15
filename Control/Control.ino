int pulsadorLe = 13;
int pulsadorUp = 12;
int pulsadorDo = 11;
int pulsadorRi = 10;
int pulsadorSe = 7;
int pulsadorSt = 6;
int pulsadorB = 4;
int pulsadorA = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(pulsadorUp, INPUT_PULLUP);
  pinMode(pulsadorLe, INPUT_PULLUP);  
  pinMode(pulsadorRi, INPUT_PULLUP);
  pinMode(pulsadorDo, INPUT_PULLUP);
  pinMode(pulsadorSe, INPUT_PULLUP);
  pinMode(pulsadorSt, INPUT_PULLUP);
  pinMode(pulsadorB, INPUT_PULLUP);
  pinMode(pulsadorA, INPUT_PULLUP);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(pulsadorUp) == 0) {
    Serial.println("arriba");
  }

  if (digitalRead(pulsadorLe) == 0) {
    Serial.println("izquierda");
  }

  if (digitalRead(pulsadorRi) == 0) {
    Serial.println("derecha");
  }

  if (digitalRead(pulsadorDo) == 0) {
    Serial.println("abajo");
  }

  if (digitalRead(pulsadorSe) == 0) {
    Serial.println("seleccionar");
    delay(100);
  }

  if (digitalRead(pulsadorSt) == 0) {
    Serial.println("iniciar");
    delay(100);
  }

  if (digitalRead(pulsadorB) == 0) {
    Serial.println("B");
    delay(100);
  }

  if (digitalRead(pulsadorA) == 0) {
    Serial.println("A");
    delay(100);
  }

  if (digitalRead(pulsadorSe) == 0 && digitalRead(pulsadorSt) == 0) {
    Serial.println("apagar");
  }

  delay(20);

}
