/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
/*
 * Instituto TecnolÃ³gico de Costa Rica
 * Computer Engineering
 * Taller de ProgramaciÃ³n
 * 
 * Código Servidor
 * Implementación del servidor NodeMCU
 * Proyecto 2, semestre 1
 * 2019
 * 
 * Profesor: Milton Villegas Lemus
 * Autor: Santiago Gamboa RamÃ­rez
 * 
 * Restricciónes: Biblioteca ESP8266WiFi instalada
 */
 /*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

 /*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
#include <ESP8266WiFi.h>
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
//Cantidad maxima de clientes es 1
#define MAX_SRV_CLIENTS 1
//Puerto por el que escucha el servidor
#define PORT 7070
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
/*
 * ssid: Nombre de la Red a la que se va a conectar el Arduino
 * password: Contraseña de la red
 * 
 * Este servidor no funciona correctamente en las redes del TEC,
 * se recomienda crear un hotspot con el celular
 */
//const char* ssid = "Aparta 4";
//const char* password = "jjhd0921";
const char* ssid = "JJVV";
const char* password = "123456789";
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
// servidor con el puerto y variable con la maxima cantidad de 
WiFiServer server(PORT);
WiFiClient serverClients[MAX_SRV_CLIENTS];
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
/* 
 * Intervalo de tiempo que se espera para comprobar que haya un nuevo mensaje
 */
unsigned long previousMillis = 0, temp = 0;
const long interval = 100;
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
/*
 * Pin donde está conectado el sensor de luz
 * Señal digital, lee 1 si hay luz y 0 si no hay.
 * Variables para manejar las luces con el registro de corrimiento.
 * Utilizan una función propia de Arduino llamada shiftOut.
 * shiftOut(ab,clk,LSBFIRST,data), la función recibe 2 pines, el orden de los bits 
 * y un dato de 8 bits.
 * El registro de corrimiento tiene 8 salidas, desde QA a QH. Nosotros usamos 6 de las 8 salidas
 * Ejemplos al enviar data: 
 * data = B00000000 -> todas encendidas
 * data = B11111111 -> todas apagadas
 * data = B00001111 -> depende de LSBFIRST o MSBFIRST la mitad encendida y la otra mitad apagada
 */
#define ldr D7
#define ab  D6 
#define clk D8
/*
 * Variables para controlar los motores.
 * EnA y EnB son los que habilitan las salidas del driver.
 * EnA = 0 o EnB = 0 -> free run (No importa que haya en las entradas el motor no recibe potencia)
 * EnA = 0 -> Controla la potencia (Para regular la velocidad utilizar analogWrite(EnA,valor), 
 * con valor [0-1023])
 * EnB = 0 -> Controla la dirección, poner en 0 para avanzar directo.
 * In1 e In2 son inputs de driver, controlan el giro del motor de potencia
 * In1 = 0 ∧ In2 = 1 -> Moverse hacia adelante
 * In1 = 1 ∧ In2 = 0 -> Moverse en reversa
 * In3 e In4 son inputs de driver, controlan la dirección del carro
 * In3 = 0 ∧ In4 = 1 -> Gira hacia la izquierda
 * In3 = 1 ∧ In4 = 0 -> Gira hacia la derecha
 */
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
//MOTOR DERECHA
int OUTPUT4 = 16;
int OUTPUT3 = 5;
//MOTOR IZQUIERDA
int OUTPUT2 = 4;
int OUTPUT1 = 0;
//ENABLE
int ENA = 2; /* GPIO02(D4) ->Motor-A Enable */
int ENB = 14; /* GPIO14(D5) ->Motor-B Enable */
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
/**
 * Variables
 * Función de configuración.
 * Se ejecuta la primera vez que el módulo se enciende.
 * Si no puede conectarse a la red especificada entra en un ciclo infinito 
 * hasta ser reestablecido y volver a llamar a la función de setup.
 * La velocidad de comunicación serial es de 115200 baudios, tenga presente
 * el valor para el monitor serial.
 */
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
void setup() {
  Serial.begin(115200);
  pinMode(OUTPUT4,OUTPUT);
  pinMode(OUTPUT3,OUTPUT);
  pinMode(OUTPUT2,OUTPUT);
  pinMode(OUTPUT1,OUTPUT);

  pinMode(ENB, OUTPUT); 
  pinMode(ENA, OUTPUT);

  pinMode(clk,OUTPUT);
  pinMode(ab,OUTPUT);
  pinMode(ldr,INPUT);
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  //ip estática para el servidor JJVV
  IPAddress ip(192,168,43,24);
  IPAddress gateway(192,168,43,1);
  IPAddress subnet(255,255,255,0);
  WiFi.config(ip, gateway, subnet);
  // ip estática para el servidor Aparta 4
  //IPAddress ip(192,168,0,200);
  //IPAddress gateway(192,168,0,1);
  //IPAddress subnet(255,255,255,0);
  //WiFi.config(ip, gateway, subnet);
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  // Modo para conectarse a la red
  WiFi.mode(WIFI_STA);
  // Intenta conectar a la red
  WiFi.begin(ssid, password);
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  uint8_t i = 0;
  while (WiFi.status() != WL_CONNECTED && i++ < 20) delay(500);
  if (i == 21) {
    Serial.print("\nCould not connect to: "); Serial.println(ssid);
    while (1) delay(500);
  } else {
    Serial.print("\nConnection Succeeded to: "); Serial.println(ssid);
    Serial.println(".....\nWaiting for a client at");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
    Serial.print("Port: ");
    Serial.print(PORT);
  }
  server.begin();
  server.setNoDelay(true);
}
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
/*
 * Función principal que llama a las otras funciones y recibe los mensajes del cliente
 * Esta función comprueba que haya un nuevo mensaje y llama a la función de procesar
 * para interpretar el mensaje recibido.
 */
