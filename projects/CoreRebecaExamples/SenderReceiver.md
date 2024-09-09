---
layout: page
title: Sender Receiver
permalink: /projects/CoreRebecaExamples/SenderReceiver

---

#### Problem Description
Consider the above system, where a SENDER and a RECEIVER want to communicate over a potential faulty communication line. The Sender sends messages to the Receiver through a Medium. This Medium might lose the message and do not deliver it to the Receiver. The Sender waits for the Acknowledgement from the Receiver before sending the next message. This system somehow uses the “Stop and Wait” mechanism for managing the Rebecs. It is also supposed that the acknowledgement message will not be lost, and the medium declares the loss of a message to the sender.

<figure>
<img align="right" src="{{ "/assets/projects/Sysfier/case-studies/Sender-Receiver/sender_receiver.gif" | absolute_url }}" alt="" />
</figure>



#### Related Files
* The specification of the model [ [zip] ](/assets/projects/Sysfier/case-studies/Sender-Receiver.zip)
