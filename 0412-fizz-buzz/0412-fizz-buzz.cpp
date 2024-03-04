class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> gay;
        for (int i = 1; i < n+1; i++) {
            if ((i%3) == 0 && (i%5) == 0) {
                cout << "FizzBuzz";
                gay.push_back("FizzBuzz");
            } 
            else if ((i%3)==0) {
                cout << "Fizz";
                gay.push_back("Fizz");
            }
            else if ((i%5)==0){
                cout << "Buzz";
                gay.push_back("Buzz");
            }
            else {
                gay.push_back(to_string(i));
                cout << i;
            }
        }
        return gay;
    }
};