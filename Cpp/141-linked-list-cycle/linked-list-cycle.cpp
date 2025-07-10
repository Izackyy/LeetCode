/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* front = head;

        while (front && front->next) {
            head = head->next;
            front = front->next->next;

            if (head == front) 
                return true;
        }

        return false;
    }
};