void loop() {
  
  unsigned long currentMillis = millis();
  uint8_t i;
  //check if there are any new clients
  if (server.hasClient()) {
    for (i = 0; i < MAX_SRV_CLIENTS; i++) {
      //find free/disconnected spot
      if (!serverClients[i] || !serverClients[i].connected()) {
        if (serverClients[i]) serverClients[i].stop();
        serverClients[i] = server.available();
        continue;
      }
    }
    //no free/disconnected spot so reject
    WiFiClient serverClient = server.available();
    serverClient.stop();
  }

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    for (i = 0; i < MAX_SRV_CLIENTS; i++) {
      // El cliente existe y está conectado
      if (serverClients[i] && serverClients[i].connected()) {
        // El cliente tiene un nuevo mensaje
        if(serverClients[i].available()){
          // Leemos el cliente hasta el caracter '\r'
          String mensaje = serverClients[i].readStringUntil('\r');
          // Eliminamos el mensaje leído.
          serverClients[i].flush();
          
          // Preparamos la respuesta para el cliente
          String respuesta; 
          procesar(mensaje, &respuesta);
          Serial.println(mensaje);
          // Escribimos la respuesta al cliente.
          serverClients[i].println(respuesta);
        }  
        serverClients[i].stop();
      }
    }
  }
}
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
/*
 * Función para dividir los comandos en pares llave, valor
 * para ser interpretados y ejecutados por el Carro
 * Un mensaje puede tener una lista de comandos separados por ;
 * Se analiza cada comando por separado.
 * Esta función es semejante a string.split(char) de python
 * 
 */
