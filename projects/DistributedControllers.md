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

#### Case Studies
* NRP FD algorithm: [ [NRP FD] ](/assets/projects/DistributedControllers/NRPFD.zip)
 
* The extended version: [ [Leasing NRP FD] ](/assets/projects/DistributedControllers/LeasingNRPFD.zip)


We have modeled failures in three scenarios. These situations lead to violations in NRP FD but would not cause any violation in the leasing NRP FD algorithm.

1. Failures on every event. In this scenario, the following commands should be left uncommented at the beginning of each message server for DCNs and switches, simulating the possibility of their failure (minor modifications also required, e.g. uncomment else and its corresponding "}" for each). 

      //Possible failure for a DCN:
  
      // if(?(true,false)) nodeFail();

      //Possible failure for a Switch:

      //if(?(true,false)) switchFail();

2. Failures that occur at specific times. To create a situation where a violation would occur in NRP FD, you can for example set the switchA1failtime and switchB1failtime variables to 2500 to simulate simultaneous failures on both networks. 

   env int switchA1failtime = 2500;
   
   env int switchB1failtime = 2500;

4. Transient failures. To activate the mechanism we have added to our model to simulate a transient failure, uncomment the following two lines:

    // attacker=1; (in  msgsrv ping_timed_out)

    // attacker++; (in msgsrv runMe)

  
  

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Bahman Pourvatan
* Bjarne Johansson
* Zahra Moezkarimi
* Alessandro Papadopoulos

