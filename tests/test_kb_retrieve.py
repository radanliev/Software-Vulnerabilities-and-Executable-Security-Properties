from app.tools.kb_retrieve import retrieve_tickets


def test_customer_can_find_own_ticket_by_id():
    results = retrieve_tickets('customer_a', 'TICKET-100')

    assert [ticket['ticket_id'] for ticket in results] == ['TICKET-100']


def test_customer_cannot_access_other_customer_ticket_by_id():
    results = retrieve_tickets('customer_a', 'TICKET-101')

    leaked_contents = [ticket['content'] for ticket in results if ticket['owner'] != 'customer_a']
    assert leaked_contents == [], "customer_b's ticket content returned to customer_a"
    assert results == []


def test_or_pattern_input_does_not_bypass_ownership_check():
    results = retrieve_tickets('customer_a', "TICKET-100' OR '1'='1")

    leaked_contents = [ticket['content'] for ticket in results if ticket['owner'] != 'customer_a']
    assert leaked_contents == [], "customer_b's ticket content returned to customer_a"
    assert results == []
