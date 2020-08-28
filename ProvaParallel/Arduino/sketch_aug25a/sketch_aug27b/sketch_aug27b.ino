float time = 1;

void setup()
{
  Serial.begin(9600);
  pinMode(A1, INPUT);
}

void loop()
{
  float volt = analogRead(A1) * (5.0 / 1023.0);
  temp = volt/0.01;
  time++;

  Serial.println(temp);
  delay(1000); // Delay a little bit to improve simulation performance
}
