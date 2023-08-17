 
 
 def splitList(self, head, head1, head2):
        cur=head
        start=head
        n=1
        while cur:
            if cur.next==start:
                break
            cur=cur.next
            n+=1
        end=cur
        secondpoint=head
        for i in range(n//2+n%2-1):
            secondpoint=secondpoint.next
        end.next=secondpoint.next
        second=secondpoint.next
        secondpoint.next=start
        return start,second