/*
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat,
and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.


Completed: November 14, 2021
*/

class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int max_dist = 0; 
        int running_max = 0;
        for (unsigned i = 0; i < seats.size(); i++) {
            if (seats[i] == 0) running_max++;
            else {
                if (running_max > max_dist)
                    max_dist = running_max;
                running_max = 0;
            }
        }
        if (running_max > max_dist)
            max_dist = running_max; 
        
        running_max = 0;
        if (seats[0]==0) {
            for (unsigned i = 0; i < seats.size(); i++) {
                if (seats[i] == 1) break;
                running_max++;
            }
        }
        max_dist = (max_dist+1)/2;
        if (running_max > max_dist) max_dist = running_max;
        
        running_max = 0;
        if (seats.back() == 0) {
            for (unsigned i = seats.size()-1; i >= 0; i--) {
                if (seats[i] == 1) break;
                running_max++;
            }
        }
        if (running_max > max_dist) max_dist = running_max;
        return max_dist;
    }
};
