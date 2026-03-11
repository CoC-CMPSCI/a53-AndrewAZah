#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int i, begin, end, sum = 0;

    // TODO: prompt user for begin and end values
    cout << "Enter begin and end values: ";
    cin >> begin >> end;

    // TODO: loop from begin to end and accumulate sum of even values
    for (i = begin; i <= end; i++) {
        if (i % 2 == 0) {
            sum += i;
        }
    }

    cout << "The sum of even values is " << sum << endl;
}
