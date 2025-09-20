/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = new ListNode(0, head);
        ListNode* cur = temp;

        while (n > 0) {
            head = head->next;
            n--;
        }
        while (head != NULL) {
            head = head->next;
            cur = cur->next;
        }

        cur->next = cur->next->next;

        return temp->next;
    }
};