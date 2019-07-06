#include "dht.h"
#define dht_apin A0 // Analog Pin sensor is connected to
 
dht DHT;

int led = 13;                // the pin that the LED is atteched to
int sensor = 2;              // the pin that the sensor is atteched to
int state = LOW;             // by default, no motion detected
int val = 0;                 // variable to store the sensor status (value)
float temp,hum =0;
int motion=0;
void setup() {
  pinMode(led, OUTPUT);      // initalize LED as an output
  pinMode(sensor, INPUT);    // initialize sensor as an input
  Serial.begin(9600);        // initialize serial

  Serial.begin(9600);
  delay(500);//Delay to let system boot
  ///Serial.println("DHT11 Humidity & temperature Sensor\n\n");
  delay(1000);//Wait before accessing Sensor
}

void loop(){

  
  DHT.read11(dht_apin);
  delay(500);
  //Serial.print("Current humidity = ");
    hum = DHT.humidity;
    //Serial.print(",");
    //Serial.print("temperature = ");
    temp =DHT.temperature; 
    //Serial.println("C  ");
    
    //delay(1000);//Wait 2 seconds before accessing sensor again.
 
  //Fastest should be once every two seconds.
  val = digitalRead(sensor);   // read sensor value
  if (val == HIGH) {           // check if the sensor is HIGH
    digitalWrite(led, HIGH);   // turn LED ON
    delay(500);
    motion = 1;
  } 
  else {
      digitalWrite(led, LOW); // turn LED OFF
      //delay(200);             // delay 200 milliseconds 
      motion  = 0;
  }
  Serial.print(temp);
  Serial.print(",");
  Serial.print(hum);
  Serial.print(",");
  Serial.println(motion);
 }
