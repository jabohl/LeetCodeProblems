#include <string>
#include <iostream>

class Solution {
public:
    bool isSubsequence(std::string s, const std::string& t) {
        for (char i : s) {
            if (t.find(i) == std::string::npos) {
                s.erase(std::remove(s.begin(), s.end(), i), s.end());
            }
        }
        int prev = 0;
        if (!s.empty()) {
            for (size_t i = 0; i < t.size(); ++i) {
                if (prev < (int)s.size()) {
                    if (s[prev] == t[i]) {
                        std::cout << s[prev] << std::endl;
                        ++prev;
                    }
                }
            }
        }
        return prev == (int)s.size();
    }
};
