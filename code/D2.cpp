#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// Structure to represent an element in an array
struct Element {
    int value;
    int array_index;
    int index;
    
    bool operator<(const Element& other) const {
        return value < other.value;
    }
};

int max_total_money(int N, int M, int K, vector<vector<int>>& arrays) {
    int total_money = 0;
    priority_queue<Element> max_heap;

    // Initialize the max heap
    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= M - K; j++) {
            max_heap.push({arrays[i][j], i, j});
        }
    }

    // Perform operations
    for (int p = 1; p <= M - K + 1; p++) {
        Element max_element = max_heap.top();
        max_heap.pop();
        total_money += max_element.value;
        arrays[max_element.array_index][max_element.index] = 0;

        // Replace the used element in the heap
        if (max_element.index + 1 <= M - K) {
            max_heap.push({arrays[max_element.array_index][max_element.index + 1], max_element.array_index, max_element.index + 1});
        }
    }

    return total_money;
}

int main() {
    int N, M, K;
    cin >> N >> M >> K;
    vector<vector<int>> arrays(N, vector<int>(M));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arrays[i][j];
        }
    }

    int result = max_total_money(N, M, K, arrays);
    cout << result << endl;

    return 0;
}
