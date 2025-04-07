#include <stdio.h>
int stack[1000000];
int top = -1;

int isEmpty();
int pop();
int peak();
void push(int value);

int main() {
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        int command;
        scanf("%d", &command);
        if (command == 1) {
            int value;
            scanf("%d", &value);
            push(value);
        }
        if (command == 2) {
            printf("%d\n", pop());
        }
        if (command == 3) {
            printf("%d\n", top + 1);
        }
        if (command == 4) {
            printf("%d\n", isEmpty());
        }
        if (command == 5) {
            printf("%d\n", peak());
        }
    }
}

int isEmpty() {
    return top == -1;
}

int pop() {
    if (isEmpty()) {
        return -1;
    }
    
    top --;
    return stack[top + 1];
}

int peak() {
    if (isEmpty()) {
        return -1;
    }
    
    return stack[top];
}

void push(int value) {
    top ++;
    stack[top] = value;
}