void procesar(String input, String * output){
  //Buscamos el delimitador ;
  Serial.println("Checking input....... ");
  int comienzo = 0, delComa, del2puntos;
  bool result = false;
  delComa = input.indexOf(';',comienzo);
  
  while(delComa>0){
    String comando = input.substring(comienzo, delComa);
    Serial.print("Processing comando: ");
    Serial.println(comando);
    del2puntos = comando.indexOf(':');
    /*
    * Si el comando tiene ':', es decir tiene un valor
    * se llama a la función exe 
    */
    if(del2puntos>0){
        String llave = comando.substring(0,del2puntos);
        String valor = comando.substring(del2puntos+1);

        Serial.print("(llave, valor) = ");
        Serial.print(llave);
        Serial.println(valor);
        //Una vez separado en llave valor 
        *output = implementar(llave,valor); 
    }
    else if(comando == "sense"){
      *output = getSense();         
    }
    /**
     * ## AGREGAR COMPARACIONES PARA COMANDOS SIN VALOR
     * EJEM: else if (comando == CIRCLE) {
     *  
     * } 
     */
    else{
      Serial.print("Comando no reconocido. Solo presenta llave");
      *output = "Undefined key value: " + comando+";";
    }
    comienzo = delComa+1;
    delComa = input.indexOf(';',comienzo);
  }
}
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
String implementar(String llave, String valor){
  String result="ok;";
  Serial.print("Comparing llave: ");
  Serial.println(llave);
  int Valor = valor.toInt();
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  if(llave == "pwm"){
    Serial.print("Move....: ");
    Serial.println(valor);
    if(valor.toInt()>0 and valor.toInt()<=1023){
      Serial.println("Valor positivo para PWM");
      digitalWrite(ENB, HIGH);
      analogWrite(OUTPUT3, Valor);
      digitalWrite(OUTPUT4, LOW);
    }
    else if(valor.toInt()<0 and valor.toInt()>=-1023){
      Serial.println("Valor negativo para PWM");
      digitalWrite(ENB,HIGH);
      digitalWrite(OUTPUT3, LOW);
      analogWrite(OUTPUT4, -Valor);
    }
    else{
      Serial.println("Valor neutro para PWM");
      digitalWrite(ENB,HIGH);
      digitalWrite(OUTPUT3, LOW);
      digitalWrite(OUTPUT4, LOW); 
    } 
  }
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  else if(llave == "dir"){
    switch (valor.toInt()){
      case 1:
        Serial.println("Girando derecha");
        digitalWrite(ENA, HIGH);  
        digitalWrite(OUTPUT1, HIGH);
        digitalWrite(OUTPUT2, LOW);
        break;
      case -1:
        Serial.println("Girando izquierda");
        digitalWrite(ENA, HIGH);
        digitalWrite(OUTPUT1, LOW);
        digitalWrite(OUTPUT2, HIGH);
        break;
       default:
        Serial.println("directo");
        digitalWrite(ENA, HIGH);
        digitalWrite(OUTPUT1, LOW);
        digitalWrite(OUTPUT2, LOW);
        break;
    }
  }
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  else if(llave[0] == 'l'){
    Serial.println("Cambiando Luces");
    Serial.print("valor luz: ");
    Serial.println(valor);
    int vsensor = digitalRead(ldr);
    byte data = B11111111;
    //Recomendación utilizar operadores lógico de bit a bit (bitwise operators)
    switch (llave[1]){
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      case 'f':
        Serial.println("Luces Frontales");
        data = B11001111;
        break;
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      case 'b':
        Serial.println("Luces Traseras");
        data = B00111111;
        break;
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      case 'l':
        Serial.println("Direccionales Izquierda");
        data = B10101111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B10101111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B10101111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B10101111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B10101111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B10101111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B10101111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B10101111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        break;
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      case 'r':
        Serial.println("Direccionales Derecha");
        data = B01011111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B01011111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B01011111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B01011111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B01011111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B01011111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B01011111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B01011111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        break;
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      case 'o':
        Serial.println("Luces Apagadas");
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        break;
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      case 'a':
        Serial.println("Luces Encendidas");
        data = B00000011;
        shiftOut(ab, clk, LSBFIRST, data);
        break;
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      case 'x':
        Serial.println("Luces encendidas según sensor");
        if(vsensor == 0){ 
          data = B00000011;
          shiftOut(ab, clk, LSBFIRST, data);
        }
        else if(vsensor == 1){
          data = B11111111;
          shiftOut(ab, clk, LSBFIRST, data);
        }
        break;
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      case 'p':
        Serial.println("Parking");
        data = B00001111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B00001111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B00001111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B00001111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B00001111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B00001111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B00001111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B00001111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
        delay(500);
        
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
      default:
        Serial.println("Ninguna de las anteriores");
        data = B11111111;
        shiftOut(ab, clk, LSBFIRST, data);
    }
    //data VARIABLE QUE DEFINE CUALES LUCES SE ENCIENDEN Y CUALES SE APAGAN
    shiftOut(ab, clk, LSBFIRST, data);
  }
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  else if (llave == "CIRCLE"){
    Serial.println("CIRCLE");
    Serial.println(valor);
    digitalWrite(ENA,HIGH);
    digitalWrite(ENB,HIGH);
    digitalWrite(OUTPUT1, HIGH);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (2000);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, LOW);
    digitalWrite(OUTPUT4, LOW);     
  }
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  else if (llave == "INFINITE"){
    Serial.println("INFINITE");
    Serial.println(valor);
    digitalWrite(ENA,HIGH);
    digitalWrite(ENB,HIGH);
    digitalWrite(OUTPUT1, HIGH);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (2000);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, HIGH);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (2000);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, LOW);
    digitalWrite(OUTPUT4, LOW); 
  }
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  else if (llave == "ZIGZAG"){
    Serial.println("ZIGZAG");
    Serial.println(valor);
    digitalWrite(ENA,HIGH);
    digitalWrite(ENB,HIGH);
    digitalWrite(OUTPUT1, HIGH);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (700);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, HIGH);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (500);
    digitalWrite(OUTPUT1, HIGH);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (700);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, HIGH);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (500);
    digitalWrite(OUTPUT1, HIGH);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (700);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, HIGH);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (500);
    digitalWrite(OUTPUT1, HIGH);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (700);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, HIGH);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (500);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, LOW);
    digitalWrite(OUTPUT4, LOW); 
  }
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  else if(llave == "CUSTOM"){
    Serial.println("CUSTOM");
    Serial.println(valor);
    digitalWrite(ENA,HIGH);
    digitalWrite(ENB,HIGH);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (2000);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, LOW);
    digitalWrite(OUTPUT4, HIGH);
    delay (00);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (500);
    digitalWrite(OUTPUT1, HIGH);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, HIGH);
    digitalWrite(OUTPUT4, LOW);
    delay (500);
    digitalWrite(OUTPUT1, LOW);
    digitalWrite(OUTPUT2, LOW);
    digitalWrite(OUTPUT3, LOW);
    digitalWrite(OUTPUT4, LOW);
        
  }
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
  /**
   * El comando tiene el formato correcto pero no tiene sentido para el servidor
   */
  else{
    result = "Undefined key value: " + llave+";";
    Serial.println(result);
  }
  return result;
}
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
/**
 * Función para obtener los valores de telemetría del auto
 */
String getSense(){
  //# EDITAR CÓDIGO PARA LEER LOS VALORES DESEADOS
  int batteryLvl = -1;
  int light = -1;

  // EQUIVALENTE A UTILIZAR STR.FORMAT EN PYTHON, %d -> valor decimal
  char sense [16];
  sprintf(sense, "blvl:%d;ldr:%d;", batteryLvl, light);
  Serial.print("Sensing: ");
  Serial.println(sense);
  return sense;
}
/*//////////////////////////////////////////////////////////////////////////////////////////////////////*/
