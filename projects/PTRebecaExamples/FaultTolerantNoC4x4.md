---
layout: page
title: Fault Tolerant NoC 4x4
permalink: /allprojects/PTRebecaExamples/FaultTolerantNoC4x4

---

#### Problem Description
NoC has emerged as a promising architecture paradigm for many-core systems. Globally Asynchronous Locally Synchronous (GALS) NoC has gained many attentions in designing of such systems. ASPIN (Asynchronous Scalable Packet switching Integrated Network) is a fully asynchronous two-dimensional GALS NoC design using XY routing algorithm. Using this algorithm, packets can only move along X direction first, and then along Y direction to reach their destination. In ASPIN, packets are transferred through channels, using four-phase handshake communication protocol. The protocol uses two signals, namely "Req" and "Ack" to implement four-phase handshaking protocol. To transfer a packet, first, the sender sends a request by rising "Req" signal, and waits for an acknowledgment which is raising "Ack" from the receiver. All the signals return to zero after a successful communication. There are four adjacent cores to each core and also four internal buffer for storing the incoming packets of different neighbors. 

In this version of the model, faulty cores are added to ASPIN. The probabilistic version of the case study is similar to the timed version presented before. The only difference is in case of a core fault, which results in routing in Y direction before completing movement in X direction.

#### Related Files
* The specification of the model [ [zip] ](/assets/projects/PTRebeca/case-studies/ASPIN-modified-faulty-v4.zip)
