---
layout: page
title: Consistency of Distributed Controllers
permalink: /allprojects/DistributedControllers

---

#### Description
A potential problem that may arise in the domain of distributed control systems is the existence of more than one primary controller in redundancy plans that may lead to inconsistency. An algorithm called NRP FD is proposed to solve this issue by prioritizing consistency over availability. 
In this project, we modeled and formally verified NRP FD using Timed Rebeca and its model checker Afra. 
For model checking, we consider the regular system behaviour, and scenarios where we have failures of Distributed Control Nodes (DCN) and switches. We examine all the possible failure combinations of DCNs and switches at the start of handling an event and also at specific points in time and perform model checking to provide a comprehensive analysis.

We have discovered an issue in where we may have two primary controllers at the same time. We then provide a solution called Leasing NRP FD to mitigate the identified issue, thereby enhancing the robustness and reliability of such systems. 

It's worth noting that this project is undertaken in collaboration with ABB Industrial Automation, Process Control Platform, in Västerås, Sweden.


### MARS@ETAPS 2024 Version 
#### Case Studies
* NRP FD algorithm: [ [NRP FD] ](/assets/projects/DistributedControllers/NRPFD.zip)
 
* The extended version: [ [Leasing NRP FD] ](/assets/projects/DistributedControllers/LeasingNRPFD.zip)

We consider a homogeneous multi-controller system with two controllers, DCN1 and DCN2, the primary and backup controllers. The Primary is unique in the system; it interacts with the I/O devices. The backup is waiting and will become the primary if the primary fails. Two controllers must communicate and are connected via a network by passing messages through switches: the primary and the backup use two independent networks to have a more reliable and robust system. The backup has to know if the primary is present and functioning. The primary sends a HeartBeat message periodically to the backup over the two networks. Each controller has one switch per network as an NRP candidate, so each controller has a set of NRP candidates. The primary has one of the NRP candidates as its NRP. 

NRPs are introduced to help the backup ensure the primary is available. If several heartbeats are missed, the backup assumes that either the primary is down, or the network is disconnected. The backup pings the NRP, and if it receives an acknowledgement, it knows that the network is not disconnected and concludes that the primary is down. The primary also pings its NRP  before sending each heartbeat to ensure it always has an active NRP.
In our example, the first network includes three switches SwitchA1, SwitchA2, and SwitchA3, and the second network includes  SwitchB1, SwitchB2, and SwitchB3. The NRP candidate set for the primary is {SwitchA1, SwitchB1} and for the back up is {SwitchA3, SwitchB3}; SwitchA1 is the NRP. 

We have modeled failures in three scenarios. These situations lead to violations in NRP FD but would not cause any violation in the leasing NRP FD algorithm. For each, the corresponding code in which the failure is modeled is available. Note that the property file is similar to the NRP FD. 

1. Failures on every event. In this scenario, the following commands are placed at the beginning of each message server for DCNs and switches, simulating the possibility of their failure. <!---(minor modifications also required, e.g. uncomment else and its corresponding "}" for each).--> 

      //Possible failure for a DCN:
  
      // if(?(true,false)) nodeFail();

      //Possible failure for a Switch:

      //if(?(true,false)) switchFail();

     * [ [NRP FD algorithm + failures on every event] ](/assets/projects/DistributedControllers/NRPFD-C2-FailuresonEachEvent.rebeca)

3. Failures that occur at specific times. To create a situation where a violation would occur in NRP FD, one can for example set the switchA1failtime and switchB1failtime variables to 2500 to simulate simultaneous failures on both networks. 

   env int switchA1failtime = 2500;
   
   env int switchB1failtime = 2500;

   * [ [NRP FD algorithm + simultaneous failures] ](/assets/projects/DistributedControllers/NRPFD-C7-switchA1andswitchB1FailsSimultaneouslyAtTime2500.rebeca)

5. Transient failures. These failures could happen if, for instance, an attacker intentionally drops the heartbeats beyond the maximum allowed misses (max_missed_heartbeats) on both networks.

    * [ [NRP FD algorithm + transient failures] ](/assets/projects/DistributedControllers/NRPFD-C8-TransientError.rebeca)
  
### Gul's Fest 2025 Version 
In this version, we use Timed Rebeca to quantify simultaneous failures in distributed control systems by analyzing the timing of network failures that could lead to dual-primary scenarios. Failures are considered "simultaneous" if they occur within a critical time window determined by heartbeat periods and network delays. By incorporating nondeterministic failure timing in our Rebeca model, we verify that dual-primary situations are avoided when the interval between failures is greater than this threshold.

NRP FD algorithm with timing analysis: [ [NRP FD] ](/assets/projects/DistributedControllers/NRPFD-TimingAnalysis-GulFest.zip)

NRP FD algorithm with timing analysis, with full comments: [ [NRP FD] ](/assets/projects/DistributedControllers/NRPFD-TimingAnalysis-GulFest-WithFullComment.zip)

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Bahman Pourvatan
* Bjarne Johansson
* Zahra Moezkarimi
* Alessandro Papadopoulos

