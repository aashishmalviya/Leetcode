​
​
​
​
The crux of this question is : Jahaan pe last string true mili ho, wahi se next string chalu hona expect karte hain
​
Tabhi s.substr(j, i-j) me immediate aage wala string milega.
​
Kyonki agar mactching string j pe end ho raha ho to hum i ko true kar rahe hain where j<i.
l e e t c o d e
0 1 2 3 4 5 6 7
string mila 3 pe, but dp[4] = true hua. Same for j=7, but dp[8] = true;
finally we check dp[8] where 8 = size is true or not.
​
agar beech me koi extra char aa jayega to dp[j] true nahi hua hoga
l e e t X c o d e
0 1 2 3 4 5 6 7
Yahaan dp[4] tp true hai but X k liye dp[5] true nahi hoga.