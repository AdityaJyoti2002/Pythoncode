#include <stdio.h>

int minStepsToReach(int x) {
    return (x / 5) + (x % 5 > 0 ? 1 : 0);
}

int main() {
    int friendHouseCoordinate = 12;
    int minSteps = minStepsToReach(friendHouseCoordinate);
    printf("The elephant needs %d steps to reach his friend's house at point %d.\n", minSteps, friendHouseCoordinate);
    return 0;
}
