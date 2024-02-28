/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public ListNode rotateRight(ListNode head, int k) {
    if (head == null || k == 0) {
      return head;
    }
    int n = 0;
    ListNode curr = head;
    while (curr != null) {
      n++;
      curr = curr.next;
    }
    k = k % n;
    if (k == 0) {
      return head;
    }
    k = n - k;
    curr = head;
    while (k-- > 1) {
      curr = curr.next;
    }
    ListNode newHead = curr.next;
    curr.next = null;
    curr = newHead;
    while (curr != null && curr.next != null) {
      curr = curr.next;
    }
    curr.next = head;
    return newHead;
  }
}
