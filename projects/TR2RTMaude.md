---
layout: page
title: Timed Rebeca to Realtime Maude Transformation
permalink: /allprojects/TR2RTMaude

---

#### Description

The actor model is one of the main models for distributed computation.  Timed Rebeca is a timed extension of the actor-based modeling language Rebeca. Although Rebeca is supported by a rich verification toolset, Timed Rebeca has not had an executable formal semantics, and has therefore had limited support for formal analysis. To resolve this limitation we provide a formal semantics of Timed Rebeca in Real-Time Maude. We have automated the translation from Timed Rebeca to Real-Time Maude, allowing Timed Rebeca models to be automatically analyzed using Real-Time Maude's reachability analysis tool and timed CTL model checker. This enables a formal model-based methodology which combines the convenience of intuitive modeling in Timed Rebeca with formal verification in Real-Time Maude.  
 
#### Tools
* Model Transformer: Shell script based toolset [ [zip] ](https://github.com/rebeca-lang/org.rebecalang.timedrebeca2rtmaude/raw/master/target/org.rebecalang.timedrebeca2rtmaude-1.0.0.zip), User manual [ [pdf] ](http://rebeca.cs.ru.is/files/document/TRtoRTM-UsersGuide.pdf)

#### Case Studies
* As one of the In this problem, the goal is to model a collision avoidance protocol for communication networks. This model is a modified version of the protocol studied in [this paper](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.25.4648). There are a number of stations connected via a shared medium and each station is composed of a user and its Interface to medium(called Slave). The assumptions are:
	- The shared medium does not corrupt or lose data,
	- It takes one unit of time to deliver the messages,
	- There is a controller component (called Master), which periodically and in a round-robin fashion, gives turn to the stations,
	- The medium broadcasts each message to all stations, and the receiving station takes its own messages based on the receiver ID of the message,
	- It takes two units of time for a Slave to process the incoming messages.
The desired properties of the system are following:
1. The protocol must be collision free.
1. The round-trip time of the protocol must be bounded.
Carrier Sense Multiple Access (CDMA) protocol with timing specification: [ [zip] ](/assets/projects/TR2RTMaude/case-studies/tcsma-rtmaude.zip)
* Other case studies including Timed Rebeca models and their corresponsing Realtime Maude models: [ [zip] ](http://rebeca.cs.ru.is/files/Case Studies.zip)

#### Project Members
* **<u>Ramtin Khosravi (Principal Investigator)</u>**
* **<u>Peter Csaba Ölveczky (Principal Investigator)</u>**
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Zeynab Sabahi-Kaviani
* Ehsan Khamespanah

#### Related Publications
* Zeynab Sabahi-Kaviani, Ramtin Khosravi, Peter Csaba Ölveczky, Ehsan Khamespanah, Marjan Sirjani: Formal semantics and efficient analysis of Timed Rebeca in Real-Time Maude, Science of Computer Programming, 2015 [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/scp/Sabahi-KavianiK15)

* Zeinab Sabahi-Kaviani, Ramtin Khosravi, Marjan Sirjani, Peter Csaba Ölveczky, and Ehsan Khamespanah: Formal Semantics and Analysis of Timed Rebeca in Real-Time Maude, FTSCS, 2013 [ [pdf] ](/assets/papers/2013/Timed-Rebeca-To-Timed-Maude.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/ftscs/Sabahi-KavianiKSOK13)
