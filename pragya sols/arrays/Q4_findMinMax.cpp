#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;

int main() {
    vector<int> arr = {12, 5, 34, 2, 19};
    // Concept: Instead of a manual loop, we use C++ STL algo
    // *min_element and *max_element give us the smallest/largest values instantly
    int minVal = *min_element(arr.begin(), arr.end());
    int maxVal = *max_element(arr.begin(), arr.end());

    cout << "Output:" << endl;
    cout << "Min=" << minVal << endl;
    cout << "Max=" << maxVal << endl;

    return 0;
}