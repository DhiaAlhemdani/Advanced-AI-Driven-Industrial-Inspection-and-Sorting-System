/* Independent Servo Control – Each servo moves alone, no mirroring */

#include <Servo.h>

Servo servoA;
Servo servoB;

// Simple circular buffer for each servo
#define QUEUE_SIZE 10
char queueA[QUEUE_SIZE];   // was QUE_SIZE – fixed
char queueB[QUEUE_SIZE];   // fixed
int headA = 0, tailA = 0, countA = 0;
int headB = 0, tailB = 0, countB = 0;

// State for each servo
bool activeA = false;
bool activeB = false;
unsigned long timerA = 0;
unsigned long timerB = 0;
bool pendingA = false;
bool pendingB = false;

// Proximity sensor pins
const int PROX_A_PIN = 2;
const int PROX_B_PIN = 3;

// Timing
const unsigned long HOLD_TIME = 500;

// ----- Position settings (fully independent) -----
const int REST_A = 35;
const int ACTIVE_A = 0;
const int REST_B = 0;
const int ACTIVE_B = 35;

void setup() {
    Serial.begin(9600);
    pinMode(PROX_A_PIN, INPUT);
    pinMode(PROX_B_PIN, INPUT);

    servoA.attach(9);//reprocess
    servoB.attach(10);//defected

    servoA.write(REST_A);
    servoB.write(REST_B);   // fixed missing argument
}

bool enqueue(char cmd, char* queue, int& head, int& tail, int& count) {
    if (count >= QUEUE_SIZE) return false;
    queue[head] = cmd;
    head = (head + 1) % QUEUE_SIZE;
    count++;
    return true;
}

char dequeue(char* queue, int& tail, int& count) {
    if (count == 0) return '\0';
    char cmd = queue[tail];
    tail = (tail + 1) % QUEUE_SIZE;
    count--;
    return cmd;
}

void executeCommand(char cmd) {
    if (cmd == 'A' && !activeA && !pendingA) {
        pendingA = true;
    } else if (cmd == 'B' && !activeB && !pendingB) {
        pendingB = true;
    }
}

void loop() {
    unsigned long now = millis();

    // Debug print (optional)
    static unsigned long lastPrint = 0;
    if (now - lastPrint > 1000) {
        Serial.print("Sensor A: ");
        Serial.print(digitalRead(PROX_A_PIN));
        Serial.print(" | Sensor B: ");
        Serial.println(digitalRead(PROX_B_PIN));
        lastPrint = now;
    }

    // ---- Start Servo A when proximity A detects bottle ----
    if (pendingA && digitalRead(PROX_A_PIN) == LOW) {
        servoA.write(ACTIVE_A);
        timerA = now;
        activeA = true;
        pendingA = false;
    }

    // ---- Start Servo B when proximity B detects bottle ----
    if (pendingB && digitalRead(PROX_B_PIN) == LOW) {
        servoB.write(ACTIVE_B);
        timerB = now;
        activeB = true;
        pendingB = false;
    }

    // ---- Return Servo A after hold time ----
    if (activeA && (now - timerA) >= HOLD_TIME) {
        servoA.write(REST_A);
        activeA = false;
        // Process next command in A's queue
        char nextCmd = dequeue(queueA, tailA, countA);
        if (nextCmd != '\0') executeCommand(nextCmd);
    }

    // ---- Return Servo B after hold time ----
    if (activeB && (now - timerB) >= HOLD_TIME) {
        servoB.write(REST_B);
        activeB = false;
        char nextCmd = dequeue(queueB, tailB, countB);
        if (nextCmd != '\0') executeCommand(nextCmd);
    }

    // ---- Serial command handling (independent) ----
    if (Serial.available()) {
        char cmd = Serial.read();
        if (cmd == 'A') {
            if (!activeA && !pendingA) {
                executeCommand(cmd);
            } else {
                enqueue(cmd, queueA, headA, tailA, countA);
            }
        } else if (cmd == 'B') {
            if (!activeB && !pendingB) {
                executeCommand(cmd);
            } else {
                enqueue(cmd, queueB, headB, tailB, countB);
            }
        }
    }
}