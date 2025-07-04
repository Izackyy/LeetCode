class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        vector<string> words = splitString(sentence);
        int searchLength = searchWord.length();

        for (int i = 0; i < words.size(); i++) {
            if (words[i].length() >= searchLength && 
                words[i].substr(0, searchLength) == searchWord) {
                
                return i + 1;
            }
        }
        return -1;
    }

private: 
    vector<string> splitString(string& sentence) {
        int start = 0;
        vector<string> words;

        while (start < sentence.length()) {
            int end = sentence.find(' ', start);
            if (end == string::npos) 
                end = sentence.length();

            words.push_back(sentence.substr(start, end - start));
            start = end + 1;
        }

        return words;
    }
};