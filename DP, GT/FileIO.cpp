#include <fstream>
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

vector<vector<int> > readData(const string& fileName) {
    ifstream inputFile(fileName);
    vector<vector<int> > data;
    int row, col;
    while (inputFile >> row >> col) {
        data.resize(row);
        for (int i = 0; i < row; i++) {
            data[i].resize(col);
            for (int j = 0; j < col; j++) {
                inputFile >> data[i][j];
            }
        }
    }
    inputFile.close();
    return data;
}

void displayData(vector<vector<int> > data) {
    for (const auto& row : data) {
        for (const auto& col : row) {
            cout << col << " ";
        }
        cout << endl;
    }
}

void displayTotal(vector<vector<int> > data) {
    int total = 0;
    for (const auto& row : data) {
        for (const auto& col : row) {
            total += col;
        }
    }
    cout << "Total: " << total << endl;
}

pair<int, int> findMax(vector<vector<int> > data) {
    int maxVal = INT_MIN;
    int maxRow = 0, maxCol = 0;
    for (int i = 0; i < data.size(); i++) {
        for (int j = 0; j < data[i].size(); j++) {
            if (data[i][j] > maxVal) {
                maxVal = data[i][j];
                maxRow = i;
                maxCol = j;
            }
        }
    }
    return make_pair(maxRow, maxCol);
}

void displayMax(vector<vector<int> > data) {
    auto result = findMax(data);
    cout << "Max value: " << data[result.first][result.second]
         << " at (" << result.first << ", " << result.second << ")" << endl;
}

int main() {
    string fileName = "data.txt";
    vector<vector<int> > data = readData(fileName);
    displayData(data);
    displayTotal(data);
    displayMax(data);
    return 0;
}
