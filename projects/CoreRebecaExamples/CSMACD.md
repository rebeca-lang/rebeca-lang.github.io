---
layout: page
title: CSMA-CD
permalink: /projects/CoreRebecaExamples/CSMACD

---

#### Problem Description

In this problem we will study the Media Access Control (Mac) sub layer of the Carrier Sense, Multiple Access with Control Detection (CSMA/CD) communication protocol. The protocol specification consists of two MAC entities, MAC1 and MAC2, interconnected by a bi-directional medium M. The MAC entities are identical and can both transmit and receive messages over the medium. This means that collisions may occur on the medium (if the two MAC's transmit simultaneously). It is assumed that collisions will be detected in the medium and signaled to both MAC1 and MAC2.


	

<figure>
<img align="right" src="{{ "/assets/projects/Sysfier/case-studies/CSMA-CD/csma-cd-overview.gif" | absolute_url }}" alt="Overview of the MAC sub layer" />
<figcaption>Overview of the MAC sub layer</figcaption>
</figure>

A model of the protocol is taken from _"Verifying a CSMA/CD Protocol with CCS"_ by Joachim Parrow. The specification uses the following synchronization actions to describe the protocol events:

1. send - service provided by Mac which reacts by transmitting a message,
1. rec - (receive) service provided by Mac, indicates that a message is ready to be received,
1. b - (begin) Mac begins message transmission to M,
1. e - (end) Mac terminates message transmission to M,
1. br - (begin receive) M begins message delivery to Mac,
1. er - (end receive) M terminates message delivery to Mac,
1. c - (collision) Mac is notified that a collision has occurred on M.

Note that a message transmission is not modeled by a single action. Instead the start of a transmission and the end of a transmission are modeled by two separate actions (the actions b(r) and e(r)). This is needed as there may be collisions detected in the middle of a transmission. Note also that we use indexes on all actions, as there are two identical MAC entities.

<figure>
<img align="right" src="{{ "/assets/projects/Sysfier/case-studies/CSMA-CD/mac1.gif" | absolute_url }}" alt="MAC1" />
<figcaption>MAC1</figcaption>
</figure>

Initially, MAC1 accepts a service call (send1?). The MAC initiates transmission (b1!), unless a message is in the process of being received. If the transmission is successfully terminated (e1!) new messages can be transmitted and the process is repeated. If a collision occurs (c1?) the MAC attempts re-transmission of the message. In all states (except when a message is being transmitted) the MAC is willing to start receiving. A message may be received (br1?) after which the MAC may not begin message transmission before the end of message (er1?) has been received and the MAC has signaled that the message is ready to be delivered (rec1!). However, the MAC may receive a send request (send1?) if there is not already another request waiting. 

<figure>
<img align="right" src="{{ "/assets/projects/Sysfier/case-studies/CSMA-CD/m.gif" | absolute_url }}" alt="The medium M" />
<figcaption>The medium M</figcaption>
</figure>

Initially, the medium accepts transmission from one of the MAC's (b1? or b2?). We assume MAC1 (b1?) starts transmitting first (the case for b2? is symmetric). The medium is assumed to be "half-duplex" meaning that a full message must be transmitted (br2!, e1?, er2!) before the next message can be accepted. If the receiving MAC (i.e. MAC2) starts transmission (b2?) the medium interrupts the transmission and signals collision (c1!, c2!) to both MAC1 and MAC1 (in any order).

#### Regular Model

To model the algorithm, we use a message server for each state that MAC or Medium enters. For the messages they transfer, Message Servers are used. This is because the CSMA algorithm is Synchronous by nature but our language is Asynchronous. The code generates the access violation error, so we were not able to run the compute_reachable command for the code in NuSMV, this is perhaps due to the great number of states that is produces during the execution. We found some semantic errors in the code, but since the compositional form has less states, we added them in our so-called compositional code which is described in the description for that algorithm.

#### Compositional Verification

We also worked on the compositional form of the CSMA algorithm.
In this model, MAC sends messages to Medium and Medium sometimes (non-deterministically) reports a collision. It also send messages to the MAC in a nondeterministic way. To prevent the Medium from sending too many messages and resulting a state explosion, the Medium decides whether or not to send only after it receives a message from MAC. This algorithm run out of queue length probably because MAC puts messages in the Medium's queue and does it again and again, but since the queue has changed, SMV assumes that the states are new so again gives the turn to the MAC, and thinks that it is a Fair running. this is perhaps the reason for the state explosion. To avoid it, we somehow synched the messages, in the way we had done for Eating Philosophers problem. Checking the queue length again was false with a queue size of 10.
There exist other problem too, which is again due to the nature of the algorithm being synchronous. In the last version we have incorrectly checked the collision occurrence in the transfer state (refer to the code and the state chart please) but since the message from Medium will be placed after the transfer message in the MAC's queue, this results in a fault behavior. Next we are going to correct this. 

#### Related Files
* The specification of the model [ [zip] ](/assets/projects/Sysfier/case-studies/CSMA-CD.zip)
