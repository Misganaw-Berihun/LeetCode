class Solution {
public:
    string reformatDate(string date) {
        map<string, int> month = {
                    {"Jan" , 1},
                    {"Feb" , 2},
                    {"Mar" , 3}, 
                    {"Apr" , 4}, 
                    {"May" , 5}, 
                    {"Jun" , 6}, 
                    {"Jul" , 7}, 
                    {"Aug" , 8}, 
                    {"Sep" , 9},
                    {"Oct" , 10}, 
                    {"Nov" , 11}, 
                    {"Dec" , 12}
            };
        
        const char* delim = " ";
        
        vector<string> str;
        istringstream ss(date);
        string del;

        while(getline(ss, del, ' ')) {
              str.push_back(del);
        }
        
        string output = "";
        string yyyy = str[2];
        string mm = to_string(month[str[1]]);
        
        if (mm.length() == 1){
            mm = "0" + mm;
        }
        int temp = str[0].length() - 2;
        string dd = str[0].substr(0, temp);
        
        if (dd.length() == 1){
            dd = "0" + dd;
        }
        
        output = yyyy + "-" + mm + "-" + dd;
        return output;
    }
};