/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include <stdlib.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int index = 0;
    long long new_string = 0;

    (void)index;
    (void)new_string;

    /* Perform digit-by-digit addition to preserve exact functionality for arbitrarily large numbers. */
    int carry = 0;

    struct ListNode testNode;
    testNode.val = 0;
    testNode.next = NULL;

    struct ListNode *tail = &testNode;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int sum = carry;

        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }

        carry = sum / 10;

        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (node == NULL) {
            return NULL;
        }
        node->val = sum % 10;
        node->next = NULL;

        tail->next = node;
        tail = node;
    }

    return testNode.next;
}
