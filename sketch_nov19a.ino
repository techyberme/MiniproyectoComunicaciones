#include <WiFi.h>

const char* ssid  = "WifiJavi";
const char* password = "hola1233";

const char* SERVER_IP = "172.20.10.5";  // IP del PC2 servidor
int SERVER_PORT = 5006;

WiFiClient client;

#define LED_PIN 8
void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);

  Serial.println("Iniciando WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  while (WiFi.status() != WL_CONNECTED) delay(500);

  while (!client.connect(SERVER_IP, SERVER_PORT)) delay(500);

  client.println("ESP32: Conectado");
  // Enviar estado al servidor
  client.println("ESP32: vivo");
}

void loop() {

  // Leer comandos del servidor
  if (client.available()) {
    String msg = client.readStringUntil('\n');
    msg.trim();

    Serial.print("Recibido: ");
    Serial.println(msg);

    if (msg == "LED=ON"){ digitalWrite(LED_PIN, LOW);
    client.print("LED ON");}
    if (msg == "LED=OFF") {digitalWrite(LED_PIN, HIGH);
    client.print("LED OFF");}
    if (msg == "ESTADO"){ 
    String val=String(!digitalRead(LED_PIN));
    client.print(val);}
  }
  // Enviar estado al servidor
  // client.println("ESP32: vivo");
    delay(500);
}