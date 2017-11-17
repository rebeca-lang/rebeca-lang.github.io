---
layout: page
title: Ticket Service System
permalink: /allprojects/TAROExamples/TicketService

---

#### Problem Description
The model consists of three reactive classes: *TicketService*, *Agent*, and *Customer*. *Customer* sends the **ticket issue** message to *Agent* and *Agent* forwards the issue to *TicketService*. *TicketService* rebec replies to *Agent* by sending a **ticket issued** message and *Agent* responds to *Customer* by sending the issued ticket identifier. As shown in line 12 of the model, issuing the ticket takes three time units (based on the configuration parameters, the issueDelay initial value equals to three). In addition, line 24 shows that *Agent* waits for five time units for *TicketService* to take the requested message and starts serving it.


#### Related Files
* The specification of the model [ [Rebeca model] ](/assets/projects/TARO/case-studies/ticketservice.rebeca)
