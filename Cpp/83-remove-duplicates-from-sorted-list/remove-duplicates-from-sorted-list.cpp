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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* pre = head;

        if (head == NULL) return NULL;
        if (head->next == NULL) return head;

        ListNode* cur = pre->next;

        while (cur != NULL) {
            if (pre->val == cur->val) {
                pre->next = cur->next;
                cur = cur->next;
            } 
            else {
                cur = cur->next;
                pre = pre->next;
            }
        }
        return head;
    }
};