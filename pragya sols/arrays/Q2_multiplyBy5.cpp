#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr = {1, 2, 3};
    cout << "Output: ";
    // Concept: Using a reference (&x) in the loop
    // This allows to modify the actual memory of the array directly without needing index 'i'
    for (int &x : arr) {
        x = x * 5; 
        cout << x << " ";
    }
    cout << endl;
    return 0;
}