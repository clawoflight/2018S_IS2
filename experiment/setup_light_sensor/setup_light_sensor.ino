const int S0 = 10;
const int S1 = 11;
const int S2 = 13;
const int S3 = 12;
const int OE = 7;

void setup() {
  Serial.begin(115200);
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(OE, OUTPUT);

  digitalWrite(S0, HIGH);
  digitalWrite(S1, HIGH);
  digitalWrite(S2, HIGH);
  digitalWrite(S3, LOW);
  digitalWrite(OE, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:

}
